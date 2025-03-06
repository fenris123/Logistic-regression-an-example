# Logistic-regression-an-example
Logistic regression:  an example using a personal SQL database made from spanish census data.

From this point, i will continue in spanish. (i'm spanish, after all). If you are interested on this, you can use google translator.


PROGRAMA PARA REALIZAR UNA REGRESION LOGISTICA.

En este programa vamos a emplear una regresion logistica usando los datos del censo del INE (Instituto Nacional de Estadistica, de España) para tratar de predecir si la población  de un municipio
subira o bajara en un año determinado. Estos datos han sido previamente limpiados y almacenados en una base de datos personal, y en este programa se descargaran mediante una consulta SQl, y se introduciran en un df. 


DATOS EMPLEADOS.

Este programa usa una base de datos SQL personal en la que se han almacenado los datos del censo obtenidos del INE.

Los datos originales pueden obtenerse aqui:
https://www.ine.es/jaxiT3/Tabla.htm?t=31304

Para que este programa funcione directamente debe evidentemente crearse una base de datos similar o modificar el programa. 
Intentaremos publicar mas adelante los pasos seguidos para limpiar y crear esa base de datos.
El unico dato relevante a indicar aqui es que durante la limpieza y creacion de la base de datos se eliminaron 17 municipios de tamaño muy pequeño por presentar datos incompletos. 
Consideramos que esto no afecta al planteamiento ni al resultado. 


En este programa solo se emplearan los datos de los años 2001 al 2020, siendo este ultimo el año a estudiar. 




REQUISITOS Y LIBRERIAS.

Este programa usa un archivo .env en el que deben constar los datos de conexion. 
Incluimos un archivo de ejemplo. Simplemente debe modificarse abriendolo con el notepad para incluir los datos de conexion a la base de datos.
Despues basta con modificar en el programa la linea  " load_dotenv('enviroments/database.env') " poniendo en su lugar la ruta donde se haya guardado el archivo.

Ademas este programa usa las siguientes librerias:

pymysql
pandas
os 
scikit-learn





DESCRIPCION DEL PROGRAMA.

Este programa pretende predecir si la poblacion del año 2020 subira (valor 1) o bajara (valor 0), a partir de dos variables predictoras.
Estas son la provincia a la que pertenece el municipio, y la variacion de la poblacion de ese municipio en terminos porcentuales entre 2001 y 2019.

De todos los municipios de España el programa selecciona al azar el 70% para entrenar el modelo.  
El planteamiento subyacente es usar el 30% restante para despues hacer una validacion del mismo. 

No obstante esto finalmente no se ha llevado a cabo, debido a que el propio reporte del modelo nos indica que la capacidad de prediccion no es demasiado buena.



POSIBLE DESARROLLO FUTURO.

El programa en si funciona de la forma esperada, cumpliendo su funcion de ejemplo de regresion logistica programada en Python, y ademas usando una consulta SQL para obtener los datos. 
La cuestion es que como decimos la capacidad de prediccion obtenida es pobre.
En este momento no sabemos aun si lo que haremos será trabajar para intentar mejorar la capacidad de prediccion de este modelo, o bien si directamente pasaremos a intentar usar otro modelo de prediccion
