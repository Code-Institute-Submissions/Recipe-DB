import os
import pymysql
from flask import Flask

app = Flask (__name__)

@app.route('/')
def hello():
    return "hello world - innit"
    
@app.route('/test')
def testSuccess():
    return "test is successful Brah!"

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)

