# Importando librerías
import pandas as  pd
import numpy as np
import statsmodels.api as sm

# Definiendo ruta de trabajo
path='C:/Users/USUARIO/Downloads/'
# Importando data
data=pd.read_csv(path+'data.csv')

# Generando variables X e y
y=data.loc[:,'mora']
X=data.loc[:,['atraso','edad','dias_lab','nivel_ahorro','score','ingreso']]

# Añadiendo intercepto (genera columna de unos)
X=sm.add_constant(X)

# Regresión Logística
######################
# Generando objeto
modelo=sm.Logit(y,X)
# Entrenando modelo
modelo=modelo.fit()
# Resultados
modelo.summary()

# Puntuando
xbeta=5.7497+0.0197*(50)+0.0065*(30)-8.746e-05*(1200)-0.0703*(7)-0.0190*(150)-3.724e-05*(6000)
import math
prob=1/(1+math.exp(-xbeta))




