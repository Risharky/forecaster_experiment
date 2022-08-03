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