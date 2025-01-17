from flask import Flask  
from flask_sqlalchemy import SQLAlchemy           

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'secret-key'        #secret key is needed when you use csrf. the secret key (lower-case) can be any word for now
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from routes import * 

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
    
    
    """
    Since we would be using a lot of '@app.route', along with a lot of other functionalities in our app.py file, its not a good idea to keep all of this code in a single file.
    You can do this but not a good way to go about keeping everything in one place as itll be hard for you to navigate through your code
    """