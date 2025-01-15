from flask import Flask, render_template               

app = Flask(__name__)         
@app.route('/')               
@app.route('/index')
def index():                  
    return render_template('index.html') 

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)        
    
    
    """
    Whats happening:
    
    Now when we run app.py, it will run the index route. Inside the index.html, it will essentially load the base.html file. 
    Inside this base.html file is the body text , the larger chunk/template of code. 
    So itll display this body of code, and whatever the code remaining inside the index.html.
    the larger chunk will display first as this is how it is strunctured inside the index.html fil.
    Next, the about page will be rendered as this is the next (@app.route('/about')). 
    Similarly, the base.html will be loaded and then followed by whatever is left inside the about.html file.
    In the base.html file, at the bottom it has:
    {%block main%}
    {%endblock main%}
    On the index.html and about.html files, whatre is between the block main and endblock, is what will display on each individual page alone with the code already on the base.html
    """