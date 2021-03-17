'''
Created on 16 Mar 2021
delete
@author: shane
'''
import pymysql


db = pymysql.connect(host='localhost', user='root', db='python', password='python', charset='utf8')
curs = db.cursor()

sql = '''
delete from sample 
where column01 = 'cc'
'''

curs.execute(sql)

sql = "select * from sample";
curs.execute(sql)

rows = curs.fetchall()
print(rows)

db.commit()
db.close()
