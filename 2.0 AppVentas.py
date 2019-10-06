# Importando librerías
import pandas as pd
import numpy as np

# Definiendo fichero de trabajo
path='C:/Users/CTIC - UNI/Documents/clase2/'

# Importando data
ventas=pd.read_csv(path+'ventas.csv')

# Verificando nombre de las columnas
ventas.columns

# Cambiar nombre a las columnas
ventas.columns=['ventas','precio','public','calid','miss']
ventas.columns

# Descriptivos
ventas.describe()

# Eliminar columna miss
ventas.drop(['miss'],axis=1,inplace=True)

# ventas=ventas.drop(['calid'],axis=1)

# Covarianzas
ventas_cov=np.cov(ventas,rowvar=False)
# Correlaciones
ventas_cor=pd.DataFrame(np.corrcoef(ventas,rowvar=False))
# Asignando nombres
ventas_cor.columns=ventas.columns
ventas_cor.index=ventas.columns

# Cálculando estadísticos
np.percentile(ventas['ventas'],90)
np.percentile(ventas.ventas,90)
np.mean((ventas.public>=400)&(ventas.public<=450))

# Predicción de la ventas
# 1) Promedio
np.mean(ventas.ventas)
np.mean(ventas.ventas.tail(5)) # Los ultimos 5 datos
np.mean(ventas.ventas.head(5)) # Los primeros 5 datos
# 2) Mediana
np.percentile(ventas.ventas,50)
np.percentile(ventas.ventas.tail(5),50)
# 3) Tendencia
ventas.ventas.pct_change()
np.mean(ventas.ventas.pct_change())
tasa=np.mean(ventas.ventas.pct_change().tail(5))
ventas.ventas.tail(1)*(1+tasa)
import matplotlib.pyplot as plt
plt.plot(ventas.ventas.pct_change())
plt.hist(ventas.ventas)
# 4) Correlaciones
ventas.ventas/ventas.public
plt.plot(ventas.ventas/ventas.public)
factor=np.mean(ventas.ventas/ventas.public)
450*factor

















