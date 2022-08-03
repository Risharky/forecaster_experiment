##################################################
## {Description: Mini proyecto de series de tiempo USD/COP con predicción a 30 dias}
##################################################
## {License_info: Restricted For educational proporses}
##################################################
## Author: {Ricardo Rodriguez Otero}
## Copyright: Copyright {2022}, {}
## Credits: [{credit_list: Fuente de datos investing.com}]
## License: {Ninguna}
## Version: {mayor}.{minor}.{rel}
## Maintainer: {Unmaintained}
## Email: {contact_email}
## Status: {dev_status: under development}
##################################################

#Importando paquetes
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

st.title(":chart_with_upwards_trend: AutoTS Modelo Arima")


#creando horizontal containers
intro= st.container()
fuentedata= st.container()
seriesT=st.container()

#introducción
with intro:
     st.title("Modelo Arima")
     st.markdown("Dada la coyuntura mundial por causa de la inflación que a su vez es causada por diversos cuellos de botella generados por la pandemia y la geopolítica actual, se vio que el Dólar tuvo un fortalecimiento que no se esperaba en diversas partes del mundo incluyendo a Colombia, en este caso solo se crearán modelos de series de tiempo usando el paquete AutoTS y Statsmodels de Python.")
     st.markdown(" Para más información [modelos](https://www.statsmodels.org/devel/examples/)")


#carga de datos
df= pd.read_excel('datos/USD_COP Historical Data.xlsx')
#configurando el campo fecha
df['Fecha'] = pd.to_datetime(df['Fecha'])

#data in
with fuentedata:

     st.title("Datos")
     st.markdown("Se usa el registro historico de la pagína [investing.com](https://www.investing.com/currencies/usd-cop) desde el primero de enero de 2022 al 2 de agosto de 2022")
     st.markdown("Actualizare datos de forma mensual. Acontinuacion podra ver algunos datos estadistiticos de estos datos.")
     st.write(df.head())
     st.write(sns.lineplot(data=df, x="Fecha", y="Price"))

#data in
with seriesT:
     st.title("AutoTS")
     st.markdown("La librería autoTS es una librería de Python que permite automatizar la creación de series de tiempo, pero usa a su vez varios paquetes como statsmodels(se usaran 3 modelos de esta librería), prophet, sklearn, pytorch-forecasting entre otros, en futuros proyectos tal vez use estas librerías.")
     st.markdown(" Para más información [AutoTS](https://github.com/winedarksea/AutoTS)")

#sidebar
st.sidebar.markdown("Desarrollado para fines academicos, no use los datos generados para realizar transacciones")
st.sidebar.write(f'''
    <a target="_blank" href="https://risharky.github.io">
        <button>
            Retornar a GH pages
        </button>
    </a>
    ''',
    unsafe_allow_html=True
)
st.sidebar.markdown(" &copy; 2022 &copy;")
