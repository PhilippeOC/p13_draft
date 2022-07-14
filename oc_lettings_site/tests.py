import pytest
# import re
from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

# def test_dummy():
#     assert 1


# @pytest.mark.django_db
# def test_holiday_homes():
#     client = Client()
#     path = reverse('home')
#     response = client.get(path)
#     content = response.content.decode()
#     expected_content = re.compile("<title>Holiday Homes</title>")
#     assert expected_content.search(content)
#     assert response.status_code == 200
#     assertTemplateUsed(response, "oc_lettings_site/home.html")


@pytest.mark.django_db
def test_holiday_homes():
    client = Client()
    path = reverse('home')
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Holiday Homes</title>"
    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "oc_lettings_site/home.html")
