#from flask_pymongo import pymongo
import pymongo
from flask import Flask,request,render_template

app = Flask(__name__)

try:
    print("Connecting to database...")
    client = pymongo.MongoClient(
        "mongodb+srv://lzyrila:woaideni1996@rilawebdb.lc25k.mongodb.net/<dbname>?retryWrites=true&w=majority")
    db = client.wish_list
    collection = db.wish_list0
    print("Success! connected to db")
except Exception as e:
    print("could not connect to db")
    print(e)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/answerToMiss.html')
def answerToMiss():
    return render_template("answerToMiss.html")

@app.route('/BirthdayCake.html')
def BirthdayCake():
    return render_template("BirthdayCake.html")

# @app.route('/category-grid.html')
# def category():
#     return render_template("category-grid.html")

# @app.route('/category-list.html')
# def category_list():
#     return render_template("category-list.html")

@app.route('/Journey.html')
def journey():
    return render_template("Journey.html")

@app.route('/our_stories.html')
def our_stories():
    return render_template("our_stories.html")

@app.route('/wish-list.html')
def wish():
    # users = collection.find()
    # for user in users:
    #     print("test.....:",user)
    return render_template("wish-list.html")

# @app.route('/single-post.html')
# def single():
#     return render_template("single-post.html")

# @app.route('/index-grid-fullwidth.html')
# def index_grid():
#     return render_template("index-grid-fullwidth.html")

@app.route('/study-hard.html')
def study():
    return render_template("study-hard.html")

# @app.route('/single-post-full-width.html')
# def single_fullwidth():
#     return render_template("single-post-full-width.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)
