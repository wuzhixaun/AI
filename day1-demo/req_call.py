import requests
import json
import os

print(os.getenv('OPENAI_API_KEY'))
url = os.getenv('OPENAI_BASE_URL') + "/chat/completions"
payload = json.dumps({
    "model": "gpt-4",
    "messages": [
        {"role": "system", "content": "assistant"},
        {"role": "user", "content": "Hello world"}
    ]
})
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + os.getenv('OPENAI_API_KEY'),
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
