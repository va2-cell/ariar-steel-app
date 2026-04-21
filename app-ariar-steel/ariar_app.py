import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime, time

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
            
            st.markdown("---")
            st.subheader("Cálculo de Horas")
            h_entrada = st.time_input("Hora de Entrada", time(7, 0))
            h_salida = st.time_input("Hora de Salida", time(17, 0))
            lonche = st.selectbox("Tiempo de lonche (horas)", [0.5, 1.0, 0.0], index=0)
            
            notas = st.text_area("Notas (Opcional)")
            enviar = st.form_submit_button("Guardar Registro")
            
            if enviar:
                # Lógica de cálculo
                t1 = datetime.combine(fecha, h_entrada)
                t2 = datetime.combine(fecha, h_salida)
                diff = (t2 - t1).total_seconds() / 3600
                horas_calculadas = diff - lonche
                
                if horas_calculadas <= 0:
                    st.error("Error: La hora de salida debe ser mayor a la de entrada.")
                else:
                    c.execute("INSERT INTO registros VALUES (?,?,?,?)", 
                              (fecha.strftime('%Y-%m-%d'), nombre, horas_calculadas, notas))
                    conn.commit()
                    st.success(f"Registradas {horas_calculadas} horas para {nombre} (Menos {lonche} de lonche)")

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
                
                # --- NUEVO: FORMATEAR FECHA CON DÍA DE LA SEMANA ---
                df['fecha'] = pd.to_datetime(df['fecha'])
                df['fecha'] = df['fecha'].dt.strftime('%A %m-%d-%Y')
                
                st.table(df)
                st.info(f"Total acumulado: {df['horas'].sum()} horas")
                
                # --- NUEVO: BOTÓN PARA BORRAR REGISTROS DE HOY ---
                st.markdown("---")
                st.subheader("¿Cometiste un error?")
                if st.button("Eliminar mis registros de hoy"):
                    hoy = datetime.now().strftime('%Y-%m-%d')
                    c.execute("DELETE FROM registros WHERE nombre=? AND fecha=?", (nombre_emp, hoy))
                    conn.commit()
                    st.warning("Registros de hoy eliminados. Recarga el reporte.")
            else:
                st.warning("Aún no tienes horas registradas.")
        elif pin_emp != "":
            st.error("PIN incorrecto para este usuario.")