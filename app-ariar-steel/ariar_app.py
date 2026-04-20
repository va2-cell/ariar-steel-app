import streamlit as st

# 1. Configuración de la página con logo
st.set_page_config(
    page_title="Ariar Steel", 
    page_icon="https://static.wixstatic.com/media/9a448a_d799fb6afe434c0697f3eebec29c01ed~mv2.png/v1/fill/w_32,h_32,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/%234%20(1).png", 
    layout="wide"
)

# 2. Lista de empleados
lista_empleados = ["Seleccionar...", "Edwin", "Luis", "Alexandra", "Juan", "Pedro", "Jose"]

# 3. Menú Lateral
with st.sidebar:
    st.image("https://static.wixstatic.com/media/9a448a_d799fb6afe434c0697f3eebec29c01ed~mv2.png/v1/fill/w_219,h_154,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/%234%20(1).png", width=150)
    st.title("Panel Ariar Steel")
    menu_opciones = ["Inicio", "Mis Horas", "Chat de Equipo"]
    
    password = st.text_input("Clave Admin", type="password")
    if password == "ariar2026":
        menu_opciones.append("⚙️ Panel de Control")
    
    opcion = st.radio("Navegación:", menu_opciones)

# 4. Contenido
if opcion == "Inicio":
    st.title("🏗️ Ariar Steel")
    st.info("Sistema oficial de registro.")
elif opcion == "Mis Horas":
    st.title("⏱️ Mis Horas")
    st.selectbox("Selecciona tu nombre:", lista_empleados)
elif opcion == "⚙️ Panel de Control":
    st.title("⚙️ Panel Admin")
    st.write("Registra las horas aquí.")
elif opcion == "Chat de Equipo":
    st.title("💬 Chat de Equipo")