from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Product.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

@app.route("/products", methods=["GET"])
def get_products():
  products = Product.query.all()
  output = []
  for product in products:
    data = {"id": product.id, "name": product.name, "price": product.price, "quantity": product.quantity}
    output.append(data)
  return jsonify({"products": output})

@app.route("/products", methods=["POST"])
def create_product():
  data = request.get_json()
  if "name" not in data or "price" not in data or "quantity" not in data:
    return jsonify({"error": "Missing data"}), 400
  product = Product(name=data["name"], price=data["price"], quantity=data["quantity"])
  db.session.add(product)
  db.session.commit()
  return jsonify({"message": "Inserted new data"}, {"New data is: ": data}), 201