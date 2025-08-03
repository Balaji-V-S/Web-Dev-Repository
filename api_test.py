import requests

api_key = "Your_API_Key"   # Replace with actual OpenAI API key
url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-4o",
    "messages": [
        {"role": "admin", "content": "You are a helpful assistant."}
    ],
    "max_tokens": 1000
}

response = requests.post(url, headers=headers, json=data)
print(response.status_code, response.text)
