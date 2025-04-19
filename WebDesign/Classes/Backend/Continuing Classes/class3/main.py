from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime
load_dotenv()
mongo = os.getenv("mongo")
app = Flask(__name__)
CORS(app)
client = MongoClient(mongo)
db = client['walkie']
collection = db.messages
@app.route("/")
def home():
  return render_template('index.html')

@app.route("/send_message", methods=["POST"])
def send():
  data = request.get_json()
  message = data.get("message", None)
  if message:
    now = datetime.now()
    timestamp = now.strftime("%y-%m-%d %H:%M:%S")
    collection.insert_one({"message": message, "timestamp": timestamp})
    return jsonify({"message": "Message sent successfully!"}), 200
  else:
    return jsonify({"error": "No message provided"}), 400 
@app.route("/receive_message", methods=["GET"])
def recieve():
  messages = list(collection.find().sort('timestamp', -1))
  for msg in messages: 
    msg["_id"] = str(msg["_id"])
  return jsonify({"messages": messages}), 200

if __name__ == "__main__":
  app.run(debug=True, port=8000)