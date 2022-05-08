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

books.BooksDatabase().create_db_table()
costumers.Costumers().create_db_table()
loans.Loans().create_db_table()

#home page and bout

@app.route('/')
def hello():
    return render_template('home.html')
 
#book class related pages

#view all the books

@app.route('/viewbooks')
def viewbooks():
    return render_template('viewbooks.html',books = books.BooksDatabase().print_all_data())

#add a book to the table

@app.route('/addbook', methods = ["POST", "GET"])
def addbook():
    if request.method == "POST":
        books.BooksDatabase().addBook(request.form["nm"],request.form["auth"],request.form["yr"],request.form["typ"])
        return redirect(url_for("viewbooks"))
    else:
        return render_template('addbook.html')

#remove a book from the table

@app.route('/removebook', methods = ["GET","POST"])
def removebook():
    if request.method == "POST":
        books.BooksDatabase().removeBook(request.form["nm"])
        return(redirect(url_for("viewbooks")))
    else:
        return render_template("removebook.html")



#costumer class related pages---

#view all the costumers

@app.route('/viewcostumers')
def viewcostumers():
    return render_template('viewcostumers.html',costumers = costumers.Costumers().print_all_data())

# add a costumer to the table

@app.route('/addcostumer', methods = ["GET","POST"])
def addcostumer():
    if request.method == "POST":
        costumers.Costumers().addCostumer(request.form["nm"],request.form["city"],request.form["age"])
        return redirect(url_for("viewcostumers"))
    else:
        return render_template('addcostumer.html')

#find a costumer by name

@app.route('/findcostumer',methods = ["GET","POST"])
def findcostumer():
    if request.method == "POST":
        return render_template("findcostumer.html", costumers =costumers.Costumers().findCostumer(request.form["nm"]) )
    else:
        return render_template('findcostumer.html')

#remove a costumer from the table

@app.route('/removecostumer',methods = ["GET","POST"])
def removecostumer():
    if request.method == "POST":
        costumers.Costumers().removeCostumer(request.form["nm"])
        return(redirect(url_for("viewcostumers")))
    else:
        return render_template("removecostumer.html")



#loans related pages ---

#view all loans

@app.route('/viewloans')
def viewloans():
    return render_template('viewloans.html',loans = loans.Loans().print_all_data())

#add a loan to the table

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


#return a loan to the table

@app.route('/returnbook')
def returnbook():
    return 'Hello, World!'

@app.route('/viewlateloans')
def viewlateloans():
    return 'Hello, World!'

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True, port = 9000)
