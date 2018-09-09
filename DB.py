import pymysql





conn = pymysql.connect(host="localhost" , port=3306,user='root' , passwd='root', db='adv' )

cursor=conn.cursor()

cursor.execute("SELECT VERSION ()")

data = cursor.fetchone()
print("Database v %s" % data)

conn.close()


