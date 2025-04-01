from flask import Flask, render_template, request, url_for, jsonify, redirect
from models import db, Student
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/', methods=['GET'])
def home():
    students = Student.query.all()
    print("the students are: ", students)
    if(students is None):
        print("No entry")
        return render_template("index.html", error="No entries found", students=[] )
    return render_template("index.html", students = list(students)), 200
    


@app.route('/students', methods=['POST'])
def add_student():
    print("Endpoint recieved")
    data  = request.get_json()    
    name = data.get("name")
    email = data.get("email")
    print(name, email)
    if name and email:    
        student = Student(name=name, email=email)
        db.session.add(student)
        db.session.commit()
        return jsonify({"message":"student data added!"}), 201
    else:
        return jsonify({"error":"student data not added!"}), 400
        

@app.route('/students/<int:id>', methods=['DELETE'])
def delStudent(id):
    print("id to be deleted:", id)
    print("type of the id:", type(id))

    student = Student.query.get(id)
    if(student is None):
        return jsonify({"error": "Student not found", "message":"student data not found!"}), 404
    db.session.delete(student)
    db.session.commit()
    
    return jsonify({"message":"student data deleted!"}), 200

@app.route('/students/<int:id>', methods=['PUT'])
def updateStudent(id):
    print("Endpoint reached")
    print("id to be updated:", id)
    print("type of the id:", type(id))
    data  = request.get_json()
    name = data.get("name")
    email = data.get("email")
    print(name, email)

    student = Student.query.get(id)
    if(student is None):
        return jsonify({"error": "Student not found", "message":"student data not found!"}), 404
    student.name = name
    student.email = email
    db.session.commit()
    return jsonify({"message":"student data updated!"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


