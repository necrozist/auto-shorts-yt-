import os
import google.generativeai as genai

def main():
    print("Initializing Auto Shorts Script...")
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing!")
    
    genai.configure(api_key=api_key)
    
    print("Generating YouTube Short topic & script using Gemini...")
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content("Give me a catchy 30-second YouTube Short script about an interesting space fact, including a Title and Description.")
    
    print("\n--- Generated Short Content ---")
    print(response.text)
    print("------------------------------\n")
    
    client_id = os.environ.get("YOUTUBE_CLIENT_ID")
    client_secret = os.environ.get("YOUTUBE_CLIENT_SECRET")
    refresh_token = os.environ.get("YOUTUBE_REFRESH_TOKEN")
    
    if client_id and client_secret and refresh_token:
        print("YouTube credentials are fully loaded and ready for upload integration!")
    else:
        print("Warning: Some YouTube credentials are missing.")

if __name__ == "__main__":
    main()
  
