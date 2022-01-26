import pymysql

db = pymysql.connect(
    # 设置数据库主机地址
    host="106.14.135.177",
    # 用户名
    user="root",
    # 密码
    password="lj19950104",
    # 数据库名称
    database="zrlog",
    # 字符集
    charset="utf8",
    # 端口号
    port=3306
)
#建立游标对象，游标是数据库的游标，所以是db类型
cusor = db.cursor()
#插入数据的
sql = "insert into log set logId=5,title='你好，希望',alias='你好，希望',content='你好，希望'"
cusor.execute(sql)

#提交数据
db.commit()
#关闭
cusor.close()
db.close()