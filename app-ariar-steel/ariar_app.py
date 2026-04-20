import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Ariar Steel", page_icon="🏗️", layout="wide")

# EL LINK DE TU HOJA (Copiado de tu mensaje anterior)
URL_HOJA = "https://docs.google.com/spreadsheets/d/1cPGCPPii_snTkllJP1XmYtG27U8y2oLdvdV5H086jDg/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

lista_empleados = ["Seleccionar...", "Edwin", "Luis", "Alexandra", "Juan", "Pedro", "Jose"]

with st.sidebar:
    st.image("https://static.wixstatic.com/media/9a448a_d799fb6afe434c0697f3eebec29c01ed~mv2.png/v1/fill/w_219,h_154,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/%234%20(1).png", width=150)
    st.title("Panel Ariar Steel")
    menu_opciones = ["Inicio", "Mis Horas"]
    
    password = st.text_input("Clave Admin", type="password")
    if password == "ariar2026":
        menu_opciones.append("⚙️ Registro")
    opcion = st.radio("Ir a:", menu_opciones)

if opcion == "⚙️ Registro":
    st.title("⚙️ Registro de Jornada")
    with st.form("nuevo_registro", clear_on_submit=True):
        emp = st.selectbox("Empleado", lista_empleados)
        fecha = st.date_input("Fecha")
        hrs = st.number_input("Horas", min_value=0.0, step=0.5)
        nota = st.text_input("Notas")
        
        if st.form_submit_button("✅ Guardar"):
            if emp != "Seleccionar...":
                nueva_fila = pd.DataFrame([{"Fecha": str(fecha), "Empleado": emp, "Horas": hrs, "Notas": nota}])
                try:
                    # El ttl=0 es la clave para que no use la memoria vieja con error
                    df_actual = conn.read(spreadsheet=URL_HOJA, ttl=0)
                    df_final = pd.concat([df_actual, nueva_fila], ignore_index=True)
                    conn.update(spreadsheet=URL_HOJA, data=df_final)
                    st.success("¡Guardado!")
                    st.balloons()
                except Exception as e:
                    st.error(f"Error: {e}")