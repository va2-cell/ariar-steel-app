
import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

# 1. Configuración de Pantalla
st.set_page_config(page_title="Ariar Steel LLC", layout="centered")

# --- FUNCIONES DE BASE DE DATOS ---
def conectar_db():
    conn = sqlite3.connect('ariar_horas.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS registro 
                 (Empleado TEXT, Fecha TEXT, Horas REAL, Notas TEXT)''')
    conn.commit()
    return conn

def guardar_datos(empleado, fecha, horas, notas):
    conn = conectar_db()
    c = conn.cursor()
    c.execute("INSERT INTO registro VALUES (?, ?, ?, ?)", (empleado, fecha, horas, notas))
    conn.commit()
    conn.close()

def cargar_datos_locales():
    conn = conectar_db()
    df = pd.read_sql_query("SELECT * FROM registro", conn)
    conn.close()
    if df.empty:
        return pd.DataFrame(columns=["Empleado", "Fecha", "Horas", "Notas"])
    return df

# --- ESTILOS ---
st.markdown("""
<style>
    .titulo { color: #1E4D8C; text-align: center; font-family: 'Arial Black'; font-size: 40px; }
    .bienvenida { text-align: center; font-size: 20px; color: #555; margin-bottom: 30px; }
    div.stButton > button { width: 100%; background-color: #1E4D8C; color: white; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='titulo'>ARIAR STEEL LLC</div>", unsafe_allow_html=True)
st.markdown("<div class='bienvenida'>Panel de Control de Horas</div>", unsafe_allow_html=True)

df = cargar_datos_locales()

# 2. Menú Lateral
with st.sidebar:
    st.title("MENÚ")
    rol = st.radio("Entrar como:", ["👷 Trabajador", "🔑 Administrador (Edwin)"])

if rol == "👷 Trabajador":
    st.subheader("Consulta tus Horas")
    if not df.empty:
        nombre_sel = st.selectbox("Selecciona tu nombre:", df["Empleado"].unique())
        if st.button("Ver mis horas"):
            mis_horas = df[df["Empleado"] == nombre_sel]
            st.write(f"Horas totales de {nombre_sel}:")
            st.dataframe(mis_horas[["Fecha", "Horas", "Notas"]], use_container_width=True)
    else:
        st.warning("Aún no hay horas registradas en el sistema.")

elif rol == "🔑 Administrador (Edwin)":
    password = st.text_input("Introduce la clave de acceso:", type="password")
    if password == "2222":
        st.success("Acceso concedido.")
        
        # --- FORMULARIO PARA REGISTRAR HORAS ---
        st.subheader("📝 Registrar Nueva Jornada")
        with st.form("registro_form"):
            nombre = st.text_input("Nombre del Empleado")
            fecha = st.date_input("Fecha", datetime.now())
            horas = st.number_input("Cantidad de Horas", min_value=0.0, step=0.5)
            notas = st.text_area("Notas / Proyecto")
            enviar = st.form_submit_button("Guardar en Base de Datos")
            
            if enviar:
                if nombre:
                    guardar_datos(nombre, fecha.strftime('%Y-%m-%d'), horas, notas)
                    st.success(f"Horas de {nombre} guardadas correctamente.")
                    st.rerun() # Para actualizar la tabla abajo
                else:
                    st.error("Por favor, pon un nombre.")

        st.subheader("📊 Todos los Registros")
        st.dataframe(df, use_container_width=True)
