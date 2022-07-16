import pytest
from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

from lettings.models import Address, Letting


@pytest.mark.django_db
def test_lettings_index():
    client = Client()
    path = reverse('letting_index')
    response = client.get(path)
    expected_content = "<title>Lettings</title>"
    assert expected_content in response.content.decode()
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_lettings():
    client = Client()
    address = Address.objects.create(
        number=12,
        street='rue des rosiers',
        city='lol',
        state='lol country',
        zip_code=1010,
        country_iso_code='fr')

    Letting.objects.create(
        title="Résidence Jules Verne",
        address=address)
    path = reverse('letting', kwargs={'letting_id': 1})
    response = client.get(path)
    expected_value = "<title>Résidence Jules Verne</title>"
    assert expected_value in response.content.decode()
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")
