from flask import Flask, request, render_template
import pickle
import os

os.chdir(os.path.dirname(__file__))
print(os.getcwd())

model = pickle.load(open('catbmodel.pkl', 'rb'))
dic_target = {0: 'Murió', 1: 'Sobrevivió'}
print(model)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/user/<name>', methods=['GET'])
def user(name):
    return render_template('datos.html', name=name)


@app.route('/predict_form')
def prediction_form():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    is_male = int(data.get('is_male'))
    Age = float(data.get('Age'))
    Fare = float(data.get('Fare'))
    Acompaniantes = int(data.get('Acompaniantes'))
    Pclass_1 = float(data.get('Pclass_1'))
    Pclass_2 = float(data.get('Pclass_2'))
    Pclass_3 = float(data.get('Pclass_3'))
    Embarked_C = float(data.get('Embarked_C'))
    Embarked_Q = float(data.get('Embarked_Q'))
    Embarked_S = float(data.get('Embarked_S'))

    # Realizar la predicción con los datos recibidos
    prediction = model.predict([[is_male, Age, Fare, Acompaniantes, Pclass_1, Pclass_2, Pclass_3, Embarked_C, Embarked_Q, Embarked_S]])

    # Obtener la etiqueta correspondiente a la predicción
    predicted_label = dic_target[prediction[0]]
    
    # Devolver la predicción
    return 'La predicción es {}'.format(predicted_label)


# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     is_male = int(data.get('is_male'))
#     Age = float(data.get('Age'))
#     Fare = float(data.get('Fare'))
#     Acompaniantes = int(data.get('Acompaniantes'))
#     Pclass_1 = float(data.get('Pclass_1'))
#     Pclass_2 = float(data.get('Pclass_2'))
#     Pclass_3= float(data.get('Pclass_3'))
#     Embarked_C = float(data.get('Embarked_C'))
#     Embarked_Q = float(data.get('Embarked_Q'))
#     Embarked_S = float(data.get('Embarked_S'))  

#     prediction = model.predict([[is_male, Age, Fare,Acompaniantes, Pclass_1, Pclass_2, Pclass_3,Embarked_C, Embarked_Q, Embarked_S]])
    
#     mensaje = print(dic_target[prediction[0]])
#     return 'La predicción es {}'.format(mensaje)


if __name__ == '__main__':
    app.run(debug=True, port=5000)