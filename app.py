import streamlit as st
import pandas as pd
import os

st.title("📚 Vocabulario Interactivo")
url = "https://docs.google.com/spreadsheets/d/1rc3eytRj9tKgX0GkP5qj6xQx4S2iTlN1/export?format=csv"

df = pd.read_csv(url)
for index, row in df.iterrows():
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])

    with col1:
        img_path = os.path.join("images", str(row["Image"]))
        if os.path.exists(img_path):
            st.image(img_path, width=150)

    with col2:
        st.subheader(row["Word"])
        st.write(row["Meaning"])
        st.write(row["Translation"])
        st.write(row["Phonetic"])
        st.write(row["Example"])

        audio_path = os.path.join("audio", str(row["Audio"]))
        if os.path.exists(audio_path):
            st.audio(audio_path)
