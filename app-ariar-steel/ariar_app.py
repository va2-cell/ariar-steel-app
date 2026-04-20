import streamlit as st

# 1. Configuración de la página (Icono y Título en la pestaña del navegador)
st.set_page_config(page_title="Ariar Steel", page_icon="🏗️", layout="wide")

# 2. Menú Lateral
with st.sidebar:
    # LOGO: Puedes cambiar este link por el de tu logo real más adelante
    st.image("https://cdn-icons-png.flaticon.com/512/4342/4342728.png", width=120)
    st.title("Panel Ariar Steel")
    st.markdown("---") # Una línea divisora
    
    opcion = st.radio(
        "Ir a:", 
        ["Inicio", "Chat de Equipo", "Mis Horas", "Reporte Semanal"],
        key="menu_principal"
    )

# 3. Lógica de Contenido (Lo que se ve en el centro)
if opcion == "Inicio":
    st.title("🏗️ Ariar Steel: Control de Obra")
    st.subheader("Bienvenido al sistema oficial")
    
    # Un cuadro informativo nítido
    st.info("Selecciona una opción en el menú de la izquierda para comenzar.")
    
    # Puedes poner una imagen de fondo o de la obra aquí
    st.image("https://images.unsplash.com/photo-1541888946425-d81bb19480c5?auto=format&fit=crop&q=80&w=1000", caption="Calidad y Resistencia en cada varilla.")

elif opcion == "Chat de Equipo":
    st.title("💬 Chat de Equipo")
    st.write("Próximamente: Sistema de mensajería interna.")

elif opcion == "Mis Horas":
    st.title("⏱️ Registro de Horas")
    st.write("Sección para consulta de horas trabajadas.")

elif opcion == "Reporte Semanal":
    st.title("📊 Reporte Semanal")
    st.write("Resumen de avance de obra.")