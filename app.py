import streamlit as st
import yt_dlp
import os
import time

# --- Lógica de Descarga ---
def descargar_musica(url):
    carpeta = "Mi_musica"
    
    # 1. Crear carpeta si no existe (Streamlit a veces necesita esta carpeta para el output)
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
        
    # 2. Configuración de yt-dlp con mejoras de compatibilidad
    opciones = {
        'format': 'bestaudio/best',
        'outtmpl': f'{carpeta}/%(title)s.%(ext)s', 
        'noplaylist': True,
        # OPCIONES DE COMPATIBILIDAD AÑADIDAS:
        # User-agent imita un navegador Chrome para evitar bloqueos de bot
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        # Agrega metadatos a los archivos descargados
        'add_metadata': True,  
        # Ayuda con ciertos tipos de enlaces de YouTube
        'extract_flat': 'in_playlist',
    }
    
    st.info(f"Iniciando descarga de: {url}...")
    
    try:
        # 3. Inicia la descarga
        with yt_dlp.YoutubeDL(opciones) as ydl:
            # Captura información del video antes de descargar (para mostrar el título)
            info = ydl.extract_info(url, download=False)
            titulo = info.get('title', 'archivo_descargado')
            
            # Descarga el archivo
            ydl.download([url])
            
            # Nota: El archivo se guarda en el servidor. Para que el usuario lo baje, 
            # necesitarías un botón de descarga adicional en la web app, 
            # pero el mensaje de éxito se mantiene.
            st.success(f"¡Descarga completada! El archivo '{titulo}' está guardado en el servidor.")
            
    except Exception as e:
        st.error(f"❌ Ocurrió un error durante la descarga.")
        st.code(f"Detalles del error: {e}")


# --- Interfaz de Streamlit ---

st.set_page_config(page_title="YouTube Audio Downloader", layout="centered")

st.title("ADEN MUSIC 2.0")
st.markdown("Pega el enlace de un video y descarga el audio.")

# Campo de entrada para la URL
url_input = st.text_input("Ingresa la URL del video de YouTube aquí:", placeholder="Ej: https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if st.button("Descargar Audio"):
    if url_input:
        with st.spinner('Procesando y descargando... Esto puede tardar unos segundos.'):
            descargar_musica(url_input)
    else:
        st.warning("Por favor, ingresa una URL antes de descargar.")
