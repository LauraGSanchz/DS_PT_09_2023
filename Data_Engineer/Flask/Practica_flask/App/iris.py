# Crear un ML con los datos de iris

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, f1_score, accuracy_score, classification_report
import pickle
import os

os.chdir(os.path.dirname(__file__))

iris = load_iris()

print(iris.keys())
print(iris.target_names())

dict = {i: name for i, name in enumerate(iris.target_names)}


# df = iris['data']
# target = iris['target']

# X_train, X_test, y_train, y_test = train_test_split(df, target, test_size=0.2, random_state=42)

# knn = KNeighborsClassifier(n_neighbors=5)

# knn.fit(X_train, y_train)

# predictions_y_train = knn.predict(X_train)
# predictions_y_test = knn.predict(X_test)

# print(classification_report(y_train, predictions_y_train))
# print('-------'*200)
# print(knn.score(X_test,y_test))
# print('-------'*200)
# print(classification_report(y_test, predictions_y_test))

# with open ('iris_model.pkl', 'wb') as f:
#     pickle.dump(knn, f)


#INFERENCIA
    
model = pickle.load(open('iris_model.pkl', 'rb'))
muestra = [[5.1, 3.5, 1.4, 0.2]]

print(dict[iris_model.predict([muestra])[0]])




