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

@app.route('/checkout', methods=['POST'])
def checkout():
    global CURRENT_ORDER_COUNT
    user_id = request.json.get("user_id")
    discount_code = request.json.get("discount_code", None)
    
    if user_id not in data["carts"]:
        return jsonify({"error": "Cart is empty"}), 400
    
    cart = data["carts"].pop(user_id)
    total = sum(item["price"] * item["quantity"] for item in cart)
    discount = 0
    
    if discount_code:
        valid_code = next((d for d in data["discounts"] if d["code"] == discount_code and not d["used"]), None)
        if valid_code:
            discount = total * 0.1
            valid_code["used"] = True
        else:
            return jsonify({"error": "Invalid or already used discount code"}), 400
    
    final_total = total - discount
    data["orders"].append({
        "user_id": user_id,
        "total": total,
        "discount": discount,
        "final_total": final_total,
    })
    CURRENT_ORDER_COUNT += 1
    return jsonify({"message": "Order placed successfully", "final_total": final_total}), 200

@app.route('/admin/discount', methods=['POST'])
def generate_discount():
    global CURRENT_ORDER_COUNT
    if CURRENT_ORDER_COUNT % NTH_ORDER == 0:
        code = str(uuid.uuid4())[:8]
        data["discounts"].append({"code": code, "order_id": None, "used": False})
        return jsonify({"message": "Discount code generated", "code": code}), 200
    return jsonify({"message": "Discount code not generated"}), 400

@app.route('/admin/summary', methods=['GET'])
def order_summary():
    total_revenue = sum(order["final_total"] for order in data["orders"])
    total_discount = sum(order["discount"] for order in data["orders"])
    return jsonify({
        "total_items": len(data["orders"]),
        "total_revenue": total_revenue,
        "total_discount": total_discount,
        "discount_codes": data["discounts"],
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
