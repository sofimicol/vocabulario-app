import streamlit as st
import pandas as pd
import os

st.title("📚 Vocabulario Interactivo")

# URL de tu Google Sheets
url = "https://docs.google.com/spreadsheets/d/1rc3eytRj9tKgX0GkP5qj6xQx4S2iTlN1/export?format=csv&gid=888573341"
df = pd.read_csv(url)

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# DEBUG opcional (puedes borrarlo después)
st.write("Columnas detectadas:", df.columns)

for index, row in df.iterrows():
    st.markdown("---")

    st.subheader(str(row.get("Word", "")))
    st.write(row.get("Meaning", ""))
    st.write(row.get("Translation", ""))
    st.write(row.get("Phonetic", ""))
    st.write(row.get("Example", ""))

    # ------------------ AUDIO ------------------
    audio_value = row.get("Audio")

    if pd.notna(audio_value):
        audio_file = str(audio_value).strip()
        audio_file = " ".join(audio_file.split())  # limpia espacios dobles

        audio_path = os.path.join(BASE_DIR, "audio", audio_file)

        st.caption(f"🔍 Buscando audio: {audio_file}")

        if os.path.exists(audio_path):
            st.audio(audio_path)
        else:
            st.error(f"❌ No se encontró el audio: {audio_file}")
    else:
        st.warning("⚠️ No hay audio para esta palabra")
