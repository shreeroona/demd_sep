
# Importing the    required package
from flask import Flask, render_template, request
#import flasgger
from flasgger import Swagger
import os

# Defining the name (will fetch from the actual file name)
app = Flask(__name__)
Swagger(app)

# Defingin the path or url attahced after the local ip
@app.route('/', methods=['GET'])
# Function that would be executed when the above URL is hit.
def welcome():
    return render_template("index.html")

# Defining second url
@app.route('/name/<your_name>')
# Function that should be executed when this URL is hit
def names(your_name):
    return f"Welcome to Praxis {your_name}"
# Defining using Swagger
@app.route('/checking_req',methods=['POST','GET'])
def get_req_parameters():
    """ Practicing Swagger
    ---
    parameters:
     - name: Student_name
       in: query
       type: string
       required: true
     - name: roll_no
       in: query
       type: number
       required: true
    responses:
       200:
            description: Result is

    """
    name = request.args.get("Student_name")
    roll_no = request.args.get("roll_no")
    return f"Student name is {name} and roll no is {roll_no} in Praxis"


if __name__ == "__main__":
    # Use debug only when required. With debug no need to stop the server every time.
    #port = int(os.environ.get('PORT',5000))
    app.run(host="0.0.0.0",port=5000)
    # Use Cntl+C to stop the server