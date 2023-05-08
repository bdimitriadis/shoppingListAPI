import pytest

from django.urls import reverse


@pytest.mark.django_db
@pytest.mark.usefixtures('django_db_setup')
def test_login(client):
    test_credentials = {
        'username': 'vlad',
        'password': 'whatever123'
    }

    r = client.post(reverse('core:owner-login'), data=test_credentials)
    assert r.status_code == 200


@pytest.mark.django_db
@pytest.mark.usefixtures('django_db_setup')
def test_signup(client):
    test_credentials = {
        'username': 'vladimiros',
        'password': 'whatever123',
        'email': 'vladimiros@ddomain.com'
    }

    r = client.post(reverse('core:owner-signup'), data=test_credentials)
    assert r.status_code == 201
