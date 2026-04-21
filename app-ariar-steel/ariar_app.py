import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime, time

# Configuración de página optimizada para celular
st.set_page_config(page_title="Ariar Steel LLC", page_icon="🏗️", layout="centered")

# Conexión a la base de datos
conn = sqlite3.connect('ariar_horas.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS registros (fecha TEXT, nombre TEXT, horas REAL, notas TEXT)')
conn.commit()

# Configuración de seguridad
PINS = {"Luis": "8349", "Melvin": "9064", "Edwin": "3909", "Admin": "2222"}
EMPLEADOS = ["Luis", "Melvin", "Edwin"]

st.title("🏗️ Ariar Steel LLC")

# Menú lateral limpio
st.sidebar.header("Panel de Control")
choice = st.sidebar.selectbox("Menú", ["Registrar Horas (Admin)", "Ver Mis Horas (Trabajador)"])

if choice == "Registrar Horas (Admin)":
    st.subheader("📝 Registro de Jornada")
    pin_admin = st.text_input("PIN de Administrador", type="password", key="admin_pin")
    
    if pin_admin == PINS["Admin"]:
        st.success("🔓 Acceso concedido")
        with st.form("registro_form", clear_on_submit=True):
            fecha = st.date_input("Fecha", datetime.now())
            nombre = st.selectbox("Empleado", EMPLEADOS)
            col1, col2 = st.columns(2)
            with col1:
                h_entrada = st.time_input("Hora de Entrada", time(7, 0))
            with col2:
                h_salida = st.time_input("Hora de Salida", time(17, 0))
            
            lonche = st.selectbox("Tiempo de lonche (horas)", [0.5, 1.0, 0.0], index=0)
            notas = st.text_area("Notas (Opcional)")
            
            submit = st.form_submit_button("✅ Guardar Registro")
            
            if submit:
                t1, t2 = datetime.combine(fecha, h_entrada), datetime.combine(fecha, h_salida)
                segundos = (t2 - t1).total_seconds()
                horas_c = (segundos / 3600) - lonche
                
                if horas_c <= 0:
                    st.error("⚠️ Error: La hora de salida debe ser después de la entrada.")
                else:
                    c.execute("INSERT INTO registros VALUES (?,?,?,?)", (fecha.strftime('%Y-%m-%d'), nombre, horas_c, notas))
                    conn.commit()
                    st.success(f"¡Hecho! Se registraron {horas_c} horas para {nombre}.")
    elif pin_admin != "":
        st.error("❌ PIN Incorrecto")

else:
    st.subheader("🕒 Reporte Personal")
    nombre_emp = st.selectbox("Selecciona tu nombre", EMPLEADOS)
    pin_emp = st.text_input("Ingresa tu PIN personal", type="password", key="emp_pin")
    
    if st.button("Ver mi reporte"):
        if nombre_emp in PINS and pin_emp == PINS[nombre_emp]:
            query = f"SELECT fecha, horas, notas FROM registros WHERE nombre='{nombre_emp}' ORDER BY fecha DESC"
            df = pd.read_sql_query(query, conn)
            if not df.empty:
                df['fecha'] = pd.to_datetime(df['fecha']).dt.strftime('%A %m-%d-%Y')
                st.table(df)
                st.info(f"📊 Total acumulado: {df['horas'].sum()} horas")
            else:
                st.warning("No tienes registros guardados aún.")
        elif pin_emp != "":
            st.error("❌ PIN incorrecto.")

# --- SECCIÓN MAESTRA (PARA BORRAR ERRORES) ---
st.sidebar.markdown("---")
if st.sidebar.checkbox("⚙️ Acceso Administrador Maestro"):
    pin_boss = st.sidebar.text_input("PIN de Seguridad", type="password", key="boss_pin")
    if pin_boss == PINS["Admin"]:
        st.sidebar.warning("ZONA DE BORRADO")
        emp_b = st.sidebar.selectbox("Empleado a corregir", EMPLEADOS)
        f_b = st.sidebar.date_input("Fecha a eliminar")
        
        if st.sidebar.button("🗑️ ELIMINAR REGISTRO"):
            c.execute("DELETE FROM registros WHERE nombre=? AND fecha=?", (emp_b, f_b.strftime('%Y-%m-%d')))
            conn.commit()
            st.sidebar.success(f"Registro de {emp_b} del {f_b} borrado.")
            st.rerun()