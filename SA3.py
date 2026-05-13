
import streamlit as st
from groq import Groq

# -----------------------------------
# Configure Groq API
# -----------------------------------

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

        prompt = f"""
        Generate a {tone} greeting message for {name}
        on the occasion of {occasion}.

        Keep it short and meaningful.
        """

        with st.spinner("Generating Greeting..."):

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a greeting generator."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            greeting = response.choices[0].message.content

        st.success("Greeting Generated Successfully")

        st.text_area(
            "Generated Greeting",
            greeting,
            height=150
        )