import streamlit as st
from groq import Groq

client = Groq(
    api_key="YOUR_OWN_API_KEY"
)

# -----------------------------------
# Streamlit Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="AI Greeting Generator",
    page_icon="🤖"
)

# -----------------------------------
# App Title
# -----------------------------------

st.title("AI Greeting Generator")

st.write("Generate greetings using Generative AI")

# -----------------------------------
# User Inputs
# -----------------------------------

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

# -----------------------------------
# Generate Greeting
# -----------------------------------

if st.button("Generate Greeting"):

    if name.strip() == "":
        st.warning("Please enter a name")

    else:

        # -----------------------------------
        # Create Prompt
        # -----------------------------------

        prompt = f"""
        Generate a {tone} greeting message for {name}
        on the occasion of {occasion}.

        Keep it short and meaningful.
        """

        # -----------------------------------
        # Display Prompt
        # -----------------------------------

        st.success("Prompt Created Successfully")

        st.text_area(
            "Generated Prompt",
            prompt,
            height=150
        )