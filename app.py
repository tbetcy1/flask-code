# Import the Flask class from the flask module
from flask import Flask 
import os
from utilities.testclass import *
from utilities.HSM import *
from utilities.Currencyvaule import *
from flask import request
import sys

# Create an instance of the Flask class
# '__name__' is a special variable in Python that represents the name of the current module.
app = Flask(__name__) 


@app.route("/hello/<name>")
def hello(name):
    ns = sayhello(name)
    return  (ns.sayfun(name))

# @app.route('/health')
# def health():
#     return f"{sys.path}"

# Define a route for the root URL ('/')
# This means that when a user accesses 'http://<server-ip>/', this function will run.
@app.route('/')
def home():
    return "Hello, Flask!"  # This is the response sent back to the client (browser).
@app.route('/HSM/<name>')
def hsmtest(name):
    hsmobj = hsm()
    return hsmobj.print(name)

#currency exchange 
@app.route("/forex/<fromcur>/<tocur>")
def weather(fromcur,tocur):
    wth = forex_rate()
    return wth.return_data(fromcur,tocur)

#post method Demo
@app.route("/process",methods=["POST"])
def process():
    try:
        data = request.get_json()
        if not data:
            return({"error": "No data provided"}),400
        name = data["name"]
        age = data["age"]
        if not age or not name:
            return({"error": "Age or name attribute is missing"}), 400
        if age >= 18:
            message = {
                "name" : name,
                "is_adult": "Is an adult"
            }
        else:
             message = {
                "name" : name,
                "is_adult": "Is not an adult"
            }
        return message
    except Exception as e:
        return({"error": str(e)}),400



# Ensure the Flask app runs when the script is executed directly
if __name__ == '__main__':
    # Run the Flask app on localhost (127.0.0.1) and port 5000
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)