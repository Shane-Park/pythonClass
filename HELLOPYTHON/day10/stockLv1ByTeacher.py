'''
Created on 22 Mar 2021

@author: shane
'''
import pymysql

def getAllPrices():
    zs = []
    conn = pymysql.connect(host='localhost', user='root', db='_stock_old', password='python', charset='utf8')
    curs = conn.cursor()
    sql = '''
        select 
            s000020,
            s000040,
            s000050
        from stock_sync_0121
        limit 10
    '''
    
    curs.execute(sql)
    rows = curs.fetchall()
    
    cnt10 = len(rows)
    cnt3 = len(rows[0])
    
    for i3 in range(cnt3):
        line = []
        first_price = rows[0][i3]
        for j10 in range(cnt10):
            line.append(rows[j10][i3])
        zs.append(line)
    
    conn.close()
    return zs

if __name__ == '__main__':
    arr = getAllPrices()
    print(arr)