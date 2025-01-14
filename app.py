from flask import Flask                

app = Flask(__name__)         # ' Flask(__name__) ' creates an instance of the Flask class. __name__ is a special variable in Python that contains the name of the current module. Flask uses this to locate resources like templates and static files.
@app.route('/')               # route decor
def hello():                  # defining a function
    return "Hello, world!"

if __name__ == '__main__':
    app.run(debug=True)        # starts the Flask development server to serve the application. debug=True enables debug mode: Automatically reloads the server when you make changes to the code and Displays detailed error messages in the browser if an error occurs.