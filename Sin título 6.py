# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 13:13:39 2019

@author: CTIC - UNI
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm

# Definiendo ruta de trabajo
path='C:/Users/CTIC - UNI/Documents/clase2/clase4/'
# Importando data
data=pd.read_csv(path+'data.csv',sep=',') 

# Separar variables de manera matricial
X=data.loc[:,['atraso','vivienda','edad','dias_lab','exp_sf','nivel_ahorro','ingreso',
              'linea_sf','deuda_sf','zona','clasif_sbs','nivel_educ']]
y=data.loc[:,['mora']]

# Separando en train y test
from sklearn.model_selection import train_test_split

Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.2,random_state=4)

# Preprocesamiento de datos
###########################

# Analizando duplicados

np.sum(data.groupby(['dni'])['dni'].count()>1)
# 0-> no hay duplicados
# >1 -> si hay duplicados

# Descriptivo rapido
data.describe()

# Analizando valores extremos
np.percentile(Xtrain.edad, range(101))
np.percentile(Xtrain.deuda_sf, range(101))
# no se calculan los percentiles debido a missings

np.sum(Xtrain.deuda_sf.isnull())

# calculando percentiles omitiendo missings
Xtrain[~Xtrain.deuda_sf.isnull()]['deuda_sf']
np.percentile(Xtrain[~Xtrain.deuda_sf.isnull()]['deuda_sf'],range(101))

# Se usara el p1 y el p99 para el tratamiento de cotas
cotas_edad=np.percentile(Xtrain.edad,[1,99])
cotas_deuda=np.percentile(Xtrain[~Xtrain.deuda_sf.isnull()]['deuda_sf'],[1,99])

# Asignando cotas superiores
Xtrain.loc[Xtrain.edad>=cotas_edad[1],'edad']=cotas_edad[1]
Xtrain.loc[Xtrain.deuda_sf>=cotas_edad[1],'deuda_sf']=cotas_deuda[1]
np.max(Xtrain.edad)
np.max(Xtrain.deuda_sf)


# Asignando cotas inferiores
Xtrain.loc[Xtrain.edad<=cotas_edad[0],'edad']=cotas_edad[0]
Xtrain.loc[Xtrain.deuda_sf<=cotas_edad[0],'deuda_sf']=cotas_deuda[0]
np.min(Xtrain.edad)
np.min(Xtrain.deuda_sf)

# analisando missings
np.sum(Xtrain.isnull())
np.mean(Xtrain.isnull())

# Tratamiento de variables cualitativas

# Tratamiento: vivienda
Xtrain.vivienda.value_counts()
Xtrain.zona.value_counts()
Xtrain.nivel_educ.value_counts()

# Tratamiento: Vivienda -> asignando or
data_train=pd.concat([ytrain,Xtrain],axis=1)

# Agrupar por cada categoria de la vivienda
or_vivienda=pd.DataFrame(data_train.groupby(['vivienda']).mean()['mora'])
or_vivienda['OR']=(1-or_vivienda.mora)/or_vivienda.mora

# Asignando valores
Xtrain['vivienda_f']=np.where(Xtrain.vivienda=='ALQUILADA',or_vivienda.iloc[0,1],
      np.where(Xtrain.vivienda=='FAMILIAR',or_vivienda.iloc[1,1],
               or_vivienda.iloc[2,1]))

# Tratamiento: nivel educativo -> Variables dummy
dummy_nivel=pd.get_dummies(Xtrain.nivel_educ,prefix='d')
Xtrain=pd.concat([Xtrain,dummy_nivel],axis=1)

# Tratamiento: Clasificacion SBS y Zona -> Agrupando categorias
Xtrain['zona_f']=np.where(Xtrain.zona=='Lima',1,0)
Xtrain['clasif_normal']=np.where(Xtrain.clasif_sbs==0,1,0)

# 



