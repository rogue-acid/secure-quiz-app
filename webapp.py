from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json



app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
     
@app.route('/p1')
def question1():
    return render_template('page1.html')
    
@app.route('/p2')
def question2():
    return render_template('page2.html')
    
@app.route('/p3')
def question3():
    return render_template('page3.html')
    
@app.route('/p4')
def question4():
    return render_template('page4.html')
    
@app.route('/p5')
def question5():
    return render_template('page5.html')
    
@app.route('/p6')
def question6():
    return render_template('page6.html')
    

    

if __name__ == '__main__':
    app.run(debug=True) # change to False when running in production
