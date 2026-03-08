from google import genai
from google.genai import types

# 1. Setup - Use your API key here
client = genai.Client(api_key="AIzaSyDwUrsbZW4pN689AxqmQ59779t_bRgGj3U")

# 2. Configure the Note-Taking Instructions
instruction = (
    "You are a professional note-taking assistant. "
    "Structure all responses using Markdown with clear headers like "
    "## Summary, ### Key Points, and ### Action Items."
)

def start_notebot():
    print("--- Note-Bot is Active (Type 'exit' to quit) ---")
    
    # Starting a chat session with the newer 2.5 Flash model
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(system_instruction=instruction)
    )

    while True:
        user_text = input("\nEnter text to organize: ")
        
        if user_text.lower() in ["exit", "quit"]:
            break

        try:
            response = chat.send_message(user_text)
            print("\n" + "="*30)
            print(response.text)
            print("="*30)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    start_notebot()