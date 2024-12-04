data = {
    "carts": {},  # user_id -> [{"item_id": ..., "quantity": ..., "price": ...}, ...]
    "orders": [],  # [{"user_id": ..., "total": ..., "discount": ..., "final_total": ...}]
    "discounts": [],  # [{"code": ..., "order_id": ..., "used": ...}]
}

