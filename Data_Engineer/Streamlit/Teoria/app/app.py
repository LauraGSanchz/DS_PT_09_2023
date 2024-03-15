import streamlit as st

<<<<<<< HEAD
# Función para cargar el CSS personalizado
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    # Cargar el CSS personalizado
    local_css("archivo.css")
    
    # Agregar contenido a la página
    st.title("Hola Mundo, esta es mi página de Streamlit")
    st.header("¡BIENVENIDOS!")
    st.balloons()
    st.write("Este es un contenido de ejemplo en mi aplicación de Streamlit.")
    st.write("¡La imagen de fondo debería estar visible ahora!")

if __name__ == "__main__":
    main()
=======
st.title('Hola mundo, esta es una prueba desde streamlit')
>>>>>>> upstream/main
