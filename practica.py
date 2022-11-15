# consume los datos del archivo de inversiones
# almacena en un dataframe el NOM_EMS, la superficie y el TIPUSSOL
# giráfico de dspersión de los importes de inversiones por TIPUSSOL
# gráfico de barras de la inversión media de los 10 primeros NOM_ENS
# grafico circular de las inversiones de 10 TIPUSSOL

import pandas as pd
import matplotlib.pyplot as plt

def consumirDispersion():

    datos = pd.read_csv('suelo.csv')

    df = datos[['NOM_ENS', 'SUPERFICIE', 'TIPUSSOL', 'EXTRACCIO']]  # convertir datos en DataFrame
    df.plot.scatter(x='SUPERFICIE', y='EXTRACCIO', alpha=0.3)
    plt.show()

#consumirDispersion()

def consumirBarras():

    datos = pd.read_csv('suelo.csv')

    df = datos[['NOM_ENS', 'SUPERFICIE', 'TIPUSSOL', 'CODI_TIPUSSOL']]  # convertir datos en DataFrame

    valor_por_ciudad = df.groupby("NOM_ENS")["CODI_TIPUSSOL"].mean()
    valor_por_ciudad.head(10).plot.barh()

    plt.show()
consumirBarras()