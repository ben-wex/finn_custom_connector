import requests

# Replace this with the actual URL of your deployed API Gateway endpoint
url = "https://3vnc926e93.execute-api.us-east-1.amazonaws.com/dev/chat"

# JSON payload to send in the POST request
data = {
    "input": "Tell me a fun fact!"
}

# Send the POST request to the Flask app
response = requests.post(url, json=data)

# Print the response from the server
if response.status_code == 200:
    print("GPT Response:", response.json().get('response'))
else:
    print(f"Error: {response.status_code}, {response.text}")
