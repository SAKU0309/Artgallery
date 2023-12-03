import json
import requests

headers = {"Authorization: bearer <eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYjY0ODE5ZGItYWJiMi00ZDEwLWFkMWQtMDA3ODIyNTUyMjhmIiwidHlwZSI6ImFwaV90b2tlbiJ9.eX5jLo_rxhdjrQcwRBhINj2lndbrC7iNr9oFEz5Mfiw>"}

url = "https://api.edenai.run/v2/image/generation"
payload = {
    "providers": "openai,stabilityai",
    "text": "photo of a mouse",
    "resolution": "512x512"   
}

response = requests.post(url, json=payload, headers=headers)
result = json.loads(response.text)
print(result['openai'])

