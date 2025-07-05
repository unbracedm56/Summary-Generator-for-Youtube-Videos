import streamlit as st
from main import summary_generator

st.title("Summary Generator for Youtube Videos")

st.text_input("Enter Youtube URL", key="URL")

st.subheader("Generated Summary:")
if st.session_state.URL:
    summary = summary_generator(st.session_state.URL)
    st.write(summary)