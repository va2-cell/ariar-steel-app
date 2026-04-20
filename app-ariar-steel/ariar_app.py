import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Ariar Steel Admin", page_icon="🏗️", layout="wide")

# 2. LISTA MAESTRA DE EMPLEADOS (Aquí puedes agregar más nombres)
lista_empleados = [
    "Seleccionar...", 
    "Edwin A lopez ", 
    "Luis Alfaro", 
    "alejandro", 
    "flavio avilez", 
    "Pedro ramos ", 
    "Jose perez "
]

# 3. Menú Lateral
with st.sidebar:
    st.image("https://static.wixstatic.com/media/9a448a_d799fb6afe434c0697f3eebec29c01ed~mv2.png/v1/fill/w_219,h_154,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/%234%20(1).png", width=150)
    st.title("Panel Ariar Steel")
    st.markdown("---")
    
    menu_opciones = ["Inicio", "Chat de Equipo", "Mis Horas"]
    
    st.markdown("### 🔐 Administradores")
    password = st.text_input("Clave de acceso", type="password")
    
    if password == "ariar2026":
        menu_opciones.append("⚙️ Panel de Control")
        st.success("Acceso Admin")
    
    st.markdown("---")
    opcion = st.radio("Ir a:", menu_opciones, key="menu_principal")

# 4. Lógica de Contenido
if opcion == "Inicio":
    st.title("🏗️ Ariar Steel: Control de Obra")
    st.info("Sistema de gestión de personal y tiempos.")
    st.write("Bienvenido. Usa el menú lateral para navegar.")

elif opcion == "Mis Horas":
    st.title("⏱️ Consulta de Horas")
    # Usamos la lista de empleados aquí también
    empleado_consulta = st.selectbox("Busca tu nombre para ver tus horas:", lista_empleados)
    if empleado_consulta != "Seleccionar...":
        st.warning(f"Todavía no hay horas registradas para {empleado_consulta} esta semana.")

elif opcion == "⚙️ Panel de Control":
    st.title("⚙️ Registro de Jornada")
    st.subheader("Ingresa las horas trabajadas hoy")
    
    with st.form("registro_admin", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            emp = st.selectbox("Selecciona al Trabajador", lista_empleados)
            fecha = st.date_input("Fecha de trabajo")
            
        with col2:
            hrs = st.number_input("Horas Totales", min_value=0.0, max_value=24.0, step=0.5)
            nota = st.text_input("Nota (ej. 'Overtime', 'Llegó tarde')")
            
        enviar = st.form_submit_button("✅ Guardar Horas")
        
        if enviar:
            if emp == "Seleccionar...":
                st.error("Por favor selecciona un nombre válido.")
            else:
                # Esto es lo que conectaremos al Excel después
                st.balloons()
                st.success(f"Registradas {hrs} horas para {emp} el día {fecha}")

elif opcion == "Chat de Equipo":
    st.title("💬 Chat de Equipo")
    st.write("Sección de avisos generales.")