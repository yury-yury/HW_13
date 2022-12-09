import pytest

from app import app

def test_app_api_1():

    response = app.test_client().get('/api/posts')
    assert response.status_code == 200
    assert type(response.json) == list
    for item in response.json:
        for key in item.keys():
            assert key in ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]


def test_app_api_2():

    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200
    assert type(response.json) == dict
    for key in response.json.keys():
        assert key in ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]




