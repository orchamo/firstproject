from flask import Flask, json, request ,render_template, url_for, redirect, session,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Column,Integer,String
from datetime import datetime
import books
import costumers
import loans

#create a Flask instance
app = Flask(__name__)
app.secret_key= "banana"
#add database

app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///costumers.db'
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///loans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#initialize db
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return render_template('home.html')
 
@app.route('/viewbooks')
def viewbooks():
    return render_template('viewbooks.html',books = books.BooksDatabase().print_all_data())

@app.route('/addbook', methods = ["POST", "GET"])
def addbook():
    if request.method == "POST":
        books.BooksDatabase().addBook(request.form["nm"],request.form["auth"],request.form["yr"],request.form["typ"])
        return redirect(url_for("viewbooks"))
    else:
        return render_template('addbook.html')


@app.route('/removebook', methods = ["GET","POST"])
def removebook():
    if request.method == "POST":
        books.BooksDatabase().removeBook(request.form["nm"])
        return(redirect(url_for("viewbooks")))
    else:
        return render_template("removebook.html")

@app.route('/viewcostumers')
def viewcostumers():
    return render_template('viewcostumers.html',costumers = costumers.Costumers().print_all_data())

@app.route('/addcostumer', methods = ["GET","POST"])
def addcostumer():
    if request.method == "POST":
        costumers.Costumers().addCostumer(request.form["nm"],request.form["city"],request.form["age"])
        return redirect(url_for("viewcostumers"))
    else:
        return render_template('addcostumer.html')

@app.route('/findcostumer',methods = ["GET","POST"])
def findcostumer():
    if request.method == "POST":
        return render_template("findcostumer.html", costumers =costumers.Costumers().findCostumer(request.form["nm"]) )
    else:
        return render_template('findcostumer.html')

@app.route('/removecostumer',methods = ["GET","POST"])
def removecostumer():
    if request.method == "POST":
        costumers.Costumers().removeCostumer(request.form["nm"])
        return(redirect(url_for("removecostumer")))
    else:
        return render_template("removecostumer.html")

@app.route('/viewloans')
def viewloans():
    return 'Hello, World!'

@app.route('/loanbook', methods = ["GET","POST"])
def loanbook():
    if request.method == "POST":
        # try:
            if books.BooksDatabase().findBookStatus(request.form["bnm"]) == "available":
                # books.BooksDatabase().updateBookStatus(request.form["bnm"], 'Not Available')
                return redirect(url_for("viewbooks"))
        # except Exception as e:
        #         print(e)
        #         print ("book not found")
    else:
        return render_template("loanbook.html")



@app.route('/returnbook')
def returnbook():
    return 'Hello, World!'

@app.route('/viewlateloans')
def viewlateloans():
    return 'Hello, World!'

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True, port = 9000)









# def main():


#     print("a - add new book")
#     print("b - add new costumer")
#     print("c - loan a book")
#     print("d - return a book")
#     print("e - display all books")
#     print("f - display all customers")
#     print("g - display all loans")
#     print("h - display all late loans")
#     print("i - find book by name")
#     print("i - find customer by name")
#     print("i - remove book")
#     print("i - remove customer")








# if __name__=="__main__":
#     main()