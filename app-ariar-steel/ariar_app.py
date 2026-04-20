import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Ariar Steel Admin", page_icon="🏗️", layout="wide")

# 2. Menú Lateral
with st.sidebar:
    st.image("https://static.wixstatic.com/media/9a448a_d799fb6afe434c0697f3eebec29c01ed~mv2.png/v1/fill/w_219,h_154,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/%234%20(1).png", width=150)
    st.title("Panel Ariar Steel")
    st.markdown("---")
    
    # Lista de opciones normal
    menu_opciones = ["Inicio", "Chat de Equipo", "Mis Horas"]
    
    # SECCIÓN DE ADMIN
    st.markdown("### 🔐 Administradores")
    password = st.text_input("Clave de acceso", type="password")
    
    # Si la clave es correcta, añadimos opciones de administrador
    # Cambia 'ariar2026' por la clave que tú quieras
    if password == "ariar2026":
        menu_opciones.append("⚙️ Panel de Control")
        st.success("Acceso Admin Concedido")
    
    st.markdown("---")
    opcion = st.radio("Ir a:", menu_opciones, key="menu_principal")

# 3. Lógica de Contenido
if opcion == "Inicio":
    st.title("🏗️ Ariar Steel: Control de Obra")
    st.subheader("Bienvenido al sistema oficial")
    st.info("Selecciona una opción en el menú de la izquierda para comenzar.")
    st.write("---")
    st.caption("Calidad y Resistencia en cada varilla.")

elif opcion == "Mis Horas":
    st.title("⏱️ Consulta de Horas")
    nombre = st.selectbox("Busca tu nombre:", ["Seleccionar...", "Luis", "Alexandra", "Edwin"])
    if nombre != "Seleccionar...":
        st.write(f"Mostrando registro para: **{nombre}**")
        st.info("No hay horas registradas para esta semana todavía.")

elif opcion == "⚙️ Panel de Control":
    st.title("⚙️ Panel de Administración")
    st.subheader("Registrar nuevas horas")
    
    # Formulario para que el admin meta datos
    with st.form("registro_horas"):
        empleado = st.selectbox("Empleado", ["Luis", "Alexandra", "Edwin"])
        fecha = st.date_input("Fecha")
        horas = st.number_input("Cantidad de horas", min_value=0, max_value=24, step=1)
        comentario = st.text_input("Notas (opcional)")
        
        enviar = st.form_submit_button("Guardar Registro")
        if enviar:
            st.success(f"Horas de {empleado} guardadas correctamente (Simulación)")

elif opcion == "Chat de Equipo":
    st.title("💬 Chat de Equipo")
    st.write("Próximamente: Sistema de mensajería interna.")