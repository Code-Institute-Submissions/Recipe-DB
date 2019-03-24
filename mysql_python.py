import os
import pymysql
from flask import Flask

app = Flask (__name__)

@app.route('/')
def hello():
    return "hello world - innit"
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)

username = os.getenv('C9_USER')

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='RecipeBook')
                            
try:
    with connection.cursor() as cursor:
        sql = "SELECT user_name FROM USER;"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)

finally:
    connection.close()
    