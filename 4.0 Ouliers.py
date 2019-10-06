# Tratamiento de valores extremos
##################################

# Importando librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulando data
norm=np.random.normal(5000,125,1000)
data=pd.DataFrame(norm)
data.columns=['norm']

# Calculando percentiles
np.percentile(data,[0,1,2,3,4,5,95,96,97,98,99,100])
perc=np.percentile(data,[0,1,2,3,4,5,95,96,97,98,99,100])

# 1) Eliminando valores extremos
data2=data[(data.norm<=perc[10])&(data.norm>=perc[1])]
data3=data[(data.norm<=np.percentile(data,99))&(data.norm>=np.percentile(data,1))]

# 2) Acotando
data['norm_acot']=np.where(data.norm<=np.percentile(data,1),np.percentile(data,1),
    np.where(data.norm>=np.percentile(data,99),np.percentile(data,99),data.norm))

# Verificando cotas
plt.hist(data.norm)
plt.hist(data.norm_acot)

np.min(data.norm),np.max(data.norm)
np.min(data.norm_acot),np.max(data.norm_acot)
np.percentile(data.norm,[1,99])











