import os
import pymysql

username = os.getenv('C9_USER')

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='RecipeBook')
                            
try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM RECIPE;"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)

finally:
    connection.close()
    