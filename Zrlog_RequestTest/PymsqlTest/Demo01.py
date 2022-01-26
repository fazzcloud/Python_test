import pymysql
#创建数据库对象
db = pymysql.connect(
    #设置数据库主机地址
    host = "106.14.135.177",
    #用户名
    user = "root",
    #密码
    password = "lj19950104",
    #数据库名称
    database = "zrlog",
    #字符集
    charset = "utf8",
    #端口号
    port = 3306
)

#创建sql游标对象，游标对象主要用来执行sql语句
cursor = db.cursor(pymysql.cursors.DictCursor)

#要执行的sql语句
sql = "select * from log"

#使用excute方法执行sql
cursor.execute(sql)
#使用fetchone方法一次性获取一条数据
res = cursor.fetchone()
cursor.execute(sql)
res2 = cursor.fetchmany(2)
cursor.execute(sql)
res3 = cursor.fetchall()
print(res)
print(res2)
print(res3)
#关闭游标对象
cursor.close()
#关闭database对象
db.close()