import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. Configuración de la página
st.set_page_config(
    page_title="Ariar Steel", 
    page_icon="https://static.wixstatic.com/media/9a448a_d799fb6afe434c0697f3eebec29c01ed~mv2.png/v1/fill/w_32,h_32,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/%234%20(1).png", 
    layout="wide"
)

# 2. Enlace de tu Google Sheet
# Ya incluí tu link aquí
URL_HOJA = "https://docs.google.com/spreadsheets/d/1cPGCPPii_snTkllJP1XmYtG27U8y2oLdvdV5H086jDg/edit?usp=sharing"

# Conexión técnica
conn = st.connection("gsheets", type=GSheetsConnection)

# 3. Lista de empleados
lista_empleados = ["Seleccionar...", "Edwin", "Luis", "Alexandra", "Juan", "Pedro", "Jose"]

# 4. Menú Lateral
with st.sidebar:
    st.image("https://static.wixstatic.com/media/9a448a_d799fb6afe434c0697f3eebec29c01ed~mv2.png/v1/fill/w_219,h_154,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/%234%20(1).png", width=150)
    st.title("Panel Ariar Steel")
    menu_opciones = ["Inicio", "Mis Horas"]
    
    st.markdown("---")
    password = st.text_input("Clave de Administrador", type="password")
    es_admin = False
    if password == "ariar2026":
        menu_opciones.append("⚙️ Registro de Horas")
        es_admin = True
    
    opcion = st.radio("Ir a:", menu_opciones)

# 5. Lógica de Contenido
if opcion == "Inicio":
    st.title("🏗️ Bienvenido a Ariar Steel")
    st.subheader("Sistema de control de jornada")
    st.write("Selecciona una opción en el menú de la izquierda para comenzar.")
    st.info("Nota: Las horas registradas se guardan automáticamente en la base de datos central.")

elif opcion == "Mis Horas":
    st.title("⏱️ Consulta de Horas")
    nombre_busqueda = st.selectbox("Busca tu nombre para ver tus horas:", lista_empleados)
    
    if nombre_busqueda != "Seleccionar...":
        try:
            # Leer los datos actuales
            df = conn.read(spreadsheet=URL_HOJA)
            # Filtrar por el nombre seleccionado
            mis_datos = df[df["Empleado"] == nombre_busqueda]
            
            if not mis_datos.empty:
                st.write(f"### Reporte para: {nombre_busqueda}")
                st.dataframe(mis_datos, use_container_width=True)
                
                # Cálculos rápidos
                total_horas = mis_datos["Horas"].astype(float).sum()
                st.metric("Total de Horas Acumuladas", f"{total_horas} hrs")
            else:
                st.warning("Aún no tienes horas registradas en el sistema.")
        except:
            st.error("No se pudo conectar con la base de datos. Verifica la conexión.")

elif opcion == "⚙️ Registro de Horas":
    st.title("⚙️ Panel Administrativo")
    st.write("Usa este formulario para anotar las horas de los empleados.")
    
    with st.form("registro_nuevo", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            emp = st.selectbox("Selecciona Empleado", lista_empleados)
            fecha = st.date_input("Fecha de Trabajo")
        with col2:
            horas = st.number_input("Cantidad de Horas", min_value=0.0, step=0.5)
            comentario = st.text_input("Nota o Ubicación de Obra")
        
        btn_guardar = st.form_submit_button("✅ Guardar en Base de Datos")
        
        if btn_guardar:
            if emp == "Seleccionar...":
                st.error("Por favor, selecciona un nombre de la lista.")
            else:
                # Preparar la nueva fila
                nueva_data = pd.DataFrame([{
                    "Fecha": str(fecha),
                    "Empleado": emp,
                    "Horas": horas,
                    "Notas": comentario
                }])
                
                try:
                    # Leer lo que ya existe
                    existente = conn.read(spreadsheet=URL_HOJA)
                    # Combinar y actualizar
                    actualizado = pd.concat([existente, nueva_data], ignore_index=True)
                    conn.update(spreadsheet=URL_HOJA, data=actualizado)
                    st.success(f"¡Listo! Se han guardado {horas} horas para {emp}.")
                    st.balloons()
                except Exception as e:
                    st.error("Hubo un problema al guardar. Asegúrate de que el Excel tenga los títulos correctos.")