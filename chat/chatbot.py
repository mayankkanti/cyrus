import google.generativeai as genai
import os
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-latest",
  system_instruction='''<ADD SYSTEM INSTRUCTION FOR CYRUS HERE!!!!!>''')

chat = model.start_chat()
class Reply:
    def gemini_response(query):
        try:
            response = chat.send_message(query)
            return response.text 
        except Exception as e:
            return f"Uh Oh... Something went wrong. Please contact Mayank at mayankkanti2325@gmail.com. Error: {e}"