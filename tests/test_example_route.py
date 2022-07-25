from app import create_app
import pytest


@pytest.fixture
def app():
    app = create_app()
    return app


def test_example_route(app):
    response = app.test_client().get("/")

    assert response.status_code == 200
