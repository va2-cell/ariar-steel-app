
import streamlit as st
import pandas as pd

# 1. Configuración de Pantalla
st.set_page_config(page_title="Ariar Steel LLC", layout="centered")

# Estilos
st.markdown("""
<style>
    .titulo { color: #1E4D8C; text-align: center; font-family: 'Arial Black'; font-size: 40px; }
    .bienvenida { text-align: center; font-size: 20px; color: #555; margin-bottom: 30px; }
    div.stButton > button { width: 100%; background-color: #1E4D8C; color: white; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='titulo'>ARIAR STEEL LLC</div>", unsafe_allow_html=True)
st.markdown("<div class='bienvenida'>Panel de Control de Horas</div>", unsafe_allow_html=True)

# 2. El Link de tu Excel (ASEGÚRATE DE QUE SEA ESTE)
# Si tu link es diferente, cámbialo aquí abajo entre las comillas
sheet_url = "https://docs.google.com/spreadsheets/d/1cPGCf1XmYtG27U8y2oLdvdV5H086jDg/export?format=csv"

def cargar_datos():
    try:
        return pd.read_csv(sheet_url)
    except:
        # Si falla, crea una tabla vacía para que la app no se trabe
        return pd.DataFrame(columns=["Empleado", "Fecha", "Horas", "Notas"])

df = cargar_datos()

# 3. Menú Lateral
with st.sidebar:
    st.title("MENÚ")
    rol = st.radio("Entrar como:", ["👷 Trabajador", "🔑 Administrador (Edwin)"])

if rol == "👷 Trabajador":
    st.subheader("Consulta tus Horas")
    if not df.empty:
        nombre = st.selectbox("Selecciona tu nombre:", df["Empleado"].unique())
        if st.button("Ver mis horas"):
            mis_horas = df[df["Empleado"] == nombre]
            st.write(f"Horas totales de {nombre}:")
            st.dataframe(mis_horas[["Fecha", "Horas", "Notas"]], use_container_width=True)
    else:
        st.warning("Aún no hay horas registradas en el sistema.")

elif rol == "🔑 Administrador (Edwin)":
    password = st.text_input("Introduce la clave de acceso:", type="password")
    if password == "2222":
        st.success("Acceso concedido.")
        st.info("Para esta versión, registra las horas directamente en tu archivo de Excel de Google y se verán reflejadas aquí automáticamente.")
        st.write("[Abrir mi Google Sheet](https://docs.google.com/spreadsheets/d/1cPGCf1XmYtG27U8y2oLdvdV5H086jDg/)")
