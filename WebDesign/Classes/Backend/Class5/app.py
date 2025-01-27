from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/health")
def healthCheck():
  return jsonify({"health": "OK"})

@app.route("/products")
def get_products():
  products = [{
    "id": 1,
    "name": "Laptop"
  }, {
    "id": 2,
    "name": "Mouse"
  }, {
    "id": 3,
    "name": "Keyboard"
  }, {
    "id": 4,
    "name": "Monitor"
  }, { 
    "id": 5,  
    "name": "Headphones"
  }, {
    "id": 6,
    "name": "Microphone"
  }, {
    "id": 7,
    "name": "Webcam"
  }, {
    "id": 8,
    "name": "USB Hub"
  }, {
    "id": 9,
    "name": "External Hard Drive"
  }, {
    "id": 10,
    "name": "Printer"
  }, {
    "id": 11,
    "name": "Scanner"
  }, {
    "id": 12,
    "name": "Speakers"
  }, {
    "id": 13,
    "name": "Projector"
  }, {
    "id": 14,
    "name": "Tablet"
  }, {
    "id": 15,
    "name": "Smartphone"
  }]
  return jsonify(products)

@app.route('/add-product', methods=['POST'])
def add_product():
  product = request.json
  return jsonify({"message": "Product added successfully", "product": product})

@app.route('/update/<int:pid>', methods=['PUT'])
def update_product(pid):
  updated_data = request.json
  return jsonify({"message": f"Product {pid} updated successfully", "product": updated_data})

@app.route('/delProduct/<int:pid>', methods=['DELETE'])
def delete_product(pid):
  try: 
    return jsonify({"message": f"Product with ID {pid} deleted successfully"})
  except:
    return jsonify({"message": "Wrong Data Format"})

if __name__ == '__main__':
    app.run(debug=True)