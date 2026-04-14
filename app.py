import streamlit as st
import pandas as pd
from gtts import gTTS
import tempfile

st.title("Vocabulario Interactivo")

url = "https://docs.google.com/spreadsheets/d/1rc3eytRj9tKgX0GkP5qj6xQx4S2iTlN1/export?format=csv&gid=888573341"

df = pd.read_csv(
    url,
    encoding="utf-8",
    on_bad_lines="skip"
)

df.columns = df.columns.str.strip()

st.write("Recursos", df.columns)

def play_audio(word):
    tts = gTTS(word, lang="en")
    file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(file.name)
    st.audio(file.name)

for i, row in df.iterrows():
    st.markdown("---")

    word = row.get("Word", "")
    meaning = row.get("Meaning", "")
    translation = row.get("Translation", "")
    phonetic = row.get("Phonetic", "")
    example = row.get("Example", "")
    word_family = row.get("Word Family", "")
    etymology = row.get("Etymology", "")

    if word:
        st.subheader(word)

    if meaning:
        st.write("Meaning:", meaning)

    if translation:
        st.write("Translation:", translation)

    if phonetic:
        st.write("Phonetic:", phonetic)

    if example:
        st.write("Example:", example)

    if word_family:
        st.write("Word Family:", word_family)

    if etymology:
        st.write("Etymology:", etymology)

    if st.button("Pronounce", key=i):
        play_audio(word)
