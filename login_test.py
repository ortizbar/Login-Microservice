import requests

url = "http://localhost:3000/login"
data = { "username":"test123", "password":"test1234"}
response = requests.post(url, json=data)

print("Status Code":, response.status_code)
print("Respnose JSON":, response.json())
