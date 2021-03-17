'''
Created on 16 Mar 2021
insert
@author: shane
'''
import pymysql


db = pymysql.connect(host='localhost', user='root', db='python', password='python', charset='utf8')
curs = db.cursor()

sql = '''insert into sample (column01, column02, column03) values ('aa','bb','cc')
'''

curs.execute(sql)

sql = "select * from sample";
curs.execute(sql)

rows = curs.fetchall()
print(rows)

db.commit()
db.close()
