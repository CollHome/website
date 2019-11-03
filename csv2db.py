#!/usr/bin/env python3
import csv
import sqlite3

conn = sqlite3.connect('collhome.db')
c = conn.cursor()
with open('collhome.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        c.executemany('INSERT INTO Chapters (university, location, contactname, chapteremail, founderemails) VALUES (?,?,?,?,?)', (row,))

conn.commit()
