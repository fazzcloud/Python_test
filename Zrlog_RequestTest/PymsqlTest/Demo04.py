import pymysql
db = pymysql.connect(
    host="106.14.135.177",
    user="root",
    password="lj19950104",
    port=3306,
    database="zrlog",
    charset="utf8"
)

cursor = db.cursor()

sql = "delete from log where logId = 7"

try:
    cursor.execute(sql)
    db.commit()
    print("语句执行完毕！")
except Exception as e:
    db.rollback()
    print("语句执行异常，数据回滚")

cursor.close()
db.close()