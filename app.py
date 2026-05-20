from flask import Flask, request, jsonify
app = flask (_name_)

#example of credentials

stored_username = "test123"
stored_password = "test1234"

@approute('/login', methods=['POST'])
def login():
  data = request.get_json()
  if "username" not in data or "password" not in data:
    return jsonify ({ 'status': "Error", 'notification': "Missing Username and Password"}), 400
  username = data["username"]
  password = data["password"]
  
  #validate credentials
  
  if username == stored_username and password == stored_password:
    return jsonify ({'status':"Success", 'notification' = "Login Successful"}), 200
  return jsonify ({'status':"Error", 'notification' = "Invalid Username or Password"}), 401

@approute('/logout', methods=['POST'])
def logout():
  return jsonify ({'status':"Success", 'notification' = "Logout Successful"}), 200

@approute('/reset-password', methods=['POST'])
def reset_password():
  data= request get_json()
  if "email" not in data:
    return jsonify ({ 'status': "Error", 'notification': "Email Required"}), 400
    return jsonify ({'status': "Success", 'notification': "Password link sent to email"}), 200

if _name_ == '_main_':
  app.run(host = '0.0.0.0', port=3000)
    
