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
#import matplotlib
#import matplotlib.pyplot as plt
#import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
from autots import AutoTS
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title(":chart_with_upwards_trend: AutoTS Modelo ETS")


#creando horizontal containers
intro= st.container()
fuentedata= st.container()
seriesT=st.container()

#introducción
with intro:
     st.title(":crystal_ball: Modelo ETS")
     st.markdown("Dada la coyuntura mundial por causa de la inflación que a su vez es causada por diversos cuellos de botella generados por la pandemia y la geopolítica actual, se vio que el Dólar tuvo un fortalecimiento que no se esperaba en diversas partes del mundo incluyendo a Colombia, en este caso solo se crearán modelos de series de tiempo usando el paquete AutoTS y Statsmodels de Python.")
     st.markdown(" Para más información [modelos](https://www.statsmodels.org/devel/examples/)")


#carga de datos
#df= pd.read_excel('datos/USD_COP Historical Data.xlsx')
df= pd.read_csv('datos/datos.csv',sep=';')
#configurando el campo fecha
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['Date'] = pd.to_datetime(df['Date'])

#data in
with fuentedata:

     st.title("Datos")
     st.markdown("Se usa el registro historico de la pagína [investing.com](https://www.investing.com/currencies/usd-cop) desde el primero de enero de 2022 al 11 de agosto de 2022")
     st.markdown("Actualizare datos de forma mensual. Acontinuacion podra ver algunos datos estadistiticos de estos datos.")
     st.write(df.head())
     st.write(df.tail())
     st.markdown("Evolucion del precio en el 2022")
     #fig1 = plt.figure(figsize=(15,8))
     #sns.lineplot(data=df, x="Fecha", y="Price", sizes=(15,8),markers=True, dashes=False)
     #st.pyplot(fig1)
     fig1 = px.line(df, x="Date", y="Price", title="USD/COP")
     st.plotly_chart(fig1)

     st.markdown("El modelo demora unos segundos, gracias por tu paciencia")
#creating modeles, autoTS tries and get the best model
#model_list = ['LastValueNaive', 'GLS', 'GLM', 'ETS', 'AverageValueNaive', 'ARIMA', 'Theta', 'ARDL'] models with errors dont use in this case UnobservedComponents, FBprofet, VARMAX, DynamicFactor, VECM
model_list = ['LastValueNaive', 'GLS', 'GLM', 'ETS', 'AverageValueNaive', 'ARIMA', 'Theta', 'ARDL']
#for performance the max values of tries are 1 and a 1 validation(zero value makes one validation), predidtions for 60 days the frecuency its automatic selected with the data
model = AutoTS(forecast_length=30, frequency='infer', prediction_interval=0.95, ensemble='simple', model_list=model_list, transformer_list='all', max_generations=5, num_validations=2)
model = model.fit(df, date_col='Date', value_col='Price', id_col=None)
prediction = model.predict()
forecast = prediction.forecast

#data in
with seriesT:
     st.title(":crystal_ball: AutoTS: ETS")
     st.markdown("Parametros del modelo:")
     st.write(model)
     st.markdown("Resultado de predicción")
     st.write(forecast)
     #xa= forecast.index
     #ya= forecast["Price"]
     #fig = plt.figure(figsize=(15,8))
     #sns.lineplot(xa, ya)
     #st.pyplot(fig)
     #st.pyplot(prediction.plot(model.df_wide_numeric, remove_zeroes=False,))
     fig2 = px.line(forecast, x=forecast.index, y="Price", title="Predicción precio del dolar en los proximos 30 dias")
     st.plotly_chart(fig2)
     fig3 =go.Figure([
     go.Scatter(
        name='Valores precio del dólar en colombia 2022',
        x=df['Date'],
        y=df['Price'],
        mode='lines+markers',
        marker=dict(color='red', size=2),
        showlegend=True
     ),
     go.Scatter(
        name='Predición de valores precio del dólar',
        x=forecast.index,
        y=forecast['Price'],
        mode='lines+markers',
        marker=dict(color='blue', size=2),
        line=dict(width=2),
        showlegend=True
     )
     ])
     fig3.update_layout(
     yaxis_title='Precio',
     title='Valores precio del dólar y prediccion a 30 días',
     hovermode="x"
     )
     st.plotly_chart(fig3)
     #st.write()

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
