import os
from flask import Flask, render_template, redirect, request, url_for
import pymysql

username = os.getenv('C9_USER')

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='RecipeBook')

app = Flask (__name__)
#api = Api(app)

@app.route('/')
def getLanding():
    cursor = connection.cursor()
    sql = "SELECT * from USER"
    cursor.execute(sql)
    result = cursor.fetchall()
    return render_template("landing_page.html", result=result)

@app.route('/login')
def getLogin():
    return render_template("login.html")
    
@app.route('/recipes')
def getRecipes():
    return render_template("recipes.html")
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)


                            
