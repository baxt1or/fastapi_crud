import pytest 
from fastapi.testclient import TestClient
from main import app
from db import Base, engine
from sqlalchemy.orm import sessionmaker

client = TestClient(app)

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

@pytest.fixture(scope="function")
def override_get_db():
    
    SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


def test_create_item(override_get_db):

    item_data = {
        "name":"Name",
        "description":"Cool and Nice", 
        "price": 12.3
    }

    response = client.post("/items", json=item_data)

    assert response.status_code == 201
    
    response_data = response.json()

    assert "id" in response_data
    assert response_data["name"] == item_data["name"]
    assert response_data["description"] == item_data["description"]
    assert response_data["price"] == item_data["price"]

    assert "created_at" in response_data
    assert "updated_at" in response_data

    assert response_data["created_at"] is not None
    assert response_data["updated_at"] is not None



def test_no_item(override_get_db):

    response = client.get("/items")

    assert response.status_code == 404
    assert response.json() == {"detail":"No items created yet."}

def test_get_item(override_get_db):

    item_data = {
        "name":"Name",
        "description":"Cool and Nice", 
        "price": 12.3
    }

    client.post("/items", json=item_data)

    response = client.get("/items")

    assert response.status_code == 200
    response_data = response.json()

    assert isinstance(response_data, list)
    assert len(response_data) == 1

    assert response_data[0]["name"] == item_data["name"]
    assert response_data[0]["description"] == item_data["description"]
    assert response_data[0]["price"] == item_data["price"]