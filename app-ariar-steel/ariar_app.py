import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Ariar Steel LLC", layout="centered")

st.title("🚜 Registro de Jornada")
st.write("Ingresa tus horas de trabajo a continuación:")

try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    
    with st.form(key="registro"):
        empleado = st.selectbox("Empleado", ["Edwin Lopez", "Alexandra", "Personal de Campo"])
        fecha = st.date_input("Fecha")
        horas = st.number_input("Horas", min_value=0.0, step=0.5)
        notas = st.text_area("Notas")
        
        boton = st.form_submit_button("Guardar Registro")
        
        if boton:
            nuevo = pd.DataFrame([{"Empleado": empleado, "Fecha": str(fecha), "Horas": horas, "Notas": notas}])
            actual = conn.read()
            df_final = pd.concat([actual, nuevo], ignore_index=True)
            conn.update(data=df_final)
            st.success(f"✅ ¡Guardado para {empleado}!")
except Exception as e:
    st.error(f"Error: {e}")
