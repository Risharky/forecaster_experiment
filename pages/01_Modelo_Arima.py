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
import matplotlib.pyplot as plt
import seaborn as sns

st.title(":chart_with_upwards_trend: Previsiones USD/COP usando Serie de tiempo")


#creando horizontal containers
intro= st.container()
fuentedata= st.container()
seriesT=st.container()

#introducción
with intro:
     st.title("Proyecto con fines educativos ")
     st.markdown("Dada la coyuntura mundial por causa de la inflación que a su vez es causada por diversos cuellos de botella generados por la pandemia y la geopolítica actual, se vio que el Dólar tuvo un fortalecimiento que no se esperaba en diversas partes del mundo incluyendo a Colombia, en este caso solo se crearán modelos de series de tiempo usando el paquete AutoTS y Statsmodels de Python.")
     st.markdown(" Para más información [modelos](https://www.statsmodels.org/devel/examples/)")


#data in
with fuentedata:
     st.title("Datos usados")
     st.markdown("Este proyecto se desarrolla de forma experimental para predecir variaciones en el precio del dólar(USD) contra el peso colombiano(COP), se realiza análisis del precio del dólar en pesos colombianos usando el precio de cierre, los datos usados provienen del histórico que genera la página especializada investing.com")
     st.markdown("Actualizare datos de forma mensual para identificar la precisión y variación de valores en cada modelo.")

#data in
with seriesT:
     st.title("AutoTS")
     st.markdown("La librería autoTS es una librería de Python que permite automatizar la creación de series de tiempo, pero usa a su vez varios paquetes como statsmodels(se usaran 3 modelos de esta librería), prophet, sklearn, pytorch-forecasting entre otros, en futuros proyectos tal vez use estas librerías.")
     st.markdown(" Para más información [AutoTS](https://github.com/winedarksea/AutoTS)")

#sidebar
st.sidebar.markdown("Desarrollado para fines academicos, no use los datos generados para realizar transacciones")
st.sidebar.write(f'''
    <a target="_blank" href="risharky.github.io/">
        <button>
            Retornar a GH pages
        </button>
    </a>
    ''',
    unsafe_allow_html=True
)
st.sidebar.markdown(" &copy; 2022 &copy;")
