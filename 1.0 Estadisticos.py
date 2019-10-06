# Comandos de análisis estadístico
##################################

# Importando librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Distribución uniforme
#######################

# Uniforme estándar: a=0 b=1 size=1
np.random.uniform()
# a=5 b=10 size=1
np.random.uniform(5,10)
# a=5 b=10 size=(filas,columnas)
np.random.uniform(5,10,size=(100,1))
np.random.uniform(5,10,size=(1,100))
np.random.uniform(5,10,size=(100,100))

unif=np.random.uniform(5,10,1000000)
plt.hist(unif)

# Distribución normal
#####################

# Normal estándar: u=0 std=1 size=1
np.random.normal()
# u=5 std=2 size=1
np.random.normal(5,2)
# u=5 std=2 size=(filas,columnas)
np.random.normal(5,2,size=(100,1))
np.random.normal(5,2,size=(1,100))
np.random.normal(5,2,size=(100,100))

norm=np.random.normal(5,2,1000000)
plt.hist(norm,bins=100)

# ¿ Qué porcentaje de datos hay en +-1 std?
np.mean((norm>=3)&(norm<=7))
# ¿ Qué porcentaje de datos hay en +-2 std?
np.mean((norm>=1)&(norm<=9))
# ¿ Qué porcentaje de datos hay en +-3 std?
np.mean((norm>=-1)&(norm<=11))

# Distribución uniforme enteros
################################
np.random.randint(1,7)

# Cálculo estadístico
#####################
# Promedio
np.mean(norm)
# Máximo
np.max(norm)
# Mínimo
np.min(norm)
# Varianza
np.var(norm)
# Desviación estándar
np.std(norm)
# Percentiles
np.percentile(norm,50) # mediana
np.percentile(norm,20) # p20
np.percentile(norm,[1,99]) # p1 y p99
np.percentile(norm,range(101))

# Importando librería
from scipy.stats import kurtosis,skew
kurtosis(norm) # exceso de kurtosis
skew(norm)

# Simular distribución t student
np.random.standar_t()

# Ejercicio:

# Simular: utilidad~N(30,15,10000)
utilidad=np.random.normal(30,15,10000)
# ¿Probabilidad de pérdida?
np.mean(utilidad<=0)
# ¿Probabilidad 25<=utilidad<=40?
np.mean((utilidad>=25)&(utilidad<=40))
# ¿x? / P(utilidad<=x)=0.1%
np.percentile(utilidad,0.1)

# Semilla aleatoria
np.random.uniform()
np.random.seed(4) # semilla aleatoria
np.random.uniform()

































































































