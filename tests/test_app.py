from app import create_app
import pytest


@pytest.fixture
def app():
    app = create_app()
    return app


def test_index_route(app):
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert (
        "Hello, I am your blank home page, you must fill me up."
        in response.data.decode("utf-8")
    )


# def test_UNK_route(app):
#     response = app.test_client().get("/UNK")

#     assert response.status_code == 200
