'''
Created on 16 Mar 2021
update
@author: shane
'''
import pymysql


db = pymysql.connect(host='localhost', user='root', db='python', password='python', charset='utf8')
curs = db.cursor()

sql = '''
update sample set column01 = 'cc', column02 = 'bb'
where column01 = 'aa';
'''

curs.execute(sql)

sql = "select * from sample";
curs.execute(sql)

rows = curs.fetchall()
print(rows)

db.commit()
db.close()
