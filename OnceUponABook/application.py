import os

from flask import Flask, render_template, request, session, url_for, flash, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretsecret!'

engine = create_engine("postgres://fvqnuioi:yVBAZf8hgrr0gmkfxyaOjWB232ADa-oD@otto.db.elephantsql.com:5432/fvqnuioi")
db = scoped_session(sessionmaker(bind=engine))

@app.route('/', methods = ['POST', 'GET'])
def main():
    if 'user' in session:
        return render_template("index.html")
    else:
        return render_template("registrar.html")

@app.route("/registrar", methods = ['POST', 'GET'] )
def registrar():
    usuario = request.form.get("us")
    email = request.form.get("email")
    passw = request.form.get("pw")
    passww = request.form.get("pw2")
    if(passw == passww):
        db.execute("INSERT INTO users (usser, email, passw) VALUES (:usser, :email, :passw)", {"usser": usuario, "email":email, "passw": passww})
        db.commit();
        return redirect(url_for('login'))
    else:
        return render_template("registrar.html")

@app.route('/login', methods = ['POST', 'GET'])
def login():
    usuario = request.form.get("us")
    passw = request.form.get("pw")
    usuarioON = db.execute("SELECT usser, email, passw FROM users WHERE usser = :usser",{"usser": usuario}).fetchone()
    if (usuarioON != None):
        session['user'] = usuarioON[0]
        return render_template("index.html")
    else:
        flash("User not found")
        return render_template("login.html")

@app.route("/search", methods= ['POST', 'GET'])
def search():
    if(request.method == ['GET']):
        if 'user' in session:
            return render_template("search.html")
        else:
            return render_template("registrar.html")
    else:
        sbook = request.form.get("search")
        sbook = str(sbook).lower()
        books = db.execute("SELECT * FROM books WHERE isbn LIKE '%' || :isbn || '%' OR LOWER(title) LIKE '%' || :title || '%' OR LOWER(author) LIKE '%' || :author || '%'", {"isbn": sbook, "title": sbook, "author": sbook}).fetchall()
        db.close()
        return render_template("search.html", books=books, message=sbook)

@app.route("/book/<book_isbn>", methods=['POST', 'GET'])
def book(book_isbn):
    book = db.execute("SELECT isbn, title, author, year FROM books WHERE isbn = :isbn",{"isbn": book_isbn}).fetchone()
    reviews = db.execute("SELECT * FROM reviews WHERE isbn = :isbn",{"isbn": book_isbn}).fetchall()
    rev_isbn = book[0]
    rev_title = book[1]
    rev_usser = session['user']
    rev_calif = request.form.get("star")
    rev = request.form.get("makereview")
    if(rev_calif and rev):
        rev = db.execute("INSERT INTO reviews (isbn, title, usser, review, calif) VALUES (:isbn, :title, :usser, :review, :calif)", {"isbn": rev_isbn, "title": rev_title, "usser": rev_usser, "review": rev, "calif": rev_calif })
        db.commit()
        return render_template("book.html", book=book, reviews=reviews)
    return render_template("book.html", book=book, reviews=reviews)

@app.route("/reviews", methods= ['POST', 'GET'])
def reviews():
    allreviews = db.execute("SELECT * FROM reviews").fetchall()
    return render_template("reviews.html", reviews=allreviews)

@app.route("/allbooks", methods= ['POST', 'GET'])
def allbooks():
    allbooks = db.execute("SELECT * FROM books").fetchall()
    return render_template("allbooks.html", books=allbooks)

@app.route("/onebook/<string:bo_isbn>", methods= ['POST', 'GET'])
def onebook(bo_isbn):
    onebook = db.execute("SELECT * FROM books WHERE isbn = :isbn",{"isbn": bo_isbn}).fetchone()
    onereviews = db.execute("SELECT * FROM reviews WHERE isbn = :isbn",{"isbn": bo_isbn}).fetchall()
    rev_isbn = onebook[0]
    rev_title = onebook[1]
    rev_usser = session['user']
    rev_calif = request.form.get("star")
    rev = request.form.get("makereview")
    if(rev_calif and rev):
        revi = db.execute("INSERT INTO reviews (isbn, title, usser, review, calif) VALUES (:isbn, :title, :usser, :review, :calif)", {"isbn": rev_isbn, "title": rev_title, "usser": rev_usser, "review": rev, "calif": rev_calif })
        db.commit()
        return render_template("onebook.html", book=book, reviews=onereviews)
    return render_template("onebook.html", book=onebook, reviews=onereviews)

@app.route('/close')
def close():
    session.pop('user')
    return redirect('/')

#if __name__ = '__main__'
