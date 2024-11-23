import streamlit as st
import pyttsx3
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Configure Streamlit UI
st.title("🎤 English Text-to-Speech Converter")
st.write("Convert your text into spoken audio in English!")

# Input text
text_input = st.text_area("Enter the text you want to convert to speech:", "")

# Voice gender options
voice_gender = st.radio("Select Voice Gender:", ("Male", "Female"))

# Speech rate
rate = st.slider("Select Speech Rate:", min_value=100, max_value=300, value=200)

# Set voice and rate for English
voices = engine.getProperty("voices")
engine.setProperty("rate", rate)

# Set the voice based on user choice (Male or Female)
selected_voice = None
if voice_gender == "Male":
    selected_voice = voices[0]  # Select Male voice (first voice, usually Male)
else:
    selected_voice = voices[1]  # Select Female voice (second voice, usually Female)

# Set the selected voice
if selected_voice:
    engine.setProperty("voice", selected_voice.id)

# Button to convert text to speech
if st.button("Convert to Speech"):
    if text_input.strip():
        with st.spinner("Processing your request..."):
            try:
                # Use the input text directly for speech synthesis
                output_audio_file = "output_audio.mp3"
                engine.save_to_file(text_input, output_audio_file)
                engine.runAndWait()

                # Provide the audio for playback
                audio_file = open(output_audio_file, "rb")
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/mp3")
                st.success(f"Speech synthesis in English complete! 🎉")

                # Download button for the audio
                st.download_button(
                    label="Download Audio",
                    data=audio_bytes,
                    file_name="speech_english.mp3",
                    mime="audio/mp3",
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to convert!")

# Footer
st.write("Powered by pyttsx3")
