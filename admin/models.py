import sqlite3 as sql
from admin import db

class Users(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(64), nullable=True)
    username = Column(String(64), nullable=True)
    password = Column(String(64), nullable=True)
    age = Column(Integer, nullable=True)

    def logincheck(self):
        con = sql.connect("userdatabase.db")
        cur = con.cursor()
        cur.execute("SELECT username, password FROM users")
        users = cur.fetchall()
        con.close()
        return users

    def insertuser(username, password,email,age):
        con = sql.connect("userdatabase.db")
        cur = con.cursor()
        cur.execute("INSERT INTO users (username,password,email,age) VALUES (?,?,?,?)", (username, password,email,age))
        con.commit()
        con.close()