from flask import Flask, jsonify, request
app = Flask(__name__)

products = {
  1: {
    "id": 1,
    "name": "Laptop",
    "price": 1000,
    "quantity": 5
  }, 
  2: {
    "id": 2,
    "name": "Phone",
    "price": 500,
    "quantity": 3
  }, 
  3: {
    "id": 3,
    "name": "Tablet",
    "price": 600,
    "quantity": 2
  },
  4: {
    "id": 4,
    "name": "Headphones",
    "price": 200,
    "quantity": 10
  },
  5: {
    "id": 5,
    "name": "Keyboard",
    "price": 50,
    "quantity": 20
  }
}

#READ
@app.route("/products", methods=["GET"])
def get_products():
    return jsonify({"products": list(products.values())})

def get_product_by_id(pid):
    return products.get(pid, None)
#READ by ID
@app.route("/products/<int:pid>", methods=["GET"])
def get_product(pid):
    product = get_product_by_id(pid)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404
#CREATE
@app.route("/products", methods=["POST"])
def create_product():
  data = request.get_json()
  if "name" not in data or "price" not in data or "quantity" not in data:
    return jsonify({"error": "Missing data"}), 400
  pid = len(products) + 1
  data["id"] = pid
  products[pid] = data
  return jsonify({"message": "Inserted new data"}, {"New data is: ": data}), 201

#DELETE
@app.route("/products/<int:pid>", methods=["DELETE"])
def deleteProduct(pid):
  prod = products.get(pid, None)
  if prod:
    del products[pid]
    return jsonify({"message": "Product deleted", "Product": prod}), 204
  else:
    return jsonify({"error": "Product not found"}), 404

#UPDATE
@app.route("/products/<int:pid>", methods=["PUT"])
def updateProduct(pid):
  product = get_product_by_id(pid)
  if product:
    data = request.get_json()
    product.update(data)
    return jsonify({"message": "Product updated", "Product": product}), 200
  return jsonify({"error": "Product not found"}), 404


app.run(debug=True)