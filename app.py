import streamlit as st
from generate_ppt import generate_slide_content, create_ppt

st.set_page_config(page_title="AI PPT Generator", page_icon="🎓", layout="centered")

st.title("🎓 AI-Powered PPT Generator")
st.write("Create high-quality educational PowerPoint slides in minutes using AI!")

topic = st.text_input("Enter your topic:")
slides = st.slider("Number of slides", 5, 15, 8)

if st.button("Generate Presentation"):
    if not topic.strip():
        st.warning("Please enter a topic before generating.")
    else:
        with st.spinner("✨ Generating slides... please wait."):
            try:
                content = generate_slide_content(topic, slides)
                ppt_path = create_ppt(content)
                st.success("✅ PowerPoint generated successfully!")
                with open(ppt_path, "rb") as f:
                    st.download_button("⬇️ Download PPT", f, file_name="AI_Presentation.pptx")
            except Exception as e:
                st.error(f"An error occurred: {e}")
