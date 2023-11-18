from sklearn import datasets, linear_model
import json
import os
import numpy as np
import pandas as pd
import matplotlib as plt  
import seaborn as sns

# Read in data
df = pd.read_csv('day.csv')

# Fit a model
df = df.drop(columns=['season','yr','mnth','instant','casual','registered','holiday','weekday','workingday','weathersit'])   # Elimine las columnas que crea que no son necesarias

<<<<<<< HEAD
target = 'cnt'
feature_list = list(df.columns)
feature_list.remove(target)
=======
clf = MLPClassifier(random_state=0, max_iter=50)
clf.fit(X_train,y_train)
>>>>>>> b29b06913176e58a3ad4a4f770c7e7fc8023944e

ciclista_X_data = df[feature_list]
ciclista_X_target = df[target]
model = linear_model.LinearRegression()
type(model)
model.fit(ciclista_X_data,ciclista_X_target)

with open("metrics.json", 'w') as outfile:
        json.dump({ "coeficiente": model.coef_, "intercepto":model.intercept_}, outfile)
