import json
import sqlite3

conn = sqlite3.connect('coursesdatabase.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Members;

CREATE TABLE User(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Members(
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY(user_id, course_id)
)
''')

file_string = open("roster_data.json").read()
data_list = json.loads(file_string)

""" How the data is in the JSON File:
[
    [ "Charley", "si110", 1 ],
    [ "Mea", "si110", 0 ],
    ....,
    ....
]"""
for row in data_list:
    name = row[0]
    course = row[1]
    # Role 1 is teacher and 0 is student
    role = row[2]
    print(name, course)

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name=?', (name,))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (course,))
    cur.execute('SELECT id FROM Course WHERE title=?', (course,))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Members (user_id, course_id, role)
                VALUES (?, ?, ?)''', (user_id, course_id, role))

    conn.commit()
