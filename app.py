import streamlit as st
import pandas as pd
import os

st.title("📚 Vocabulario Interactivo")

# URL de tu Google Sheets
url = "https://docs.google.com/spreadsheets/d/1rc3eytRj9tKgX0GkP5qj6xQx4S2iTlN1/export?format=csv&gid=888573341"
df = pd.read_csv(url)

# Ruta base del proyecto (IMPORTANTE para evitar errores)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

for index, row in df.iterrows():
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])

    # ------------------ IMAGEN ------------------
    with col1:
        img_file = str(row["Image"]).strip()
        img_path = os.path.join(BASE_DIR, "images", img_file)

        if os.path.exists(img_path):
            st.image(img_path, width=150)
        else:
            st.warning(f"⚠️ Imagen no encontrada: {img_file}")

    # ------------------ TEXTO + AUDIO ------------------
    with col2:
        st.subheader(str(row["Word"]))
        st.write(row["Meaning"])
        st.write(row["Translation"])
        st.write(row["Phonetic"])
        st.write(row["Example"])

        # LIMPIEZA del nombre del archivo (clave para mayúsculas y espacios)
        audio_file = str(row["Audio"]).strip()
        audio_path = os.path.join(BASE_DIR, "audio", audio_file)

        # DEBUG visual
        st.caption(f"🔍 Buscando audio: {audio_file}")

        if os.path.exists(audio_path):
            st.audio(audio_path)
        else:
            st.error(f"❌ No se encontró el audio: {audio_file}")
