import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_image_with_question(image_bytes: bytes, question: str) -> str:
    response = model.generate_content([
        question,
        {
            "mime_type": "image/jpeg",
            "data": image_bytes
        }
    ])
    return response.text
