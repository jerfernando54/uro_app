import numpy as np
import pandas as pd

import joblib
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split 

from prediction.models import BladderCancerPrediction
from constants import constants

def trainPredictModelBladderCancer(patient, methodID, is_trainig = False):
  mapeo_columnas = {
    'dm': {'Sí':1, 'No':0},
    'hta': {'Sí': 1, 'No': 0},
    'hereda': {'Sí':1, 'No':0},
    'exitus': {'No': 0,'Sí':1},
    'primario': {'Sí': 1, 'No': 0},
    'sexo': {'Varón':1, 'Varon': 1, 'Mujer': 0},
    'recidivante': {'Sí': 1, 'No': 0},
    'expoprofesional':{'Sí':1, 'No':0},
    'acarsinoinsitu': {'Sí': 1, 'No': 0},
    'evoldesfavorable': {'NO': 0,'SI':1, 'No': 0, 'Sí': 1, 'Si':1},
    'fhistoatipicas': {'Sí': 1, 'No': 0},
    'permiacionvascular': {'Sí': 1, 'No': 0},
    'carcinomaUrotelial': {'Sí': 1, 'No': 0},
    'gradotumoral': {'G1': 0, 'G2': 1, 'G3': 2},
    'tamtumoral': {'< 2cm': 0,'< 2 cm': 0, '2-5cm': 1, '2-5 cm': 1, '> 5cm': 2, '> 5 cm': 2},
    'numtumores': {'+5': 6},
    'aspectotumoral': {'Papilar': 0, 'Mixto': 1, 'Sólido': 2, 'Solido': 2},
    'tac':{'No infiltrante': 0, 'Dudoso': 1, 'Infiltrante': 2},
    'obesidad': {'NC': 0, 'IMC < 25': 1, 'IMC 25-30': 2, 'IMC > 30': 3},
    'estadotumoralclinico':{'Ta': 1, 'T1': 2, 'T2': 3, 'T3': 4, 'T4': 5},
    'clinica':{'Asintomático': 0, 'Asintomatico': 0, 'Hematuria': 1, 'Síndrome miccional': 2},
    'progresiva':{'No': 0,'Estadio (T)':1, 'Ganglios (N)':2, 'Metástasis (M)':3},
    'rtu': {'No': 0,'Sí, no infiltrante':1, 'Sí, dudoso':2, 'Sí, infiltrante':3},
    'citologias': {'Negativa': 0, 'Atipias': 1, 'Positiva': 2, 'Sospechosa': 3, 'Carcinoma urotelial': 4},
    'recidiva': {'No': 0,'Menores características':1, 'Iguales características':2, 'Mayores características':3},
    'instalacionprevia': {'No': 0, 'Sí, inmediata MMC': 1, 'Sí, inmediata y diferida con MMC': 2, 'Sí, diferida: BCG, MMG': 3},
    'tabaco': {'NC': 0, 'No': 1, 'Exfumador': 2, '< 10 cigarrillos/día': 3, '10-20 cigarrillos/día': 4, '> 20 cigarrillos/día': 5},
  }

  data = patient
  if (len(data) > 0) and not is_trainig:
    delete_columns = ['dni','fechacir','exitus','progresiva', 'recidiva','nrecidivas', 'evoldesfavorable', 'is_active']
    for file in data:
      for column in delete_columns:
        file.pop(column, None)

    for fila in data:
      for columna, mapeo in mapeo_columnas.items():
          if columna in fila:
              fila[columna] = mapeo.get(fila[columna], fila[columna])

    df = pd.DataFrame(data)
    pd.set_option('display.max_columns', None)
    # print(df)

    df = df.apply(lambda x: pd.to_numeric(x, errors='coerce')).astype('Int64')
    patientData = df.iloc[:, :24]

    if methodID == 0:
      predictions = getRF_Model_Prediction(patientData)
      res = predictions[0]
      res = res.tolist()
      return res
    elif methodID == 1:
      predictions = getRF_Model_Prediction(patientData)
      res = predictions[0]
      res = res.tolist()
      return res
    else:
      return constants.NOT_VALID_METHOD    
  
  else:
    data = list(BladderCancerPrediction.objects.values())
    for fila in data:
      for columna, mapeo in mapeo_columnas.items():
          if columna in fila:
              fila[columna] = mapeo.get(fila[columna], fila[columna])
    
    df = pd.DataFrame(data)
    df = df.apply(lambda x: pd.to_numeric(x, errors='coerce')).astype('Int64')

    X = df.iloc[:, :24]
    y = df.iloc[:, -5:]

    if methodID == 0:
      res = K_NN_Model(X, y)
      return res
    elif methodID == 1:
      res = Random_Forest_Model(X, y)
      return res
    elif methodID == 2:
      res = Naive_Byes_Model(X,y)
      return res
    else:
      return constants.NOT_VALID_METHOD

def K_NN_Model(X, y):
  X_train, y_train = train_test_split(X, y, test_size=0.2, random_state=52)

  k = 3
  knn_classifier = KNeighborsClassifier(n_neighbors=k)
  knn_classifier.fit(X_train, y_train)

  route = constants.KNN_MODEL_ROUTE

  joblib.dump(knn_classifier, route)

  return constants.KNN_TRAINED

def Random_Forest_Model(X, y):
  X_train, y_train = train_test_split(X, y, test_size=0.2, random_state=42)
  random_forest_model = RandomForestClassifier(n_estimators=100, random_state=42)
  random_forest_model.fit(X_train, y_train)
  
  route = constants.RANDOM_FOREST_MODEL_ROUTE

  joblib.dump(random_forest_model, route)

  return constants.RANDOM_FOREST_TRAINED

def Naive_Byes_Model(X,y):
  X_train, y_train = train_test_split(X, y, test_size=0.2, random_state=42)
  naive_bayes_model = [MultinomialNB() for _ in range(5)]

  for i, model in enumerate(naive_bayes_model):
    y_train_single = y_train.iloc[:, i]
    model.fit(X_train, y_train_single)

  route = constants.NAIVE_BAYES_MODEL

  joblib.dump(naive_bayes_model, route)

  return constants.NAIVE_BAYES_TRAINED

def getk_NN_Model_Prediction(paciente):
  model_route = constants.KNN_MODEL_ROUTE
  knn_model = joblib.load(model_route)
  knn_prediction = knn_model.predict(paciente)
  
  return knn_prediction

def getRF_Model_Prediction(paciente):
  model_route = constants.RANDOM_FOREST_MODEL_ROUTE
  random_forest_model = joblib.load(model_route)
  rf_prediction = random_forest_model.predict(paciente)
  return rf_prediction

