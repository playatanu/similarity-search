import streamlit as st
from app import load_image
from PIL import Image

st.header("Similar Search using Image Embedding +  Vector Database")

if "all_images" not in st.session_state:
    st.session_state.all_images = load_image()

if "search_image" not in st.session_state:
    st.session_state.search_image = None


num_columns = 3
rows = [
    st.session_state.all_images[i : i + num_columns]
    for i in range(0, len(st.session_state.all_images), num_columns)
]

for row in rows:
    cols = st.columns(num_columns)
    for col, (img_id, img_path) in zip(cols, row):
        image = Image.open(img_path).resize((300, 200))

        col.image(image, width=300)
        if col.button(f"{img_path}", key=img_id):
            st.session_state.search_image = img_path
            st.switch_page("pages/similar.py")
