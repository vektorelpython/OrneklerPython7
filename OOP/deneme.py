import sqlite3


db = sqlite3.connect(r"D:\İbrahim EDİZ\OrnekDB\chinook.db")
cursor = db.cursor()
sorgu = """SELECT AlbumId from albums  
where ArtistId IN 
(SELECT ArtistId from artists 
where name LIKE 'A%')
ORDER BY Title DESC,ArtistId"""
cursor.execute(sorgu)

print(cursor.fetchall())