from app import app #from the file named app, import the instance app
from flask import render_template

import forms

@app.route('/')               
@app.route('/index')
def index():                  
    return render_template('index.html') 

@app.route('/about', methods=['GET', 'POST'])
def about():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print('Submitted title', form.title.data) #accessing info on the forms
        return render_template('about.html', form=form, title=form.title.data) #passing on multiple things to our template
    return render_template('about.html', form=form)