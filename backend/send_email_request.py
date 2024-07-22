import requests

# Set the URL
url = 'http://127.0.0.1:8000/student/send-email/'

# Make a POST request
response = requests.post(url)

# Print the response
print(f'Status Code: {response.status_code}')
print(f'Response Content: {response.text}')
