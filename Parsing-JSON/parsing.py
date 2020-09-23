import json
import sqlite3

conn = sqlite3.connect('coursesdatabase.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

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
