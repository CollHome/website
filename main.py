#!/usr/bin/env python3

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, redirect, url_for, flash

import register
db_url = "sqlite:///collhome.db"
engine = create_engine(db_url, convert_unicode=True)
db = scoped_session(sessionmaker(autocommit=True, autoflush=False, bind=engine))
register.Base.query = db.query_property()
register.Base.metadata.create_all(bind=engine, checkfirst=True)

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route("/")
def home():
    return render_template("home.html", rows=db.query(register.Chapter).all())

@app.route("/register/", methods=["GET", "POST"])
def registerform():
    form = register.Register()
    if form.validate_on_submit():
        fd = form.data
        del fd['submit']
        del fd['csrf_token']
        db.add(register.Chapter(**fd))
        flash("Added "+form.university.data+" Chapter")
        return redirect(url_for("home"))
    return render_template("register.html", form=form)


if __name__ == "__main__":
    app.run()
