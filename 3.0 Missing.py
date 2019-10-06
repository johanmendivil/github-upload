# Trabajando con valores faltantes (missings):

# Importando librerías
import numpy as np
import pandas as pd

# Generando data frame
df=pd.DataFrame([[1,np.nan,2,np.nan],
                 [2,3,5,np.nan],
                 [np.nan,4,6,np.nan]])

# Asignando nombres a las columnas
df.columns=['x1','x2','x3','x4']
# Asignando nombres a las filas
df.index=['a','b','c']

df

# Cuantificando cantidad de missings
df.isnull()
# Por columnas
np.sum(df.isnull()) # términos absolutos
np.mean(df.isnull()) # términos relativos
# Por filas
np.sum(df.isnull(),axis=1) # términos absolutos
np.mean(df.isnull(),axis=1) # términos relativos
# Para una variable en particular
np.sum(df.x2.isnull())
np.mean(df.x2.isnull())

# Tratamiento de missings
#########################

# 1) Eliminando observaciones
df
# Elimino columnas con al menos un missing
df.dropna(axis=1)
# Elimino filas con al menos un missing
df.dropna(axis=0)

# Elimino columnas donde todo este en missing
df.dropna(axis=1,how='all')
# Elimino filas donde todo este en missing
df.dropna(axis=0,how='all')

# Estableciendo umbrales
df.dropna(axis=1,thresh=2)
df.dropna(axis=0,thresh=2)

# OJO: Para guardar campos
# df.dropna(axis=1,inplace=True)
# df=df.dropna(axis=1)

# 2) Asignación de missings
df
df.fillna(0)
df.x1=df.x1.fillna(np.mean(df.x1))
df.x2=df.x2.fillna(np.percentile(df.x2,50))
df.x4=df.x4.fillna(999)

# Generando data frame original
df=pd.DataFrame([[1,np.nan,2,np.nan],
                 [2,3,5,np.nan],
                 [np.nan,4,6,np.nan]])

# Asignando nombres a las columnas
df.columns=['x1','x2','x3','x4']
# Asignando nombres a las filas
df.index=['a','b','c']

# Completando con el dato previo
df
df.fillna(method='ffill',axis=0) # por columnas
df.fillna(method='ffill',axis=1) # por filas

# Completando con el dato siguiente
df
df.fillna(method='bfill',axis=0) # por columnas
df.fillna(method='bfill',axis=1) # por filas





























































