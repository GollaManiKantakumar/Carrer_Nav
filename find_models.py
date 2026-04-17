import requests
res = requests.get('https://generativelanguage.googleapis.com/v1beta/models?key=AIzaSyBsvs4Ig0AGvij6f5iVnJx07578LPV3HDc').json()
for m in res.get('models', []):
    if 'generateContent' in m.get('supportedGenerationMethods', []):
        print(m['name'])
