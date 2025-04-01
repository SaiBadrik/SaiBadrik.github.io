from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Student.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  class_ = db.Column(db.String(50), nullable=False)
  grade = db.Column(db.Integer, nullable=False)
  roll_number = db.Column(db.Integer, nullable=False)
  marks = db.Column(db.Integer, nullable=False)

  def __init__(self, name, class_, grade, roll_number, marks):
    self.name = name
    self.class_ = class_
    self.grade = grade
    self.roll_number = roll_number
    self.marks = marks

@app.route("/students", methods=["GET"])
def get_students():
  students = Student.query.all()
  output = []
  for student in students:
    data = {"id": student.id, "name": student.name, "class": student.class_, "grade": student.grade, "roll_number": student.roll_number, "marks": student.marks}
    output.append(data)
  return jsonify({"students": output})

@app.route("/students", methods=["POST"])
def create_student():
  data = request.get_json()
  if "name" not in data or "class" not in data or "grade" not in data or "roll_number" not in data or "marks" not in data:
    return jsonify({"error": "Missing data"}), 400
  student = Student(name=data["name"], class_=data["class"], grade=data["grade"], roll_number=data["roll_number"], marks=data["marks"])
  db.session.add(student)
  db.session.commit()
  return jsonify({"message": "Inserted new data"}, {"New data is: ": data}), 201

@app.route("/students/<int:id>", methods=["GET"])
def getStudentById(id):
  student = Student.query.get(id)
  if not student:
    return jsonify({"error": "Student not found"}), 404
  else:
    return jsonify({"id": student.id, "name": student.name, "class": student.class_, "grade": student.grade, "roll_number": student.roll_number, "marks": student.marks})

@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
  student = Student.query.get(id)
  if not student:
    return jsonify({"error": "Student not found"}), 404
  data = request.get_json()
  if "name" in data:
    student.name = data["name"]
  if "class" in data:
    student.class_ = data["class"]
  if "grade" in data:
    student.grade = data["grade"]
  if "roll_number" in data:
    student.roll_number = data["roll_number"]
  if "marks" in data:
    student.marks = data["marks"]
  db.session.commit()
  return jsonify({"message": "Updated data", "New data": data}), 200

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
  student = Student.query.get(id)
  if not student:
    return jsonify({"error": "Student not found"}), 404
  data = {"id": student.id, "name": student.name, "class": student.class_, "grade": student.grade, "roll_number": student.roll_number, "marks": student.marks}
  db.session.delete(student)
  db.session.commit()
  return jsonify({"message": "Student deleted", "Student": data}), 200

if __name__ == "__main__":
  with app.app_context():
      db.create_all()
  app.run(debug=True)