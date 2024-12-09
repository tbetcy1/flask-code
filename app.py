# Import the Flask class from the flask module
from flask import Flask 
from utilities.testclass import *
import sys

# Create an instance of the Flask class
# '__name__' is a special variable in Python that represents the name of the current module.
app = Flask(__name__) 


@app.route("/hello/<name>")
def hello(name):
    ns = sayhello(name)
    return  (ns.sayfun(name))

@app.route('/health')
def health():
    return f"{sys.path}"

# Define a route for the root URL ('/')
# This means that when a user accesses 'http://<server-ip>/', this function will run.
@app.route('/')
def home():
    return "Hello, Flask!"  # This is the response sent back to the client (browser).

# Ensure the Flask app runs when the script is executed directly
if __name__ == '__main__':
    # Run the Flask app on localhost (127.0.0.1) and port 5000
    app.run(debug=True)