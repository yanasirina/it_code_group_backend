from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from core import models


class Register(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_not_allowed(self):
        """Тестирование get-запроса при регистрации"""
        response = self.client.get(reverse('core:user_register'))
        print('Response code', response.status_code)
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED,
            'GET-запрос должен выбрасывать ошибку 405'
        )

    def test_success_registration(self):
        """Тестирование post-запроса при регистрации"""
        data = {'username': 'test_user', 'password': 'test_password'}

        response = self.client.post(
            path=reverse('core:user_register'),
            data=data
        )

        print('Response code', response.status_code)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            'GET-запрос должен выдавать код 201'
        )
        user = models.User.objects.filter(username=data['username']).first()

        self.assertTrue(
            user,
            'Пользователь не был создан'
        )

        self.assertTrue(
            user.check_password(data['password']),
            'Неверно добавлен пароль'
        )

