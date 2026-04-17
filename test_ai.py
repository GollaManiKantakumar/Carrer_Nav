import google.generativeai as genai
import traceback

genai.configure(api_key="AIzaSyBsvs4Ig0AGvij6f5iVnJx07578LPV3HDc")
model = genai.GenerativeModel('gemini-1.5-flash')

try:
    print("Sending prompt...")
    response = model.generate_content("Hello, this is a test. Provide a simple JSON: {'status': 'ok'}")
    print("Response received.")
    print("Text:", response.text)
except Exception as e:
    print("Error occurred:")
    traceback.print_exc()
