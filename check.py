from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

print("\nAvailable Gemini Models:\n")

for model in genai.list_models():
    print(model.name)

    if hasattr(model, "supported_generation_methods"):
        print("Supported Methods:", model.supported_generation_methods)

    print("-" * 50)