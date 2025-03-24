from app.main import app

def test_hello():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.data == b"I LOVEEE YOUUU PYAARRII TANNUUUUU\u2764\uFE0F \u2764\uFE0F \u2764\uFE0F \u2764\uFE0F"
