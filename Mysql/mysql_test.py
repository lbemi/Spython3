# import pymysql
# db = pymysql.connect('192.168.0.184','Miebao','Miebao_0805','miebao_test')
# tee = db.cursor()
# cursor.execute('select * from miebao_admin')
# data = cursor.fetchone()
# print(data)
#
# db.close()


import pymysql
ss = pymysql.connect('192.168.0.184','Miebao','Miebao_0805','miebao_test')
test = ss.cursor()
try:
    sql = "delete from miebao_admin where mobile='15926885095'"
    test.execute(sql)
    ss.commit()
except:
    print('----------')
    ss.rollback()
    print('tetssgvdfsjagdf')
ss.close()