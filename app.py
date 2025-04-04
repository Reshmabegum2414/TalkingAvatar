import streamlit as st
from elevenlabs import generate, save, set_api_key
import os
import subprocess

set_api_key("sk_0be86a97d6cd7dd86b035694a0a607d3bb9466018b9090b7")

st.title("🗣️ Talking Avatar Generator")

text = st.text_area("Enter your text below:")
if st.button("Generate Talking Avatar") and text:
    # Generate audio
    audio = generate(text=text, voice="EXAVITQu4vr4xnSDxMaL", model="eleven_monolingual_v1")
    save(audio, "output.mp3")

    # Merge with avatar image using ffmpeg
    if not os.path.exists("static"):
        os.makedirs("static")
    subprocess.call([
        "ffmpeg", "-y", "-i", "output.mp3", "-loop", "1", "-i", "static/avatar.jpg",
        "-c:v", "libx264", "-t", "5", "-pix_fmt", "yuv420p", "static/video.mp4"
    ])

    # Show result
    st.video("static/video.mp4")
