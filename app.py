import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle


app = Flask(__name__)
model=pickle.load(open("model",'rb'))

@app.route('/')
def homee():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    values=[int(x) for x in request.form.values()]
    predicted_value=(model.predict([values]))
    
    
    return render_template("index.html", prediction_text=predicted_value )
    
    
    





if __name__ == "__main__":
    app.run(debug=True)

