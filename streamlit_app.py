import streamlit as st
from PIL import Image

st.title("Automating Logistics Sign")
data_load_state = st.text("Loading necessary stuff...")
data_load_state.text("Loading necessary stuff...done!")


col1, col2 = st.columns(2, gap="medium")

with col1:
    uploaded_file = st.file_uploader("Choose a image file", type=["jpg", "png"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, use_column_width="always")

with col2:
    st.subheader("Prompt: ")
    prompt = st.text_area("Prompt: ").strip()

    submit_btn = st.button("Submit")
    if submit_btn:
        ans = "Success"
    else:
        ans = ""

    st.subheader("Answer: ")
    st.markdown("**" + ans + "**")
