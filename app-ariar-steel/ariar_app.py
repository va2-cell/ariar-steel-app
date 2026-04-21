
import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. Configuración de la página (Con logo en la pestaña)
st.set_page_config(
    page_title="Ariar Steel LLC",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Estilos Personalizados (Panel profesional azul)
st.markdown("""
<style>
    /* Estilo para el título principal */
    .main-title {
        color: #1E4D8C; /* Azul Ariar Steel */
        font-family: 'Arial Black', sans-serif;
        font-size: 50px;
        text-align: center;
        margin-top: 30px;
        margin-bottom: -10px;
    }
    /* Estilo para el subtítulo */
    .subtitle {
        color: #555555;
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 24px;
        text-align: center;
        margin-bottom: 50px;
    }
    /* Estilo para el cuadro azul informativo */
    .stAlert {
        border: 2px solid #1E4D8C;
        border-radius: 10px;
    }
    /* Asegurar que el logo central esté bien centrado en celulares */
    div[data-testid="stImage"] > img {
        margin: 0 auto;
        display: block;
    }
</style>
""", unsafe_allow_html=True)

# 3. Contenedor Central para el Panel de Control
# He quitado las columnas para asegurar que el logo central sea lo más grande posible.

st.markdown("<div class='main-title'>PANEL DE CONTROL</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>ARIAR STEEL LLC</div>", unsafe_allow_html=True)

# 4. EL LOGO CENTRAL GRANDE
# He verificado la URL de tu logo en GitHub para que cargue perfectamente.
# Si en el futuro quieres cambiar la foto, solo tienes que cambiar esta URL.
logo_url = "https://raw.githubusercontent.com/EdwinLopez22/Ariar-Steel-App/main/logo_ariar.png"

# Intento de cargar la imagen con un control de error para que no salga el cuadro roto
try:
    # use_container_width=True asegura que se adapte al tamaño de la pantalla del celular
    st.image(logo_url, use_container_width=True, caption=None) 
except:
    # Si la URL falla, simplemente no muestra nada en lugar de un cuadro roto.
    pass

st.write("---")

# 5. Cuadro informativo principal
st.info("🚜 Utilice el menú de la izquierda (el icono de las flechas >> arriba) para **registrar sus horas** o consultar reportes.")
