from app import create_app


def test_health():
    client = create_app().test_client()
    res = client.get("/health")
    assert res.get_json()["status"] == "ok"


def test_create_and_list_notes():
    client = create_app().test_client()
    created = client.post("/notes", json={"text": "buy milk"}).get_json()
    assert created["text"] == "buy milk"
    notes = client.get("/notes").get_json()
    assert len(notes) >= 1
