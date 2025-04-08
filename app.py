from flask import Flask, render_template, request
from elevenlabs import generate, save, set_api_key

# ✅ Set API key and voice ID
set_api_key("sk_a61a466b7fff5a7ae1e4f67dda5f83bfa7ba14e814944f6d")
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # ← Use voice ID from your account

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]

        try:
            # ✅ Generate speech using ElevenLabs
            audio = generate(
                text=text,
                voice=VOICE_ID,
                model="eleven_monolingual_v1"
            )
            save(audio, "static/output.mp3")
            return render_template("index.html", audio_file="static/output.mp3")
        except Exception as e:
            return f"❌ Error: {str(e)}"

    return render_template("index.html", audio_file=None)

if __name__ == "__main__":
    app.run(debug=True)

