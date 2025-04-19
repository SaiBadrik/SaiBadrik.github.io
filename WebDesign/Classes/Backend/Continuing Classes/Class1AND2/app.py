from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, render_template, request, url_for, redirect, jsonify
app = Flask(__name__)
client = MongoClient("mongodb+srv://SaiBadrik:BADRIKTHEGOAT@cluster0.qtfa2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['Badrik']
collection = db.tasks

class Task:
  dict = {}
  def __init__(self, title, description):
    self.task_data = {
      "title": title,
      "description": description,
      "status": "incomplete"
    }

@app.route('/')
def home():
  tasks  = list(collection.find())
  for task in tasks:
    task['_id'] = str(task['_id'])
  return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
  title = request.form['title']
  description = request.form['description']
  task = Task(title, description)
  collection.insert_one(task.task_data)
  return redirect(url_for('home'))

@app.route('/update/<id>', methods=['PUT'])
def update(id):
  status = request.json.get('status', 'incomplete')
  result = collection.update_one({'_id': ObjectId(id)}, {'$set': {'status': status}})
  if result.modified_count == 0:
    return jsonify({'error': 'Task not found'}), 404
  return jsonify({'message': 'Task updated successfully'})

@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
  result = collection.delete_one({'_id': ObjectId(id)})
  if result.deleted_count == 0:
    return jsonify({'error': 'Task not found'}), 404
  return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)