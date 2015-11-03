"""import sqlite3

conn = sqlite3.connect("blog.db")

c = conn.cursor()

q = "CREATE TABLE  user(uid integer, username text, password text)"
c.execute(q)

q = "CREATE TABLE post(pid integer, uid integer, title text, content text)"
c.execute(q)

q ="CREATE TABLE comment(cid integer, pid integer, uid integer, content text)"
c.execute(q)

conn.commit()
conn.close()
"""
