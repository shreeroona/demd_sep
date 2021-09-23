from flask import Flask, request
import numpy as np
import pandas as pd
import pickle
from flasgger import Swagger
import sklearn


app = Flask(__name__)
Swagger(app)

pickled_model = open("Pickle_file_iris.pkl","rb")
classifier = pickle.load(pickled_model)

@app.route("/")
def home():
    return "Welcome to Iris Classifier"
@app.route('/predict')
def predict_flower():

    """ Predict the IRIS flower category
    ---
    parameters:
     - name: Sepal_width
       in: query
       type: number
       required: true
     - name: Sepal_length
       in: query
       type: number
       required: true
     - name: Petal_width
       in: query
       type: number
       required: true 
     - name: Petal_length
       in: query
       type: number
       required: true             
    responses:
       200:
            description: Result is

    """

    sw = request.args.get("Sepal_width")
    sl = request.args.get("Sepal_length")
    pw = request.args.get("Petal_width")
    pl = request.args.get("Petal_length")

    result = classifier.predict([[sw,sl,pw,pl]])
    return f"The prediction is {result}"
if __name__ == "__main__":
    app.run()
