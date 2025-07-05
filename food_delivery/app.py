
# app.py (same as before)
from flask import Flask, jsonify, request

app = Flask(__name__)

food_items = [
    {"id": 1, "name": "Pizza", "price": 250},
    {"id": 2, "name": "Burger", "price": 120},
    {"id": 3, "name": "Pasta", "price": 200},
    {"id": 4, "name": "samus", "price": 12},
    {"id": 5, "name": "vadpav", "price": 12}
]

@app.route('/api/foods', methods=['GET'])
def get_foods():
    return jsonify(food_items), 200

@app.route('/api/order', methods=['POST'])
def place_order():
    data = request.json
    return jsonify({
        "message": "Order placed!",
        "items": data.get('items'),
        "customer": data.get('customer')
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
