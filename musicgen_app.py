import streamlit as st
from transformers import pipeline
import scipy.io.wavfile

# Load the MusicGen model
@st.cache_resource
def load_model():
    return pipeline("text-to-audio", model="facebook/musicgen-small")

model = load_model()

# Streamlit app
st.title("Music Generation with MusicGen")
prompt = st.text_input("Enter your music prompt:")

if st.button("Generate Music"):
    if prompt:
        with st.spinner("Generating music..."):
            music = model(prompt, forward_params={"do_sample": True})
            audio_data = music["audio"]
            sampling_rate = music["sampling_rate"]
            
            # Save the generated music to a file
            output_file = "generated_music.wav"
            scipy.io.wavfile.write(output_file, rate=sampling_rate, data=audio_data)
            
            st.success("Music generated successfully!")
            st.audio(output_file, format="audio/wav")
    else:
        st.warning("Please enter a prompt to generate music.")
