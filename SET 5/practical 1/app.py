 #A program that creates a simple RESTful API that returns a list of users in  JSON format.

from flask import Flask, jsonify 
app = Flask(__name__)
# Sample user data (replace with database connection if needed) 
users = [
{"id": 1, "name": "Ram", "email": "ram@example.com"},
{"id": 2, "name": "Shyam", "email": "shyam@example.com"},
{"id": 3, "name": "Sheel", "email": "sheel@example.com"},
]
@app.route('/',methods=['GET']) 
def get_users():

 return jsonify(users)
if __name__== ' main ': 
 app.run(debug=True)
