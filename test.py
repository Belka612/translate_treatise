# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# load_dotenv()

# GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
# genai.configure(api_key=GOOGLE_API_KEY)

# gemini_pro = genai.GenerativeModel("gemini-1.5-flash-8b")
# with open("prompt.txt", "r", encoding="utf-8") as file:
#     prompt = file.read()

# response = gemini_pro.generate_content(prompt)
# print(response.text)

import tiktoken
encoding = tiktoken.encoding_for_model("gpt-4o")
encode = encoding.encode('何らかのテキスト')

print(len(encode))
