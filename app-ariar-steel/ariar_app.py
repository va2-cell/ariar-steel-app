
import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Ariar Steel LLC", layout="wide")

# 2. Diseño del Panel
st.markdown("""
<style>
    .titulo-principal {
        color: #1E4D8C;
        font-family: 'Arial Black', sans-serif;
        font-size: 45px;
        text-align: center;
        margin-top: 10px;
    }
    .subtitulo {
        color: #555;
        font-size: 22px;
        text-align: center;
        margin-bottom: 20px;
    }
    div[data-testid="stImage"] > img {
        margin: 0 auto;
        display: block;
        border-radius: 15px;
        max-width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# 3. Encabezado del Panel
st.markdown("<div class='titulo-principal'>PANEL DE CONTROL</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>ARIAR STEEL LLC</div>", unsafe_allow_html=True)

# 4. Cargar el logo que acabas de renombrar
try:
    st.image("logo.avif", use_container_width=True)
except:
    st.error("Cargando imagen del panel...")

st.write("---")

# 5. Mensaje de bienvenida
st.info("🚜 El sistema Ariar Steel está listo. Use el menú lateral para registrar jornadas o ver reportes.")

# 6. Menú Lateral
with st.sidebar:
    st.header("MENÚ")
    opcion = st.radio("Seleccione una opción:", ["🏠 Inicio", "🚜 Registro de Horas", "📊 Ver Reportes"])
