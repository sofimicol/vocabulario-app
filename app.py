import streamlit as st
import pandas as pd
from gtts import gTTS
import tempfile

# ------------------ CONFIG ------------------
st.title("📚 Vocabulario Interactivo")

url = "https://docs.google.com/spreadsheets/d/1rc3eytRj9tKgX0GkP5qj6xQx4S2iTlN1/export?format=csv&gid=888573341"

# FIX encoding (evita PoblaciÃ³n, EstadÃ­stico, etc.)
df = pd.read_csv(url, encoding="utf-8")

# ------------------ FUNCIÓN AUDIO ------------------
def play_audio(word):
    tts = gTTS(text=word, lang="en")
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    st.audio(temp_file.name)

# ------------------ DEBUG ------------------
st.write("Columnas detectadas:", df.columns)

# ------------------ APP ------------------
for index, row in df.iterrows():
    st.markdown("---")

    word = str(row.get("Word", "")).strip()
    meaning = row.get("Meaning", "")
    translation = row.get("Translation", "")
    phonetic = row.get("Phonetic", "")
    example = row.get("Example", "")

    # WORD
    st.subheader(word)

    # CONTENIDO
    st.write(meaning)
    st.write(translation)
    st.write(phonetic)
    st.write(example)

    # ------------------ AUDIO BUTTON ------------------
    if st.button(f"🔊 Pronunciar", key=index):
        if word:
            play_audio(word)
        else:
            st.warning("No hay palabra para pronunciar")
