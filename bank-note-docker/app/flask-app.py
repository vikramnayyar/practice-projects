from flask import Flask, request
# import Flask
import pandas as pd
import numpy as np
import pickle
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

pickle_in=open("model/model.pkl", "rb")
model = pickle.load(pickle_in)

@app.route('/')               # home page
def welcome():
    return "Hare Krishna, type http://192.168.1.5:8000/apidocs/ in browser"


@app.route('/predict')        # performs prediction
def predict_notes():

    """This app is developed to detect fake notes.
        Use the following form to get started!
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses: 
        200:
            description: the output values

    """
    variance = request.args.get("variance")
    skewness = request.args.get("skewness")
    curtosis = request.args.get("curtosis")
    entropy = request.args.get("entropy")
    prediction = model.predict([[variance, skewness, curtosis, entropy]])
    return "The predicted value is "+ str(prediction)
    # http://127.0.0.1:5000/predict?variance=2&skewness=3&curtosis=2&entropy=1


@app.route('/predict_file', methods = ["POST"])        # performs prediction
def predict_notes_usingcsv():
    """This app is developed to detect fake notes.
        Use the following form to get started!
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """

    df_test = pd.read_csv(request.files.get("file"))
    prediction = model.predict(df_test.head())
    
    return str(list(prediction))
    # return "The predicted value for csv "+ str(list(prediction))
    # http://127.0.0.1:5000/predict?variance=2&skewness=3&curtosis=2&entropy=1


if __name__ =="__main__":
    app.run(host='0.0.0.0', port=8000)