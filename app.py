import streamlit as st
import yt_dlp
import os
import time

# --- Lógica de Descarga (Tu código) ---
def descargar_musica(url):
    carpeta = "Mi_musica"
    
    # 1. Crear carpeta si no existe (no necesaria en Streamlit, pero por seguridad)
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
        
    # 2. Configuración de yt-dlp
    opciones = {
        'format': 'bestaudio/best',
        # Nota: En una web app, el archivo se guarda donde se ejecuta el script.
        'outtmpl': f'{carpeta}/%(title)s.%(ext)s', 
        'noplaylist': True 
    }
    
    st.info(f"Iniciando descarga de: {url}...")
    
    try:
        # 3. Inicia la descarga
        with yt_dlp.YoutubeDL(opciones) as ydl:
            # Captura información del video antes de descargar (opcional, para el título)
            info = ydl.extract_info(url, download=False)
            titulo = info.get('title', 'archivo_descargado')
            
            # Descarga el archivo
            ydl.download([url])
            
            st.success(f"¡Descarga completada! El archivo '{titulo}' está guardado en la carpeta '{carpeta}'.")
            
    except Exception as e:
        st.error(f"❌ Ocurrió un error durante la descarga.")
        st.code(f"Detalles del error: {e}")


# PROBANDO LA INTEFAZ :_V

st.set_page_config(page_title="YouTube Audio Downloader", layout="centered")

st.title("ADEN MUSIC 2.0")
st.markdown("Pega el enlace de un video y descarga el audio.")

# LINK CELDA URL :V
url_input = st.text_input("Ingresa la URL del video de YouTube aquí:", placeholder="Ej: https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if st.button("Descargar Audio"):
    if url_input:
        with st.spinner('Procesando y descargando... Esto puede tardar unos segundos.'):
            descargar_musica(url_input)
    else:
        st.warning("Por favor, ingresa una URL antes de descargar.")