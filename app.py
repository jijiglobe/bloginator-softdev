from flask import Flask, render_template, session

@app.route("")
@app.route("/home")
def home():


@app.route("/login")
def login():


@app.route("/profile") #list of all user posts + most recent comments
def profile():


@app.route("/posts") #shows all posts, title + most recent comment
def posts():


@app.route("/posts/<pid>") #for individual posts
def onepost():
    #comments

