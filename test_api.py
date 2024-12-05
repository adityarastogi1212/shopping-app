import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_add_to_cart(client):
    response = client.post('/cart', json={"user_id": "user1", "item_id": "item1", "quantity": 2, "price": 100})
    assert response.status_code == 200

def test_get_cart(client):
    client.post('/cart', json={"user_id": "user1", "item_id": "item1", "quantity": 2, "price": 100})
    response = client.get('/cart', query_string={"user_id": "user1"})
    assert response.status_code == 200
    assert len(response.get_json()["cart"]) == 1

def test_checkout(client):
    client.post('/cart', json={"user_id": "user1", "item_id": "item1", "quantity": 2, "price": 100})
    response = client.post('/checkout', json={"user_id": "user1"})
    assert response.status_code == 200
    assert "final_total" in response.get_json()

def test_generate_discount_code(client):
    for i in range(5):
        client.post('/cart', json={"user_id": f"user{i}", "item_id": "item1", "quantity": 1, "price": 100})
        client.post('/checkout', json={"user_id": f"user{i}"})
    response = client.post('/admin/discount')
    assert response.status_code == 200
    assert "code" in response.get_json()

