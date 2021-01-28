import sqlite3

class Database:

    def __init__(self,data):
        self.conn = sqlite3.connect(data)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, t text, a text, y integer,i integer)")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        return self.cur.fetchall()

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE t=? OR a=? OR y=? OR i=?",(title,author,year,isbn))
        return self.cur.fetchall()

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()
        
    def updatedata(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET t=?, a=?, y=?, i=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()

    def update(self,tData):
        self.updatedata(tData[0],tData[1],tData[2],tData[3],tData[4])
