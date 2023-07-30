import sqlite3

# Open database
conn = sqlite3.connect('revision.db')

# Create table
c = conn.cursor()
c.execute('''CREATE TABLE revision
             (topic text, questionname text, questionlink text, code text)''')

conn.close()
