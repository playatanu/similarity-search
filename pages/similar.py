import streamlit as st
from app import get_similar_images
from PIL import Image


similar_images = get_similar_images(st.session_state.search_image, 13)
similar_images = similar_images[1:]

num_columns = 3
rows = [
    similar_images[i : i + num_columns]
    for i in range(0, len(similar_images), num_columns)
]

if st.button(
    f"back",
):
    st.switch_page("home.py")

image = Image.open(st.session_state.search_image).resize((300, 200))
st.image(image, width=300)
st.write(f"image: {st.session_state.search_image}")

st.header("Similar Images")

for row in rows:
    cols = st.columns(num_columns)
    for col, (img_id, img_path) in zip(cols, row):
        image = Image.open(img_path).resize((300, 200))
        col.image(
            image,
            width=300,
        )
