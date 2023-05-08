import pytest

from django.urls import reverse


def test_get_owner(client):
    r = client.get(reverse('core:owners-list'))
    assert r.status_code == 200
    assert type(r.json) == 'list'

