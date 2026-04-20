import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Ariar Steel", page_icon="🏗️", layout="wide")

# 2. LISTA DE EMPLEADOS (Actualízala con los nombres reales)
lista_empleados = [
    "Seleccionar...", 
    "Edwin", 
    "Luis", 
    "Alexandra", 
    "Juan", 
    "Pedro", 
    "Jose"
]

# 3. Menú Lateral
with st.sidebar:
    st.image("https://static.wixstatic.com/media/9a448a_d799fb6afe434c0697f3eebec29c01ed~mv2.png/v1/fill/w_219,h_154,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/%234%20(1).png", width=150)
    st.title("Panel Ariar Steel")
    st.markdown("---")
    
    # Opciones que todos ven
    menu_opciones = ["Inicio", "Mis Horas", "Chat de Equipo"]
    
    st.markdown("### 🔐 Acceso Admin")
    password = st.text_input("Clave para administradores", type="password")
    
    # Solo si ponen la clave correcta aparece el panel de control
    es_admin = False
    if password == "ariar2026":
        menu_opciones.append("⚙️ Panel de Control")
        es_admin = True
        st.success("Modo Admin Activo")
    
    st.markdown("---")
    opcion = st.radio("Navegación:", menu_opciones)

# 4. Lógica de Contenido
if opcion == "Inicio":
    st.title("🏗️ Ariar Steel: Control de Obra")
    st.subheader("Bienvenido al sistema oficial de registro")
    st.info("Para revisar tus horas, selecciona 'Mis Horas' en el menú de la izquierda.")
    st.write("---")
    st.caption("Calidad y Resistencia en cada varilla.")

elif opcion == "Mis Horas":
    st.title("⏱️ Consulta de mis Horas")
    st.write("Busca tu nombre para ver cuánto tiempo has trabajado esta semana.")
    
    nombre_usuario = st.selectbox("Selecciona tu nombre:", lista_empleados)
    
    if nombre_usuario != "Seleccionar...":
        st.write(f"### Reporte para: {nombre_usuario}")
        # Aquí es donde se mostrarán los datos del Excel después
        st.warning(f"Hola {nombre_usuario}, tus horas de esta semana se están procesando. Vuelve a consultar más tarde.")
        
        # Simulación de visualización
        col1, col2 = st.columns(2)
        col1.metric("Horas Totales", "0.0 hrs")
        col2.metric("Días Trabajados", "0")

elif opcion == "⚙️ Panel de Control":
    st.title("⚙️ Registro de Jornada (Solo Administradores)")
    
    with st.form("registro_admin", clear_on_submit=True):
        st.write("Completa los datos para guardar las horas del empleado.")
        col1, col2 = st.columns(2)
        with col1:
            emp = st.selectbox("Empleado", lista_empleados)
            fecha = st.date_input("Fecha")
        with col2:
            hrs = st.number_input("Horas", min_value=0.0, max_value=24.0, step=0.5)
            nota = st.text_input("Comentarios")
            
        if st.form_submit_button("✅ Guardar en Registro"):
            if emp == "Seleccionar...":
                st.error("Selecciona un empleado válido.")
            else:
                st.success(f"¡Hecho! Se han anotado {hrs} horas para {emp}.")
                st.balloons()

elif opcion == "Chat de Equipo":
    st.title("💬 Chat de Equipo")
    st.write("Anuncios importantes para todo el personal de Ariar Steel.")