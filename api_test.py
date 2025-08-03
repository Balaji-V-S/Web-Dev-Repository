import requests

api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMzIsInJvbGUiOiJvcmd1c2VyIiwiZW1haWwiOiJiYWxhamkudnNAcHJvZGFwdC5jb20iLCJ1c2VybmFtZSI6InVzZXJfMDEzMSIsImlhdCI6MTc1NDIwNjQ4NiwiZXhwIjoxNzU0MjEwMDg2fQ.StSICDz0zDMxr_XIkcHFUV5AGkBw4uQYV8e7hhRgmEI"   # Replace with actual OpenAI API key
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
