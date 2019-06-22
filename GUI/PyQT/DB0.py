import sqlite3
class DBPyQT0:
    def __init__(self):
        self.db = None
        self.cur = None
        self.dbAc()
    def dbAc(self):
        self.db = sqlite3.connect(r"D:\İbrahim EDİZ\Ornekler\OrnekDB\chinook.db")
        self.cur = self.db.cursor()
    
    def listele(self):
        liste = []
        sorgu = """
        SELECT CustomerId,
        FirstName,
        LastName
        FROM customers;
        """
        liste = self.cur.execute(sorgu).fetchall()
        return liste
