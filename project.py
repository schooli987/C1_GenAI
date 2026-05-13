# ======================================
# AI Fun Facts Generator
# Streamlit + Groq
# ======================================

import streamlit as st
from groq import Groq

# --------------------------------------
# GROQ API KEY
# --------------------------------------
API_KEY = "YOUR_OWN_API_KEY"

client = Groq(api_key=API_KEY)

# --------------------------------------
# PAGE SETTINGS
# --------------------------------------
st.set_page_config(
    page_title="AI Fun Facts Generator",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 AI Fun Facts Generator")

st.write("Generate interesting fun facts using AI")

# --------------------------------------
# TOPIC INPUT
# --------------------------------------
topic = st.text_input(
    "Enter a Topic",
    placeholder="Example: Space, Animals, Ocean, AI"
)

# --------------------------------------
# NUMBER OF FACTS
# --------------------------------------
num_facts = st.slider(
    "Number of Facts",
    min_value=1,
    max_value=10,
    value=5
)

# --------------------------------------
# GENERATE BUTTON
# --------------------------------------
if st.button("Generate Fun Facts"):

    if topic.strip() == "":
        st.warning("Please enter a topic")

    else:

        prompt = f"""
        Give {num_facts} fun and interesting facts about {topic}.
        Use simple language for students.
        """

        # --------------------------------------
        # AI RESPONSE
        # --------------------------------------
        with st.spinner("Generating Facts..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.8,
                max_tokens=400
            )

            output = response.choices[0].message.content

        # --------------------------------------
        # DISPLAY OUTPUT
        # --------------------------------------
        st.subheader("📚 Fun Facts")
        st.write(output)

        # --------------------------------------
        # DOWNLOAD BUTTON
        # --------------------------------------
        st.download_button(
            label="⬇️ Download Facts",
            data=output,
            file_name="fun_facts.txt",
            mime="text/plain"
        )