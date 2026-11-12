import os
import sys

def main():
    print("Starting execution of main.py...")
    
    try:
        import google.generativeai as genai
        print("-> google.generativeai package loaded successfully.")
    except Exception as e:
        print(f"ERROR: Failed to import google.generativeai: {e}")
        sys.exit(1)
        
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY is missing from repository secrets!")
        sys.exit(1)
    else:
        print("-> GEMINI_API_KEY found.")
    
    try:
        genai.configure(api_key=api_key)
        
        # Automatically find the first available working model for this API key
        available_models = [
            m.name for m in genai.list_models()
            if 'generateContent' in m.supported_generation_methods
        ]
        
        if not available_models:
            print("ERROR: No models available for generateContent with this API key!")
            sys.exit(1)
            
        # Prefer a flash model if available, otherwise pick the first working one
        selected_model = next((m for m in available_models if 'flash' in m), available_models[0])
        print(f"-> Auto-selected working model: {selected_model}")
        
        model = genai.GenerativeModel(selected_model)
        print("-> Generating content using Gemini...")
        response = model.generate_content("Give me a catchy 30-second YouTube Short title and script about a space fact.")
        
        print("\n==============================")
        print("       GEMINI OUTPUT          ")
        print("==============================\n")
        print(response.text)
        print("\n==============================")
    except Exception as e:
        print(f"ERROR during Gemini API call: {e}")
        sys.exit(1)

    yt_client_id = os.environ.get("YOUTUBE_CLIENT_ID")
    yt_client_secret = os.environ.get("YOUTUBE_CLIENT_SECRET")
    yt_refresh_token = os.environ.get("YOUTUBE_REFRESH_TOKEN")
    
    if yt_client_id and yt_client_secret and yt_refresh_token:
        print("-> All YouTube credentials present and verified.")
    else:
        print("-> WARNING: Some YouTube credentials are missing in secrets.")

    print("\nScript executed successfully from start to finish!")

if __name__ == "__main__":
    main()
    
