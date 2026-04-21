
import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. Configuración de la página
st.set_page_config(
    page_title="Ariar Steel LLC",
    page_icon="🏗️",
    layout="wide"
)

# 2. Estilos Personalizados
st.markdown("""
<style>
    .main-title {
        color: #1E4D8C;
        font-family: 'Arial Black', sans-serif;
        font-size: 45px;
        text-align: center;
        margin-top: 20px;
    }
    .subtitle {
        color: #555;
        font-size: 20px;
        text-align: center;
        margin-bottom: 40px;
    }
    [data-testid="stSidebar"] {
        background-color: #1E4D8C;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Barra Lateral (Menú)
with st.sidebar:
    # Logo en el menú
    st.image("https://raw.githubusercontent.com/EdwinLopez22/Ariar-Steel-App/main/logo_ariar.png", use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>MENÚ</h2>", unsafe_allow_html=True)
    
    opcion = st.radio(
        "Ir a:",
        ["🏠 Inicio (Panel)", "🚜 Registro de Horas", "📊 Ver Reportes"]
    )
    st.write("---")
    st.write("Ariar Steel LLC © 2026")

# 4. Lógica de Pantallas
if opcion == "🏠 Inicio (Panel)":
    # ESTO ES LO QUE VERÁS AL ABRIR LA APP
    st.markdown("<div class='main-title'>PANEL DE CONTROL</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>ARIAR STEEL LLC</div>", unsafe_allow_html=True)
    
    # Logo grande central
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("https://raw.githubusercontent.com/EdwinLopez22/Ariar-Steel-App/main/logo_ariar.png", use_container_width=True)
    
    st.info("Utilice el menú de la izquierda para registrar sus horas o consultar reportes.")

elif opcion == "🚜 Registro de Horas":
    st.markdown("<h2 style='color: #1E4D8C;'>Registro de Jornada</h2>", unsafe_allow_html=True)
    try:
        conn = st.connection("gsheets", type=GSheetsConnection)
        with st.form(key="form_trabajo"):
            empleado = st.selectbox("Empleado", ["Edwin Lopez", "Alexandra", "Personal"])
            fecha = st.date_input("Fecha")
            horas = st.number_input("Horas", min_value=0.0, step=0.5)
            notas = st.text_area("Notas")
            if st.form_submit_button("Guardar Registro"):
                nuevo = pd.DataFrame([{"Empleado": empleado, "Fecha": str(fecha), "Horas": horas, "Notas": notas}])
                actual = conn.read()
                df_final = pd.concat([actual, nuevo], ignore_index=True)
                conn.update(data=df_final)
                st.success("✅ Guardado en el sistema.")
    except:
        st.error("Error de conexión. Verifica los Secrets.")

elif opcion == "📊 Ver Reportes":
    st.markdown("<h2 style='color: #1E4D8C;'>Historial de Trabajo</h2>", unsafe_allow_html=True)
    try:
        conn = st.connection("gsheets", type=GSheetsConnection)
        df = conn.read()
        st.dataframe(df, use_container_width=True)
    except:
        st.error("No se pudo cargar el historial.")
