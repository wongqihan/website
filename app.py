import os
import sys
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv

# Load env vars
load_dotenv()

# Instagram agent import removed (files deleted in commit 9379884)
generate_adventure = None
generate_images = None

app = Flask(__name__)

@app.route("/")
def index():
    """Render the portfolio landing page."""
    return render_template("index.html", name="Qi-Han Wong")

@app.route("/project/instagram-agent")
def project_instagram():
    """Render the Instagram Agent project detail page."""
    return render_template("project_instagram.html", name="Qi-Han Wong")

@app.route("/project/youtube-vibe")
def project_youtube_vibe():
    """Render the YouTube Vibe Matcher embedded project page."""
    return render_template("project_youtube_vibe.html", name="Qi-Han Wong")

@app.route("/project/shiok-scout")
def project_shiok_scout():
    """Render the Shiok Scout embedded project page."""
    return render_template("project_shiok_scout.html", name="Qi-Han Wong")

@app.route("/project/wrap-me-up")
def project_wrap_me_up():
    """Render the Wrap Me Up project page."""
    return render_template("project_wrap_me_up.html", name="Qi-Han Wong")

@app.route("/project/hawkersense")
def project_hawkersense():
    """Render the HawkerSense project page."""
    return render_template("project_hawkersense.html", name="Qi-Han Wong")

@app.route("/project/log-cake-protocol")
def project_log_cake_protocol():
    """Render the Log Cake Protocol project page."""
    return render_template("project_log_cake_protocol.html", name="Qi-Han Wong")

@app.route("/project/workout-corrector")
def project_workout_corrector():
    """Render the AI Workout Form Corrector project page."""
    return render_template("project_workout_corrector.html", name="Qi-Han Wong")


@app.route("/api/run/instagram-agent", methods=["POST"])
def run_instagram_agent():
    """
    Trigger the GenAI workflow:
    1. Generate Story (Gemini)
    2. Generate Images (Imagen)
    3. Return data (DO NOT post to Instagram)
    """
    return jsonify({
        "status": "error",
        "message": "Demo mode is currently disabled in this deployment."
    }), 503



if __name__ == "__main__":
    app.run(debug=True, port=5000)
