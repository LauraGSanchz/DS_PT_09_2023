# 1. Importación de biblioteca
import os
import uvicorn #rederizar
from fastapi import FastAPI #para crear la aplicación
from Model import IrisModel, IrisSpecies #del Model.py


os.chdir(os.path.dirname(__file__))
# 2. Crear la aplicación y los objetos del modelo

app = FastAPI()
model = IrisModel()

# 3. Exponer la funcionalidad de predicción, realizar una predicción a partir de los datos JSON pasados
#    y devolver la especie de flor predicha con la confianza

@app.post('/predict') #es metodo post porq necsita recibir datos y es una ruta que se llama predict
def predict_species(iris: IrisSpecies):
    data = iris.dict()
    prediction, probability = model.predict_species(
        data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']  #estos nombrees tienen que ser los mismos que en Model.py 
    )
    return {
        'prediction': prediction,
        'probability': probability
    }

# 4. Ejecutar la API con uvicorn
#    Se ejecutará en http://127.0.0.1:8000

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)