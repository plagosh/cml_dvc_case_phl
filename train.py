from sklearn import datasets, linear_model
import json
import os
import numpy as np
import pandas as pd
import matplotlib as plt  

# Read in data
df = pd.read_csv('day.csv')

# Fit a model
df = df.drop(columns=['season','yr','mnth','instant','casual','registered','holiday','weekday','workingday','weathersit','dteday'])   # Elimine las columnas que crea que no son necesarias

target = 'cnt'
feature_list = list(df.columns)
feature_list.remove(target)

ciclista_X_data = df[feature_list]
ciclista_X_target = df[target]
model = linear_model.LinearRegression()
type(model)
model.fit(ciclista_X_data,ciclista_X_target)
coef = model.intercept_
# intercepto[] = model.coef_

with open("metrics.json", 'w') as outfile:
        json.dump({ "coeficiente": coef}, outfile)
