import sqlite3 as sql

db = sql.connect(r"D:\İbrahim EDİZ\Ornekler\OrnekDB\chinook.db")
cur = db.cursor()

artisname = input("Artist Adı Giriniz")
sorgu = "insert into artists (Name) values ('{}')".format(artisname)
cur.execute(sorgu)
db.commit()


query = """
select * from artists where name like '{}%'
""".format(input("Aramak istediğin sanatçılar"))
cur.execute(query)
liste =  cur.fetchall()
print(*liste,sep="\n")
db.close()
