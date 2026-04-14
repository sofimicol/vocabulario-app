import streamlit as st
import pandas as pd
from gtts import gTTS
import tempfile

st.title("📚 Vocabulario Interactivo")

url = "https://docs.google.com/spreadsheets/d/1rc3eytRj9tKgX0GkP5qj6xQx4S2iTlN1/export?format=csv&gid=888573341"

df = pd.read_csv(
    url,
    encoding="utf-8",
    on_bad_lines="skip"
)

df.columns = df.columns.str.strip()

st.write("Columnas detectadas:", df.columns)

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
    image = row.get("Image", "")
    word_family = row.get("Word Family", "")
    etymology = row.get("Etymology", "")

    if word:
        st.subheader(word)

    st.write(f"📖 **Meaning:** {meaning}")
    st.write(f"🌍 **Translation:** {translation}")
    st.write(f"🔊 **Phonetic:** {phonetic}")
    st.write(f"💬 **Example:** {example}")

    # 👉 NUEVO: Word Family
    if word_family:
        st.write(f"🧩 **Word Family:** {word_family}")

    # 👉 NUEVO: Etymology
    if etymology:
        st.write(f"📜 **Etymology:** {etymology}")

    # 👉 Imagen (opcional)
    if image:
        st.image(image, width=150)

    if st.button("🔊 Pronunciar", key=i):
        play_audio(word)
