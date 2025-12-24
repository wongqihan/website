# Setting up Google Cloud Vertex AI

To use **Imagen 3** and **Veo** properly, you need to enable Vertex AI on your Google Cloud Project and set up authentication.

## 1. Enable the API
1.  Go to the [Vertex AI API page](https://console.cloud.google.com/marketplace/product/google/aiplatform.googleapis.com) in the Google Cloud Console.
2.  Select your project (the one matching your API key).
3.  Click **Enable**.

## 2. Install Google Cloud CLI
You need the `gcloud` command-line tool to authenticate.
1.  **Download & Install**: Follow instructions here: [Install gcloud CLI](https://cloud.google.com/sdk/docs/install).
    *   *Mac Tip*: If you have Homebrew, run `brew install --cask google-cloud-sdk`.

## 3. Authenticate
Run this command in your terminal to log in:
```bash
gcloud auth application-default login
```
This creates a local credential file that the Python script will automatically use.

## 4. Update Dependencies
I will update your `requirements.txt` to include `google-cloud-aiplatform`.
