
import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Ariar Steel LLC", page_icon="🏗️")

# --- BASE DE DATOS ---
conn = sqlite3.connect('ariar_horas.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS registros 
             (fecha TEXT, nombre TEXT, horas REAL, notas TEXT)''')
conn.commit()

# --- DICCIONARIO DE PINS ---
PINS = {
    "Luis": "8349",
    "Melvin": "9064",
    "Edwin": "3909",
    "Admin": "2222"
}

st.title("🏗️ Ariar Steel LLC")

menu = ["Registrar Horas (Admin)", "Ver Mis Horas (Trabajador)"]
choice = st.sidebar.selectbox("Menú", menu)

# --- SECCIÓN ADMINISTRADOR ---
if choice == "Registrar Horas (Admin)":
    pin_admin = st.text_input("PIN de Administrador", type="password")
    if pin_admin == PINS["Admin"]:
        st.success("Acceso concedido")
        with st.form("registro_form"):
            fecha = st.date_input("Fecha", datetime.now())
            nombre = st.selectbox("Empleado", ["Luis", "Melvin", "Edwin"])
            horas = st.number_input("Horas Trabajadas", min_value=0.0, step=0.5)
            notas = st.text_area("Notas (Opcional)")
            enviar = st.form_submit_button("Guardar Registro")
            
            if enviar:
                c.execute("INSERT INTO registros VALUES (?,?,?,?)", (fecha.strftime('%Y-%m-%d'), nombre, horas, notas))
                conn.commit()
                st.success(f"Registradas {horas} horas para {nombre}")
    elif pin_admin != "":
        st.error("PIN Incorrecto")

# --- SECCIÓN TRABAJADOR ---
else:
    nombre_emp = st.selectbox("Selecciona tu nombre", ["Luis", "Melvin", "Edwin"])
    pin_emp = st.text_input("Ingresa tu PIN personal", type="password")
    
    if st.button("Ver mi reporte"):
        if nombre_emp in PINS and pin_emp == PINS[nombre_emp]:
            df = pd.read_sql_query(f"SELECT fecha, horas, notas FROM registros WHERE nombre='{nombre_emp}'", conn)
            if not df.empty:
                st.write(f"### Horas de {nombre_emp}")
                st.table(df)
                st.info(f"Total acumulado: {df['horas'].sum()} horas")
            else:
                st.warning("Aún no tienes horas registradas.")
        elif pin_emp != "":
            st.error("PIN incorrecto para este usuario.")