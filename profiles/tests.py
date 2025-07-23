from __future__ import annotations

# import pytest
# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status


# @pytest.mark.django_db
# def test_register_user(client):
#     url = reverse('register')
#     data = {
#         'email': 'abc@example.com',
#         'password': 'securepassword123',
#         'first_name': 'Test',
#         'last_name': 'User',
#         'username': 'abc123',
#     }

#     response = client.post(url, data, format='json')
#     assert response.status_code == status.HTTP_201_CREATED

#     user = get_user_model().objects.get(email='abc@example.com')
#     assert user.first_name == 'Test'
#     assert user.last_name == 'User'
#     assert user.email == 'abc@example.com'
#     assert user.username == 'abc123'
#     assert user.check_password('securepassword123')


# @pytest.mark.django_db
# def test_register_user_invalid_email(client):
#     url = reverse('register')
#     data = {
#         'email': 'invalidemail',
#         'password': 'securepassword123',
#         'first_name': 'Test',
#         'last_name': 'User',
#         'username': 'abc123',
#     }

#     response = client.post(url, data, format='json')
#     assert response.status_code == status.HTTP_400_BAD_REQUEST
#     assert 'email' in response.data


# @pytest.mark.django_db
# def test_login_user(client):
#     user = get_user_model().objects.create_user(
#         email='abc@example.com',
#         password='securepassword123',
#         first_name='Test',
#         last_name='User',
#         username='abc123',
#     )

#     url = reverse('login')
#     data = {
#         'email': 'abc@example.com',
#         'password': 'securepassword123',
#     }

#     response = client.post(url, data, format='json')
#     assert response.status_code == status.HTTP_200_OK
#     assert 'access_token' in response.data
#     assert 'refresh_token' in response.data


# @pytest.mark.django_db
# def test_login_user_invalid_credentials(client):
#     user = get_user_model().objects.create_user(
#         email='abc@example.com',
#         password='securepassword123',
#         first_name='Test',
#         last_name='User',
#         username='abc123',
#     )

#     url = reverse('login')
#     data = {
#         'email': 'abc@example.com',
#         'password': 'wrongpassword',
#     }

#     response = client.post(url, data, format='json')
#     assert response.status_code == status.HTTP_401_UNAUTHORIZED
