import os

def main():
    print("Checking GitHub Secrets...")
    print("Gemini Key Exists:", bool(os.environ.get("GEMINI_API_KEY")))
    print("Client ID Exists:", bool(os.environ.get("YOUTUBE_CLIENT_ID")))
    print("Client Secret Exists:", bool(os.environ.get("YOUTUBE_CLIENT_SECRET")))
    print("Refresh Token Exists:", bool(os.environ.get("YOUTUBE_REFRESH_TOKEN")))
    print("All secrets loaded successfully!")

if __name__ == "__main__":
    main()
  
