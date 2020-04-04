from django.test import Client


def test_home(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200
