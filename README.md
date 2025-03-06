#Logistic regression: an example using a personal SQL database made from Spanish census data

From this point, I will continue in Spanish (I’m Spanish, after all). If you are interested in this, you can use Google Translator.


PROGRAMA PARA REALIZAR UNA REGRESIÓN LOGÍSTICA

En este programa vamos a emplear una regresión logística usando los datos del censo del INE (Instituto Nacional de Estadística, de España) para tratar de predecir si la población de un municipio subirá o bajará en un año determinado. 
Estos datos han sido previamente limpiados y almacenados en una base de datos personal, y en este programa se descargarán mediante una consulta SQL, para posteriormente ser introducidos en un DataFrame.




DATOS EMPLEADOS

Este programa usa una base de datos SQL personal en la que se han almacenado los datos del censo obtenidos del INE.

Los datos originales pueden obtenerse aquí: https://www.ine.es/jaxiT3/Tabla.htm?t=31304

Para que este programa funcione directamente, evidentemente debe crearse una base de datos similar o modificar el programa. 
Intentaremos publicar más adelante los pasos seguidos para limpiar y crear esa base de datos. 
El único dato relevante a indicar aquí es que, durante la limpieza y creación de la base de datos, se eliminaron 17 municipios de tamaño muy pequeño por presentar datos incompletos. 
Consideramos que esto no afecta al planteamiento ni al resultado.

En este programa solo se emplearán los datos de los años 2001 al 2020, siendo este último el año a estudiar.




REQUISITOS Y LIBRERÍAS

Este programa usa un archivo .env en el que deben constar los datos de conexión. 
Incluimos un archivo de ejemplo, que simplemente debe modificarse abriéndolo con el Notepad para incluir los datos de conexión a la base de datos. 
Después, basta con modificar en el programa la línea: ( " load_dotenv('enviroments/database.env') " sustituyéndola por la ruta donde se haya guardado el archivo.

Además, este programa utiliza las siguientes librerías:

pymysql
pandas
os
scikit-learn





DESCRIPCIÓN DEL PROGRAMA

Este programa pretende predecir si la población del año 2020 subirá (valor 1) o bajará (valor 0), a partir de dos variables predictoras:

- La provincia a la que pertenece el municipio.
- La variación porcentual de la población de ese municipio entre 2001 y 2019.

De todos los municipios de España el programa selecciona al azar el 70% para entrenar el modelo.
El planteamiento subyacente era usar el 30% restante para realizar posteriormente una validación del modelo.
No obstante, esto finalmente no se ha llevado a cabo debido a que el propio reporte del modelo nos indica que la capacidad de predicción no es demasiado buena.


POSIBLE DESARROLLO FUTURO

El programa en sí funciona de la forma esperada, cumpliendo su función de ejemplo de regresión logística programada en Python y, además, usando una consulta SQL para obtener los datos.
La cuestión es que como hemos indicado la capacidad de predicción obtenida es pobre. 
En este momento no sabemos aún si trabajaremos para intentar mejorar la capacidad de predicción de este modelo o si directamente pasaremos a intentar usar otro modelo de predicción.


