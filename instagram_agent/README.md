# Instagram Automation Agent

This agent automates daily Instagram posts for Bobo and Stella.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Environment Variables**:
    Copy `.env.example` to `.env` and fill in your details:
    ```bash
    cp .env.example .env
    ```
    - `GOOGLE_API_KEY`: Your Google Cloud API key (with Gemini and Imagen enabled).
    - `INSTAGRAM_USERNAME`: Your Instagram handle.
    - `INSTAGRAM_PASSWORD`: Your Instagram password.

## Usage

### Dry Run (Test)
To test the story generation and image generation (mocked or real) without uploading:
```bash
python3 main.py --dry-run
```
This will save generated images to the current directory.

### Live Run
To generate and upload to Instagram:
```bash
python3 main.py
```

## Deployment
You can deploy this to Google Cloud Functions by setting up a Cloud Scheduler to trigger the function daily.
