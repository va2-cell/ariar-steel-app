import streamlit as st

# Configuración de la App
st.set_page_config(page_title="Ariar Steel App", page_icon="🏗️")

# --- MENÚ LATERAL ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4342/4342728.png", width=100) # Un icono de construcción
st.sidebar.title("Panel Ariar Steel")
opcion = st.sidebar.radio("Ir a:", ["Inicio", "Chat de Equipo", "Mis Horas", "Reporte Semanal"])

# --- SECCIÓN: INICIO ---
if opcion == "Inicio":
    st.title("🏗️ Ariar Steel: Control de Obra")
    st.write("Bienvenido al sistema oficial de Ariar Steel.")
    st.info("Desde aquí puedes reportar tus horas y comunicarte con el equipo.")

# --- SECCIÓN: CHAT DE EQUIPO ---
elif opcion == "Chat de Equipo":
    st.header("💬 Mensajería de Empleados")
    
    if "chat_ariar" not in st.session_state:
        st.session_state.chat_ariar = []

    # Mostrar mensajes
    for m in st.session_state.chat_ariar:
        with st.chat_message(m["usuario"]):
            st.write(f"**{m['usuario']}**: {m['texto']}")

    # Entrada de mensaje
    if prompt := st.chat_input("Escribe un mensaje al grupo..."):
        st.session_state.chat_ariar.append({"usuario": "Edwin", "texto": prompt})
        st.rerun()

# --- SECCIÓN: MIS HORAS ---
elif opcion == "Mis Horas":
    st.header("⏱️ Registro de Jornada")
    
    with st.form("form_horas"):
        nombre_emp = st.text_input("Nombre del Empleado")
        fecha_trabajo = st.date_input("Fecha de hoy")
        horas_t = st.number_input("Total de horas trabajadas", min_value=0.0, max_value=24.0, step=0.5)
        notas = st.text_area("¿Qué trabajo hiciste hoy? (Varilla, Concreto, etc.)")
        
        boton = st.form_submit_button("Guardar Horas")
        
        if boton:
            st.success(f"Horas de {nombre_emp} guardadas correctamente.")
            # Aquí luego conectaremos el Excel para que no se borren

# --- SECCIÓN: REPORTE (Solo para ti) ---
elif opcion == "Reporte Semanal":
    st.header("📊 Resumen de Nómina")
    st.write("Aquí verás cuánto le toca a cada quién el fin de semana.")
    st.warning("Sección protegida para el administrador.")
import streamlit as st

# Configuración de la App
st.set_page_config(page_title="Ariar Steel App", page_icon="🏗️")

# --- MENÚ LATERAL ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4342/4342728.png", width=100) # Un icono de construcción
st.sidebar.title("Panel Ariar Steel")
opcion = st.sidebar.radio("Ir a:", ["Inicio", "Chat de Equipo", "Mis Horas", "Reporte Semanal"])

# --- SECCIÓN: INICIO ---
if opcion == "Inicio":
    st.title("🏗️ Ariar Steel: Control de Obra")
    st.write("Bienvenido al sistema oficial de Ariar Steel.")
    st.info("Desde aquí puedes reportar tus horas y comunicarte con el equipo.")

# --- SECCIÓN: CHAT DE EQUIPO ---
elif opcion == "Chat de Equipo":
    st.header("💬 Mensajería de Empleados")
    
    if "chat_ariar" not in st.session_state:
        st.session_state.chat_ariar = []

    # Mostrar mensajes
    for m in st.session_state.chat_ariar:
        with st.chat_message(m["usuario"]):
            st.write(f"**{m['usuario']}**: {m['texto']}")

    # Entrada de mensaje
    if prompt := st.chat_input("Escribe un mensaje al grupo..."):
        st.session_state.chat_ariar.append({"usuario": "Edwin", "texto": prompt})
        st.rerun()

# --- SECCIÓN: MIS HORAS ---
elif opcion == "Mis Horas":
    st.header("⏱️ Registro de Jornada")
    
    with st.form("form_horas"):
        nombre_emp = st.text_input("Nombre del Empleado")
        fecha_trabajo = st.date_input("Fecha de hoy")
        horas_t = st.number_input("Total de horas trabajadas", min_value=0.0, max_value=24.0, step=0.5)
        notas = st.text_area("¿Qué trabajo hiciste hoy? (Varilla, Concreto, etc.)")
        
        boton = st.form_submit_button("Guardar Horas")
        
        if boton:
            st.success(f"Horas de {nombre_emp} guardadas correctamente.")
            # Aquí luego conectaremos el Excel para que no se borren

# --- SECCIÓN: REPORTE (Solo para ti) ---
elif opcion == "Reporte Semanal":
    st.header("📊 Resumen de Nómina")
    st.write("Aquí verás cuánto le toca a cada quién el fin de semana.")
    st.warning("Sección protegida para el administrador.")
