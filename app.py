from flask import Flask, render_template               

app = Flask(__name__)         
@app.route('/')               # this is defining two routes that map to the same function (index()). if a user visits the root URL (/) or /index, the same content will be displayed.
@app.route('/index')
def index():                  
    return render_template('index.html', current_title='Custom Title') # allows us to change out html dynamically. 

if __name__ == '__main__':
    app.run(debug=True)        