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
    # return"<h1>APP FLASK IRIS</h1> \n <h2>Hola {}/h2>"
    return render_template('index.html')

@app.route('/user/<name>', methods=['GET'])
def user(name):
    return "<h1>APP FLASK IRIS </h1> \n <h2>Hola {}</h2>".format(name)



@app.route('/predict', methods=['POST'])  #es metodo post porq necsita recibir datos
def predict():
    # a =float(request.args.get('a',None))
    # b =float(request.args.get('b',None))
    # c =float(request.args.get('c',None))
    # d =float(request.args.get('d',None))
    #  PONEMOS FLOAT PORQ LOS PROTOCOLOS HTML, TIENEN JSON POR DETRAS Q LO ENVIAN COMO STRING AUNQ YO PONGA UN NUMERO

    # a =float(request.args.get('a'))
    # b =float(request.args.get('b'))
    # c =float(request.args.get('c'))
    # d =float(request.args.get('d'))
    # ESTA SEGUNDA OPCIÓN DARÍA UN ERROR: no numeric, asi que habria que convertir todo en float


    prediction = iris_model.predict([[a,b,c,d]])


    return 'la predicción es {}'.format(prediction)

if __name__ == '__main__':
    app.run(debug=True)