
import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. Configuración de Seguridad y Pantalla
st.set_page_config(page_title="Ariar Steel LLC", layout="centered")

# Estilos rápidos (Azul y Blanco)
st.markdown("""
<style>
    .titulo { color: #1E4D8C; text-align: center; font-family: 'Arial Black'; font-size: 40px; }
    .bienvenida { text-align: center; font-size: 20px; color: #555; margin-bottom: 30px; }
    div.stButton > button { width: 100%; background-color: #1E4D8C; color: white; }
</style>
""", unsafe_allow_html=True)

# 2. Panel de Bienvenida
st.markdown("<div class='titulo'>ARIAR STEEL LLC</div>", unsafe_allow_html=True)
st.markdown("<div class='bienvenida'>Bienvenido al sistema de control de jornadas</div>", unsafe_allow_html=True)

# 3. Menú Lateral
with st.sidebar:
    st.title("MENÚ")
    rol = st.radio("Entrar como:", ["👷 Trabajador", "🔑 Administrador (Edwin)"])

# 4. Conexión a Google Sheets
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()

    if rol == "👷 Trabajador":
        st.subheader("Consulta tus Horas")
        nombre = st.selectbox("Selecciona tu nombre:", df["Empleado"].unique() if not df.empty else ["Sin datos"])
        
        if st.button("Ver mis horas"):
            mis_horas = df[df["Empleado"] == nombre]
            st.dataframe(mis_horas[["Fecha", "Horas", "Notas"]], use_container_width=True)

    elif rol == "🔑 Administrador (Edwin)":
        password = st.text_input("Introduce la clave de acceso:", type="password")
        
        # Clave simple para que solo tú entres (puedes cambiar '1234')
        if password == "2222":
            st.success("Acceso concedido, Edwin.")
            st.subheader("Registrar Horas de Trabajadores")
            
            with st.form("form_admin"):
                emp = st.text_input("Nombre del Trabajador")
                fec = st.date_input("Fecha")
                hrs = st.number_input("Horas Trabajadas", min_value=0.0, step=0.5)
                not_ = st.text_area("Tarea realizada")
                
                if st.form_submit_button("Guardar en el Sistema"):
                    nuevo = pd.DataFrame([{"Empleado": emp, "Fecha": str(fec), "Horas": hrs, "Notas": not_}])
                    df_final = pd.concat([df, nuevo], ignore_index=True)
                    conn.update(data=df_final)
                    st.success("✅ Horas registradas correctamente.")
        elif password != "":
            st.error("Clave incorrecta")

except Exception as e:
    st.info("Configurando conexión... Asegúrate de conectar tu Google Sheet en Streamlit Cloud.")
