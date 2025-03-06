# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 11:14:07 2025

@author: fenris123
"""

#####  WARNING  #####
#####  WARNING  #####

#  Este programa requiere un archivo .env con los datos de conexion.



### PASO 1: Librerias
 
### pip install pymysql
### pip install pandas
### pip install os 
### pip install scikit-learn
### pip install numpy



import pymysql
import pandas as pd
import numpy as np
import os

from dotenv import load_dotenv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report






### PASO 2: Leer la base de datos y meterla en un DF


load_dotenv('enviroments/database.env')  #EN ESTE ARCHIVO DEBEN ESTAR LOS DATOS DE CONEXION


conn = pymysql.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)


### Creacion del query SQL
query = """
SELECT 
    p.id_municip,
    m.municipio,
    p.year,
    p.poblacion_total,
    pr.provincia,
    ROUND((p.poblacion_total - p2001.poblacion_total) / p2001.poblacion_total * 100,2) AS variacion_porcentual,
    CASE WHEN p.poblacion_total > p2019.poblacion_total THEN 1 ELSE 0 END AS sube_baja
FROM 
    poblacion p
JOIN 
    municipios m ON p.id_municip = m.id_municip
JOIN 
    provincias pr ON m.cod_prov = pr.cod_prov
LEFT JOIN 
    poblacion p2001 ON p2001.id_municip = p.id_municip AND p2001.year = 2001
LEFT JOIN 
    poblacion p2019 ON p2019.id_municip = p.id_municip AND p2019.year = 2019
WHERE 
    p.year = 2020;
"""

df_municipios = pd.read_sql(query, conn)

conn.close()




#### PASO OPCIONAL   Comprobar que nuestro dataframe esta como nosotros queremos.

print(df_municipios.head())




###  PASO 3  Regresion logistica.

df = df_municipios.copy()


# Creamos la variable "dummy" para provincia.
# En lenguaje claro: pasamos las provincias a un df de 0 y 1, que indica "presencia" o "ausencia" de cada provincia.

df = pd.get_dummies(df, columns=['provincia'], drop_first=True)   #creamos la vairable "dummy" para provincia.



# creacion de variables predictoras  y objetivo, y selecciond el 70% para entrenamiento, y 30% para validacion.

X = df.drop(columns=['sube_baja', 'id_municip', 'municipio', 'year', 'poblacion_total'])
y = df['sube_baja']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Entrenamos el modelo.
modelo = LogisticRegression(max_iter=1000)    #Con otros datos puede ser recomendable aumentar las iteracciones.
modelo.fit(X_train, y_train)


# ejecutamos el test. 

y_pred = modelo.predict(X_test)


print("Resultados de la matriz de confusión:")
print(confusion_matrix(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

# Imprimir los resultados con descripciones
print(f"Datos indican baja, modelo indica baja (acierto del modelo): {tn}")
print(f"Datos indican baja, modelo indica subida (fallo del modelo): {fp}")
print(f"Datos indican subida, modelo indica baja (fallo del modelo): {fn}")
print(f"Datos indican subida, modelo indica subida (acierto del modelo): {tp}")

print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred))


