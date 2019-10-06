# Importando librerías
import pandas as  pd
import numpy as np
from statsmodels.formula.api import ols

# Definiendo ruta de trabajo
path='C:/Users/CTIC - UNI/Documents/clase2/'
# Importando data
ventas=pd.read_csv(path+'ventas.csv',sep=',')

# Cambiando nombres de las columnas
ventas.columns=['ventas','precio','public','calid','miss']
# Eliminando columnas
ventas.drop(['miss'],axis=1,inplace=True)

# Analizando correlación entre variables
correlaciones=pd.DataFrame(np.corrcoef(ventas,rowvar=False))
correlaciones.columns=ventas.columns
correlaciones.index=ventas.columns

# Regresión Lineal: MCO
#######################
# Definiendo objeto
modelo=ols(formula='ventas~precio+public+calid',data=ventas)
# Entrenando el modelo
modelo=modelo.fit()
# Summary
modelo.summary()

#Extrayendo objetos
modelo.params # coeficientes
modelo.bse # std(coeficientes)

# prueba de hipotesis
# Ho = bcalidad=0

# Definiento parametros
alpha=0.05 #nivel de significancia
k=0 # valor a testear

# Estadistico calculado
tcalc=(modelo.params[3]-k)/modelo.bse[3]

# Estadistico de tablas
from scipy import stats
ttab = stats.t.ppf(alpha/2,len(ventas)-len(modelo.params))

# Regla de desicion
if abs(tcalc)>abs(ttab):
    print('Se rechaza Ho')
else:
    print('No se Rechaza Ho')

# Intervalo de confianza
ls_calid=modelo.params[3]+stats.t.ppf(1-alpha/2,len(ventas)-len(modelo.params))*modelo.bse[3]
ls_calid=modelo.params[3]+stats.t.ppf(alpha/2,len(ventas)-len(modelo.params))*modelo.bse[3]















