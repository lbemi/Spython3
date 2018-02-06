import pymysql
con = pymysql.connect(host='127.0.0.1',user='root', passwd = 'admin', db = 'mypydb')
# con.query("create database mypydb")
# con.query("create table mypydb.mytb(title ChAR(20) NOT NULL ,keywd CHAR (30))")
# con.query("insert into mytb(title, keywd, name) VALUES ('ccc','eee','你大爷')")
# con.query("alter table mytb add COLUMN name VARCHAR (20)")