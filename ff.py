from flask import Flask,render_template,url_for
from NewsFeedApp import *


app=Flask(__name__)
ns=NewsFeedApp.shownews()

@app.route("/")
@app.route("/home")
def homepage():
    return render_template('home.html',ns=ns)
    #return("".join(ns))
    
@app.route("/sports")
def sports():
    sports=NewsFeedApp.shownewsCat('sports')
    return  render_template('sports.html',sports=sports)
   
@app.route("/tech")
def tech():
    tech=NewsFeedApp.shownewsCat('technology')
    return  render_template('tech.html',tech=tech)
    
@app.route("/business")
def business():
    business=NewsFeedApp.shownewsCat('business')
    return  render_template('business.html',business=business)
    
@app.route("/science")
def science():
    science=NewsFeedApp.shownewsCat('science')
    return  render_template('science.html',science=science)
   
if __name__=="__main__":
    app.run(debug=True)

