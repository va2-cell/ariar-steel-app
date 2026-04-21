import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime, time

st.set_page_config(page_title="Ariar Steel LLC", page_icon="🏗️")

# Conexión a la base de datos
conn = sqlite3.connect('ariar_horas.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS registros (fecha TEXT, nombre TEXT, horas REAL, notas TEXT)')
conn.commit()

PINS = {"Luis": "8349", "Melvin": "9064", "Edwin": "3909", "Admin": "2222"}

st.title("🏗️ Ariar Steel LLC")
menu = ["Registrar Horas (Admin)", "Ver Mis Horas (Trabajador)"]
choice = st.sidebar.selectbox("Menú", menu)

if choice == "Registrar Horas (Admin)":
    pin_admin = st.text_input("PIN de Administrador", type="password")
    if pin_admin == PINS["Admin"]:
        st.success("Acceso concedido")
        with st.form("registro_form"):
            fecha = st.date_input("Fecha", datetime.now())
            nombre = st.selectbox("Empleado", ["Luis", "Melvin", "Edwin"])
            h_entrada = st.time_input("Hora de Entrada", time(7, 0))
            h_salida = st.time_input("Hora de Salida", time(17, 0))
            lonche = st.selectbox("Tiempo de lonche (horas)", [0.5, 1.0, 0.0], index=0)
            notas = st.text_area("Notas (Opcional)")
            if st.form_submit_button("Guardar Registro"):
                t1 = datetime.combine(fecha, h_entrada)
                t2 = datetime.combine(fecha, h_salida)
                horas_c = ((t2 - t1).total_seconds() / 3600) - lonche
                if horas_c <= 0:
                    st.error("Error: La salida debe ser después de la entrada.")
                else:
                    c.execute("INSERT INTO registros VALUES (?,?,?,?)", (fecha.strftime('%Y-%m-%d'), nombre, horas_c, notas))
                    conn.commit()
                    st.success(f"Registradas {horas_c} horas.")
    elif pin_admin != "":
        st.error("PIN Incorrecto")
else:
    nombre_emp = st.selectbox("Selecciona tu nombre", ["Luis", "Melvin", "Edwin"])
    pin_emp = st.text_input("Ingresa tu PIN personal", type="password")
    if st.button("Ver mi reporte"):
        if nombre_emp in PINS and pin_emp == PINS[nombre_emp]:
            df = pd.read_sql_query(f"SELECT fecha, horas, notas FROM registros WHERE nombre='{nombre_emp}'", conn)
            if not df.empty:
                df['fecha'] = pd.to_datetime(df['fecha']).dt.strftime('%A %m-%d-%Y')
                st.table(df)
                st.info(f"Total: {df['horas'].sum()} horas")
            else:
                st.warning("No hay registros aún.")
        elif pin_emp != "":
            st.error("PIN incorrecto.")

# --- PANEL DE CONTROL MAESTRO ---
st.sidebar.markdown("---")
if st.sidebar.checkbox("Acceso Administrador Maestro"):
    pin_boss = st.text_input("PIN Maestro", type="password")
    if pin_boss == PINS["Admin"]:
        st.info("Herramienta para borrar registros por fecha.")
        emp_b = st.selectbox("Empleado", ["Luis", "Melvin", "Edwin"], key="adm_n")
        f_b = st.date_input("Fecha", key="adm_f")
        if st.button("BORRAR REGISTRO SELECCIONADO"):
            c.execute("DELETE FROM registros WHERE nombre=? AND fecha=?", (emp_b, f_b.strftime('%Y-%m-%d')))
            conn.commit()
            st.success("Registro borrado.")
            st.rerun()
