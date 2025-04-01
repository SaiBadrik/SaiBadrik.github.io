from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient("mongodb+srv://SaiBadrik:BADRIKTHEGOAT@cluster0.qtfa2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['walkie']
collection = db.messages