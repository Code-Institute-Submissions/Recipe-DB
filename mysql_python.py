import os
from flask import Flask, render_template, redirect, request, url_for
import pymysql
import pymysql.cursors

username = os.getenv('C9_USER')

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='RecipeBook',
                            cursorclass=pymysql.cursors.DictCursor)

app = Flask (__name__)
#api = Api(app)

@app.route('/')
def getLanding():
    cursor = connection.cursor()
    sql = "SELECT * from USER"
    cursor.execute(sql)
    result = cursor.fetchall()
    return render_template("landing_page.html", result=result)

@app.route('/recipes')
def getRecipes():
    cursor = connection.cursor()
    sql = "SELECT * from RECIPE"
    cursor.execute(sql)
    recipeResult = cursor.fetchall()
    return render_template("recipes.html", recipeResult=recipeResult)

@app.route('/addrecipe')
def addRecipe():
    return render_template("addrecipe.html")
  
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)


                            
