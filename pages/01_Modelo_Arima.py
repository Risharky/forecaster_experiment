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

#creating modeles, autoTS tries and get the best model
#model_list = ['LastValueNaive', 'GLS', 'GLM', 'ETS', 'AverageValueNaive', 'ARIMA', 'Theta', 'ARDL'] models with errors dont use in this case UnobservedComponents, FBprofet, VARMAX, DynamicFactor, VECM
model_list = ['ARIMA']
#for performance the max values of tries are 1 and a 1 validation(zero value makes one validation), predidtions for 60 days the frecuency its automatic selected with the data
model = AutoTS(forecast_length=30, frequency='infer', prediction_interval=0.95, ensemble='simple', model_list=model_list, transformer_list='all', max_generations=5, num_validations=2, n_jobs='auto')
model = model.fit(df, date_col='Fecha', value_col='Price', id_col=None)
prediction = model.predict()
forecast = prediction.forecast

#data in
with seriesT:
     st.title("AutoTS:ARIMA")
     st.markdown("Parametros del modelo:")
     st.write(model)
     st.markdown("Resultado de predicción")
     st.write(forecast)

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
