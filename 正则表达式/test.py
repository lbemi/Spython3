import pymysql
db = pymysql.connect('192.168.0.184','Miebao','Miebao_0805','miebao_test')
tee = db.cursor()
cursor.execute('select * from miebao_admin')
data = cursor.fetchone()
print(data)

db.close()


import pymysql
ss = pymysql.connect('192.168.0.184','Miebao','Miebao_0805','miebao_test')
test = ss.cursor()
test.execute('select version')
data = test.fetchone()
print(data)