# Login-Microservice
# Description: 

# Comunnication Pipe:
Rest API

# Request Data:
Applications will send a request to the microservice which will compare username and password against stored credentials which will return a response indication whether the request was successful, or it failed. 

# Receive Data:
The Login Microservice will receive a POST request from applications with the username and password. The microservice will check the validity of the login attempt by checking the provided passwords with stored account information. The microservice will produce a JSON response with authentication status, confirmation messages, or error notifications after processing the request.

# Example call:
SEND POST request to /login with username and password

RECEIVE JSON response

If status == “success”:
        allow user access
Else:
        deny access and show error alert
