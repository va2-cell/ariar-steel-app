import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. Configuración de la pestaña y el Panel
st.set_page_config(
    page_title="Ariar Steel LLC - Panel de Control",
    page_icon="🏗️",
    layout="wide"
)

# 2. Estilos para que se vea profesional (Azul Ariar)
st.markdown("""
<style>
    .main-title {
        color: #1E4D8C;
        font-family: 'Arial Black', sans-serif;
        font-size: 35px;
        text-align: center;
        margin-top: -50px;
    }
    .sidebar-text {
        font-weight: bold;
        color: #1E4D8C;
    }
    div.stButton > button {
        background-color: #1E4D8C;
        color: white;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# 3. Barra Lateral con el Logo y el Menú
with st.sidebar:
    # Aquí va el logo azul de Ariar
    st.image("https://raw.githubusercontent.com/EdwinLopez22/Ariar-Steel-App/main/logo_ariar.png", use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #1E4D8C;'>PANEL ARIAR STEEL</h2>", unsafe_allow_html=True)
    st.write("---")
    
    opcion = st.radio(
        "SELECCIONE UNA OPCIÓN:",
        ["🚜 Registro de Horas", "📊 Ver Reportes", "🛠️ Configuración"]
    )
    st.write("---")
    st.info("Usuario: Administrador")

# 4. Título en el Panel Principal
st.markdown("<div class='main-title'>PANEL DE CONTROL - ARIAR STEEL LLC</div>", unsafe_allow_html=True)
st.write("---")

# 5. Conexión a la base de datos de Google Sheets
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    
    if opcion == "🚜 Registro de Horas":
        st.subheader("Ingreso de Jornada Laboral")
        
        with st.form(key="form_registro"):
            col1, col2 = st.columns(2)
            with col1:
                empleado = st.selectbox("Nombre del Empleado", ["Edwin Lopez", "Alexandra", "Personal de Campo"])
                fecha = st.date_input("Fecha de Trabajo")
            with col2:
                horas = st.number_input("Horas Trabajadas", min_value=0.0, max_value=24.0, step=0.5)
                # Puedes agregar el campo 'Lugar de trabajo' si lo necesitas
            
            notas = st.text_area("Notas o descripción de la tarea")
            
            boton_enviar = st.form_submit_button("GUARDAR EN EL PANEL")
            
            if boton_enviar:
                # Crear la fila para el Excel
                nuevo_dato = pd.DataFrame([{
                    "Empleado": empleado,
                    "Fecha": str(fecha),
                    "Horas": horas,
                    "Notas": notas
                }])
                
                # Leer datos actuales y guardar
                datos_existentes = conn.read()
                df_final = pd.concat([datos_existentes, nuevo_dato], ignore_index=True)
                conn.update(data=df_final)
                
                st.success(f"✅ ¡Datos guardados correctamente para {empleado}!")

    elif opcion == "📊 Ver Reportes":
        st.subheader("Historial de Registros")
        df = conn.read()
        st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error("⚠️ Error de conexión: Revisa si los 'Secrets' están pegados en Streamlit Cloud.")
    st.info("Si la app carga pero no guarda, es porque falta la clave del Excel en la configuración.")
