from flask import Flask, render_template, request
from elevenlabs import generate, play, Voice, set_api_key
import os
import subprocess

app = Flask(__name__)

# ✅ Set your ElevenLabs API key
set_api_key("sk_0be86a97d6cd7dd86b035694a0a607d3bb9466018b9090b7")  # Replace this!

@app.route('/', methods=['GET', 'POST'])
def index():
    show_video = False

    if request.method == 'POST':
        text = request.form['text']

        # Generate TTS audio
        audio = generate(
            text=text,
            voice="EXAVITQu4vr4xnSDxMaL",  # You can change to another voice in your account
            model="eleven_monolingual_v1"
        )

        # Save audio to file
        with open("static/output.mp3", "wb") as f:
            f.write(audio)

        # ✅ Generate talking video (basic version using image)
        subprocess.call([
            "ffmpeg", "-y",
            "-loop", "1",
            "-i", "avatar.jpg",
            "-i", "static/output.mp3",
            "-shortest",
            "-vf", "scale=640:480",
            "-c:v", "libx264",
            "-c:a", "aac",
            "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "static/talking_avatar.mp4"
        ])

        show_video = True

    return render_template("index.html", show_video=show_video)

if __name__ == '__main__':
    app.run(debug=True)