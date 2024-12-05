from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory store
data = {
    "carts": {},  # user_id -> [{"item_id": ..., "quantity": ..., "price": ...}, ...]
    "orders": [],  # [{"user_id": ..., "total": ..., "discount": ..., "final_total": ...}]
    "discounts": [],  # [{"code": ..., "order_id": ..., "used": ...}]
}

NTH_ORDER = 5
CURRENT_ORDER_COUNT = 0

@app.route('/cart', methods=['POST'])
def add_to_cart():
    user_id = request.json.get("user_id")
    item = {
        "item_id": request.json.get("item_id"),
        "quantity": request.json.get("quantity"),
        "price": request.json.get("price"),
    }
    data["carts"].setdefault(user_id, []).append(item)
    return jsonify({"message": "Item added to cart"}), 200


if __name__ == '__main__':
    app.run(debug=True)
