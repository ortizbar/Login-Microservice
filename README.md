# Login-Microservice
# Description:
Login microservice provides user authentication and authorization. The microservices verifies username and password and returns a response indicating whether login attempt was successful or failed.

# Comunnication Pipe:
Rest API
Method: POST
Format: JSON
Endpoints: 
/login
/logout
/reset-password:

# Request Data:
Applications will send a request to the microservice which will compare username and password against stored credentials which will return a response indication whether the request was successful, or it failed. 

Request parameters
•username (string)
•Password (string)

# Example call:
import requests

url = "http://localhost:3000/login"
data = { "username":"test123", "password":"test1234"}
response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON":, response.json())

# Receive Data
The Login Microservice will receive a POST request from applications with the username and password. The microservice will check the validity of the login attempt by checking the provided passwords with stored account information. The microservice will produce a JSON response with authentication status, confirmation messages, or error notifications after processing the request.

# Example call:
SEND POST request to /login with username and password

RECEIVE JSON response

If status == “success”:
        allow user access
Else:
        deny access and show error alert

# UML Sequence
Client/Test Program       Login Microservice
      |                          |
      |---- POST /login--------->|
      |                          |
      |<--- JSON response--------|
      |                          |
