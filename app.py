import streamlit as st
from elevenlabs import generate, set_api_key
from moviepy.editor import *
import os

# 🔐 Set your ElevenLabs API Key here
set_api_key("sk_a61a466b7fff5a7ae1e4f67dda5f83bfa7ba14e814944f6d")

st.set_page_config(page_title="Talking Avatar with ElevenLabs", layout="centered")

st.title("🗣️ Talking Avatar (ElevenLabs)")
st.markdown("Enter text and watch your avatar speak with lifelike ElevenLabs voice!")

text_input = st.text_area("📝 Enter your text here:")

if st.button("🎬 Generate Talking Avatar"):
    if text_input.strip():
        with st.spinner("Generating speech and video..."):

            try:
                # 1. Generate audio from ElevenLabs
                audio = generate(
                    text=text_input,
                    voice="EXAVITQu4vr4xnSDxMaL",  # You can change to any available voice
                    model="eleven_multilingual_v2"
                )
                with open("output.mp3", "wb") as f:
                    f.write(audio)

                # 2. Create video from avatar + audio
                if not os.path.exists("avatar.jpg"):
                    st.error("Missing 'avatar.jpg'. Please upload it.")
                else:
                    image_clip = ImageClip("avatar.jpg").set_duration(5)
                    audio_clip = AudioFileClip("output.mp3")
                    video = image_clip.set_audio(audio_clip)

                    video.write_videofile("final.mp4", fps=1)

                    # 3. Display the video
                    st.success("✅ Done!")
                    st.video("final.mp4")

            except Exception as e:
                st.error(f"Error: {e}")

    else:
        st.warning("Please enter some text.")


