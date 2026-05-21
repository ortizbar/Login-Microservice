import requests

url = "http://localhost:5000/login"
data = { "username":"test123", "password":"test1234"}
response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON":, response.json())
