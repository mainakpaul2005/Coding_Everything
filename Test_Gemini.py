# d:/Coding/Test_Gemini.py

import google.generativeai as genai
import os

# Use .get() to safely read the environment variable by its NAME
api_key = os.environ.get("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set the GOOGLE_API_KEY environment variable.")

# Configure the library with the key you retrieved
genai.configure(api_key=api_key)

# Now the rest of your code can run
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("What is the current time in India?")
print(response.text)