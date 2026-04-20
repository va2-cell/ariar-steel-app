import streamlit as st

# 1. Configuración de la página (Icono y Título en la pestaña del navegador)
st.set_page_config(page_title="Ariar Steel", page_icon="🏗️", layout="wide")
# 2. Menú Lateral
with st.sidebar:
    # TU LOGO REAL
    st.image("https://static.wixstatic.com/media/9a448a_d799fb6afe434c0697f3eebec29c01ed~mv2.png/v1/fill/w_219,h_154,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/%234%20(1).png", width=150)
    st.title("Panel Ariar Steel")
    st.markdown("---")
    
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