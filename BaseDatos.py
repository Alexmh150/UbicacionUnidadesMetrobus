import sqlite3
import pandas as pd

try:
    conx = sqlite3.connect('data.bd')
    print('Se ha establecido la conexion con la base de datos en memoria')    
    x = pd.read_csv("data\prueba_fetchdata_metrobus.csv")    
    x.to_sql('base1',conx)
    print('Se guardo la base de datos')
    conx.close()
except sqlite3.Error as error:
    print('Se ha producion un error', error)