import pymysql
db = pymysql.connect(
    host="106.14.135.177",
    user="root",
    password="lj19950104",
    database="zrlog",
    charset="utf8",
    port=3306
)
cursor =db.cursor()
sql = "insert into log set logId=7,title='你好，中国',alias='你好，中国',content='你好，中国'"
sql2 = "insert into log set logId=6,title='你好，未来',alias='你好，未来',content='你好，未来'"
#加入异常机制
try:
    cursor.execute(sql)
    cursor.execute(sql2)
    db.commit()
    print("语句执行完毕！")
except Exception as e:
    '''
    若sql执行异常，则结果统一回滚
    就算其中一条语句执行成功，但只另一条语句执行异常，结果依旧会统一回滚，保证数据的正确性和完整性
    '''
    db.rollback()
    print("语句执行异常，数据回滚")

#关闭
cursor.close()
db.close()