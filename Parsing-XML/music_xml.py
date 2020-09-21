import xml.etree.ElementTree as ET
import sqlite3

# First of all, I will connect to the sql file and delete the table if EXISTS

conn = sqlite3.connect('tracksdb.sqlite')
cur = conn.cursor()

# Make new tables using executescript
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# It's time to XML Parsing
filename = "Library.xml"
tree = ET.parse(filename)

"""
I'm going to find all the tracks in his respective dictionary. Those are in
the third order dictionary
"""
all_tracks = tree.findall('dict/dict/dict')
print('Number of tracks:', len(all_tracks))

"""This is how every third order dict child tags look like:
<key>Track ID</key><integer>369</integer>
<key>Name</key><string>Another One Bites The Dust</string>
<key>Artist</key><string>Queen</string>
"""


def lookup(dictionary, value):
    """
    This function will scan all the dictionary and return the content of the
    'key' tag if the content of that key tag is the same as the function Second
    parameter 'value'. Else, return None
    """
    found = False
    for child_element in dictionary:
        if found:
            return child_element.text
        if child_element.tag == 'key' and child_element.text == value:
            found = True
    return None


for track in all_tracks:
    # If there is no track in the dictionary, continue
    if lookup(track, 'Track ID') is None:
        continue

    name = lookup(track, 'Name')
    artist = lookup(track, 'Artist')
    album = lookup(track, 'Album')
    length = lookup(track, 'Total Time')
    count = lookup(track, 'Play Count')
    rating = lookup(track, 'Rating')

    """
    Manage if there is no track name, artist or album. Cuz I don't want to put
    None in my database
    """
    if name is None or artist is None or album is None:
        continue

    print(name, artist, album, length, count, rating)
