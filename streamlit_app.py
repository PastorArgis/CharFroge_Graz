import streamlit as st

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )


st.title("DnD Character Sheet")

name = st.text_input("Name", "Arannis")
level = st.number_input("Level", 1, 20, 3)

st.write(f"{name} ist Level {level}")