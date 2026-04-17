import requests
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyBsvs4Ig0AGvij6f5iVnJx07578LPV3HDc"
headers = {'Content-Type': 'application/json'}
payload = {"contents": [{"parts": [{"text": "Hello"}]}]}
res = requests.post(url, headers=headers, json=payload)
print(res.status_code)
print(res.text)
