import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Mi experiencia aprendiendo a programar",
    layout="centered"
)

# CSS personalizado para mejorar el estilo del sidebar
st.markdown("""
    <style>
        /* Estilo general del sidebar */
        [data-testid="stSidebar"] {
            background-color: #2b3e50; /* Fondo oscuro */
            padding: 20px;
        }
        
        /* Título del sidebar */
        .css-1lcbmhc {
            color: #f0f0f0 !important; /* Color claro para el texto */
            font-size: 22px !important;
            text-align: center;
            font-weight: bold;
            margin-bottom: 20px;
        }

        /* Radio buttons del sidebar */
        .css-1inwz65, .css-16huue1 {
            font-size: 18px !important;
            color: #ffffff !important; /* Texto blanco */
        }

        /* Espaciado entre radio buttons */
        .css-1inwz65 {
            margin: 10px 0 !important;
        }

        /* Hover para los radio buttons */
        .css-1inwz65:hover {
            background-color: #f63366; /* Resalta al pasar el mouse */
            border-radius: 5px;
            color: white !important;
        }

        /* Pie de página del sidebar */
        .css-qri22k {
            margin-top: 20px;
            color: #ffffff !important; 
            font-size: 14px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar para la navegación
st.sidebar.title("APRENDIENDO A PROGRAMAR")
opcion = st.sidebar.radio(
    "Selecciona una categoría:",
    (
        "👩 SOBRE MI", #Icono de mujer
        "📘 MI EXPERIENCIA",  # Icono de libro
        "⚙️ RETOS",           # Icono de engranaje
        "🌟 APRENDIZAJE CLAVE",  # Icono de estrella
        "💡 CONSEJOS"          # Icono de bombilla
    )
)

# Contenido para cada categoría
if opcion == "👩 SOBRE MI":
    st.title("👩 Sobre mí")
    
    # Línea decorativa debajo del título
    st.markdown("""
        <hr style="border: none; height: 2px; margin-top: -5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);">
    """, unsafe_allow_html=True)

    # Crear columnas
    col1, col2 = st.columns([1, 2])  # Ajusta la proporción de ancho (1:2, 2:1, etc.)
    
    # Imagen en una columna
    with col1:
        st.image(
            "imagenes/perfil.jpeg", 
            caption="Estudiante de la carrera de Publicidad", 
            use_container_width=True  # Nuevo parámetro
        )
    
    # Texto en otra columna
    with col2:
        st.write("""Desde la edición de videos hasta la creación de campañas publicitarias, 
                mi pasión por contar historias visuales me ha llevado a explorar el fascinante 
                mundo de la Publicidad. Actualmente curso dicha carrera, en la cual he 
                desarrollado habilidades creativas y técnicas para comunicar ideas de manera 
                impactante. La fotografía y la edición son mis herramientas favoritas para plasmar 
                conceptos únicos, y estoy convencida de que la creatividad es la clave para conectar 
                personas y marcas de forma auténtica.""")
        st.write("😄" "Nombre: Gemma Haruko Soriano Vergara")
        st.write("🎓" "Centro de Estudio: Pontificia Universidad Católica del Perú")
        st.write("📚" "Intereses: Edición de videos, Fotografía, Dormir")

    
    st.title("🤹‍♀️Mis habilidades")
    # Línea decorativa debajo del título
    st.markdown("""
        <hr style="border: none; height: 2px; margin-top: -5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);">
    """, unsafe_allow_html=True)

    # Lista de habilidades
    skills = [
        "Autónoma", "Flexible", "Resiliente", "Comunicadora", "Líder", "Creativa",
        "Empática", "Crítica", "Gestora", "Eficiente", "Mediadora", 
    ]

    # Crear 4 columnas
    cols = st.columns(4)

    # Asignar botones a las columnas
    for i, skill in enumerate(skills):
        col_index = i % 4  # Determina la columna
        with cols[col_index]:
            if st.button(skill):
                st.write(f"You clicked on {skill}!")
    
    st.title("💼 Aspecto laboral")
    
    # Línea decorativa debajo del título
    st.markdown("""
        <hr style="border: none; height: 2px; margin-top: -5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);">
    """, unsafe_allow_html=True)

    st.write("""
    Si bien aún no he comenzado mis prácticas profesionales en el ámbito publicitario, 
    he adquirido experiencia creando contenido relacionado con mi carrera. He desarrollado 
    posts publicitarios, ediciones creativas y materiales visuales tanto para la academia de 
    mi papá como para pequeños emprendimientos de personas que confiaron en mi trabajo. Estas 
    experiencias me han permitido aplicar mis conocimientos de publicidad de manera práctica y 
    desarrollar mi creatividad en proyectos reales.""")

    st.write("👀 Linkedin: https://pe.linkedin.com/in/gemma-haruko-soriano-vergara-4888572ba")


elif opcion == "📘 MI EXPERIENCIA":
    st.title("📘 Mi Experiencia")
    # Línea decorativa debajo del título
    st.markdown("""
        <hr style="border: none; height: 2px; margin-top: -5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);">
    """, unsafe_allow_html=True)

    # Texto descriptivo
    st.write("""
    Mi experiencia en programación comenzó desde cero, sin conocimientos previos de programación. 
    Empecé aprendiendo los fundamentos de Python, un lenguaje que me cautivó por su simplicidad y versatilidad. 
    A lo largo de mi aprendizaje, me he enfrentado a desafíos, pero también he experimentado momentos de gran satisfacción, como cuando 
    logré crear mi primer programa funcional o cuando entendí cómo las funciones y las clases interactúan para construir proyectos 
    más complejos. Luego, descubrí Streamlit, una herramienta que me permitió llevar mis conocimientos de Python a un nivel más 
    práctico, creando aplicaciones web interactivas rápidamente sin complicaciones.

    Hoy en día, me siento más segura al resolver problemas de programación y desarrollar proyectos, aunque sé que el aprendizaje 
    nunca termina. Cada día es una oportunidad para mejorar mis habilidades y enfrentar nuevos retos.
    """)

    # Definir los eventos en los meses de agosto, septiembre, octubre y noviembre
    timeline = {
        "Agosto": "Comencé a aprender Python desde cero y junto a las sesiones fui aprendiendo progresivamente.",
        "Septiembre": "Empecé a desarrollar programas más complejos y a entenderlo mejor.",
        "Octubre": "Me concentré en la depuración de errores y mejoré mi conocimiento en Git.",
        "Noviembre": "Empecé a trabajar con Streamlit para desarrollar mi primera aplicación interactiva."
    }

    # Slider para seleccionar el mes
    mes = st.slider("Selecciona un mes para ver tu progreso:", 8, 11, step=1, format="MM")

    # Mapeo de números a meses
    meses = {8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre"}

    # Mostrar el progreso basado en el mes seleccionado
    st.write(f"En {meses[mes]}: {timeline[meses[mes]]}")




elif opcion == "⚙️ RETOS":
    st.title("⚙️ Retos")
    # Línea decorativa debajo del título
    st.markdown("""
        <hr style="border: none; height: 2px; margin-top: -5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);">
    """, unsafe_allow_html=True)

    # Crear dos columnas para distribuir el contenido
    col1, col2 = st.columns(2)

    # Columna 1: Mostrar las barras de desplazamiento (sliders)
    with col1:
        st.write("Selecciona la dificultad de los retos afrontados:")
        dificultad_programacion = st.slider(
            "*Entender la lógica de programación",
            min_value=0,
            max_value=100,
            value=70,  # Valor inicial
            step=1
        )

        dificultad_errores = st.slider(
            "*Depuración de errores",
            min_value=0,
            max_value=100,
            value=85,
            step=1
        )

        dificultad_tiempo = st.slider(
            "*Gestión del tiempo",
            min_value=0,
            max_value=100,
            value=60,
            step=1
        )

        dificultad_comunicacion = st.slider(
            "*Comunicación efectiva",
            min_value=0,
            max_value=100,
            value=50,  # Valor inicial
            step=1
        )

        dificultad_creatividad = st.slider(
            "*Creatividad en la solución de problemas",
            min_value=0,
            max_value=100,
            value=80,  # Valor inicial
            step=1
        )

    # Columna 2: Mostrar una imagen
    with col2:
        st.image("imagenes/retos.jpg", use_container_width=True)



elif opcion == "🌟 APRENDIZAJE CLAVE":
    st.title("🌟 Aprendizaje Clave")
    # Línea decorativa debajo del título
    st.markdown("""
        <hr style="border: none; height: 2px; margin-top: -5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);">
    """, unsafe_allow_html=True)
    st.write("""
    Aquí están algunos momentos clave que marcaron mi aprendizaje:
    
    - **Mi primer programa funcional**: Ver un proyecto completo funcionando fue increíble.
    - **Colaboración en equipo**: Trabajar con mis compañeros me enseñó sobre comunicación y organización.
    - **Exploración de herramientas avanzadas**: Python y Streamlit me sorprendieron por su gran utilidad.
    """)

    st.write("**Progreso en habilidades**:")

    # Diccionario de habilidades y su progreso
    habilidades = {"Python": 90, "HTML/CSS": 75, "Streamlit": 85}

    for habilidad, progreso in habilidades.items():
        # Muestra el nombre de la habilidad
        st.write(f"{habilidad}: {progreso}%")
        
        # Muestra la barra de progreso
        st.progress(progreso / 100)


elif opcion == "💡 CONSEJOS":
    st.title("💡 Consejos")
    # Línea decorativa debajo del título
    st.markdown("""
        <hr style="border: none; height: 2px; margin-top: -5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);">
    """, unsafe_allow_html=True)
    st.write("Aquí tienes algunos consejos para facilitar tu proceso de aprendizaje:")
    with st.expander("1. Aprende a buscar en Google"):
        st.write("La programación no se trata de saberlo todo, sino de encontrar respuestas rápidamente.")
    with st.expander("2. Practica todos los días"):
        st.write("Incluso 30 minutos diarios hacen la diferencia.")
    with st.expander("3. No tengas miedo de equivocarte"):
        st.write("Los errores son oportunidades para aprender. ¡Abraza los bugs!")
    with st.expander("4. Aprende de tus errores"):
        st.write("Cada error es una oportunidad para mejorar. Al revisar lo que salió mal, puedes aprender mucho más que de lo que funciona correctamente.")
        
    with st.expander("5. No te compares con otros"):
        st.write("El aprendizaje es un proceso personal. No te compares con los demás, ya que cada quien tiene su propio ritmo. Enfócate en tu propio progreso.")







