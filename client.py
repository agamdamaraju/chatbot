import requests

url = "http://127.0.0.1:5000/chatbot"

response = requests.post(url, json={'message': 'What city am I currenty in?'})
if response.status_code == 200:
    print(response.json()) 
else:
    print(f"Error {response.status_code}: {response.text}")