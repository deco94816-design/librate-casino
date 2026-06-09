import sqlite3
c = sqlite3.connect('optimus.db')
print(c.execute("PRAGMA table_info('deposits');").fetchall())
