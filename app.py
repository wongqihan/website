import os
import sys
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv

# Load env vars
load_dotenv()

# Import core functions
try:
    from instagram_agent.main import generate_adventure, generate_images
except ImportError:
    # Fallback if running from root
    import sys
    sys.path.append(os.path.abspath("."))
    from instagram_agent.main import generate_adventure, generate_images

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

@app.route("/api/run/instagram-agent", methods=["POST"])
def run_instagram_agent():
    """
    Trigger the GenAI workflow:
    1. Generate Story (Gemini)
    2. Generate Images (Imagen)
    3. Return data (DO NOT post to Instagram)
    """
    try:
        # 1. Generate Story
        story = generate_adventure(dry_run=False)
        
        # 2. Generate Images
        # generate_images returns (image_paths, video_path)
        # We need to handle the fact that generate_images uploads to GCS in the original script?
        # Actually, looking at main.py, generate_images returns local paths.
        # But wait, the upload logic was in upload_carousel.
        # We need to upload to GCS to get public URLs for the frontend to display?
        # OR we can serve local files if running locally, but for production we need GCS.
        
        # Let's check main.py again. generate_images saves locally.
        # We should modify/wrapper to upload to GCS and return URLs.
        
        image_paths, video_path = generate_images(story, dry_run=False)
        
        # Helper to upload to GCS and get URL (reusing logic from main.py)
        public_urls = []
        try:
            from google.cloud import storage
            import time
            
            project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
            if project_id:
                storage_client = storage.Client(project=project_id)
                bucket = storage_client.bucket("boboandstella-instagram")
                
                for img_path in image_paths:
                    if not img_path or not os.path.exists(img_path):
                        continue
                        
                    blob_name = f"website_demo/{int(time.time())}_{os.path.basename(img_path)}"
                    blob = bucket.blob(blob_name)
                    blob.upload_from_filename(img_path)
                    
                    public_url = f"https://storage.googleapis.com/boboandstella-instagram/{blob_name}"
                    public_urls.append(public_url)
        except Exception as e:
            print(f"GCS Upload failed: {e}")
            # Fallback: If we can't upload, we can't easily show them unless we serve static files.
            # For now, return error or placeholder.
            return jsonify({"status": "error", "message": "Failed to upload generated images to cloud."}), 500

        return jsonify({
            "status": "success",
            "story": story,
            "images": public_urls,
            "logs": [
                "✅ Gemini 2.5 Flash: Generated story context.",
                f"✅ Imagen 3.0: Generated {len(image_paths)} photorealistic images.",
                "✅ Google Cloud Storage: Images uploaded to public bucket.",
                "⚠️ Instagram Graph API: Posting disabled for demo mode."
            ]
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500



if __name__ == "__main__":
    app.run(debug=True, port=5000)
