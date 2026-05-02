from app import app
import json

def test_home():
    client = app.test_client()
    responce = client.get("/")
    assert responce.status_code == 200


def test_predict():
    client = app.test_client()

    data = {"a": 2 , "b": 3}

    responce = client.post(
        "/predict" ,
        data = json.dump(data),
        content_type = "application/json"

    )

    result = responce.get_json()

    assert result["result"] == 5
    