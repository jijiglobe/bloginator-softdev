from flask import Flask, render_template, session

@app.route("")
@app.route("/home")
def home():
    pass

@app.route("/login")
def login():
    pass

@app.route("/profile") #list of all user posts + most recent comments
def profile():
    pass

@app.route("/posts") #shows all posts, title + most recent comment
def posts():
    pass

@app.route("/posts/<pid>") #for individual posts
def onepost():
    #comments
    pass
