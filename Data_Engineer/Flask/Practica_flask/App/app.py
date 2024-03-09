from flask import Flask, jsonify, render_template
from flask import Flask, request
import pickle
import os

os.chdir(os.path.dirname(__file__))
print(os.getcwd())

model = pickle.load(open('iris_model.pkl', 'rb'))
print(model)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return"<h1>APP FLASK IRIS</h1>"

@app.route('/predict', methods=['POST'])  #es metodo post porq necsita recibir datos
def predict():

    return 

if __name__ == '__main__':
    app.run(debug=True)