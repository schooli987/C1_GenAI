import streamlit as st

st.set_page_config(
    page_title="AI Greeting Generator",
    page_icon="🤖"
)
st.title("AI Greeting Generator")

st.write("Generate greetings using Generative AI")

name = st.text_input(
    "Enter Name",
    placeholder="John"
)

occasion = st.selectbox(
    "Choose Occasion",
    [
        "Birthday",
        "Festival",
        "New Year",
        "Welcome",
        "Congratulations"
    ]
)

tone = st.selectbox(
    "Choose Tone",
    [
        "Formal",
        "Friendly",
        "Funny",
        "Professional"
    ]
)

generate = st.button("Generate Greeting")