from http import HTTPStatus

from django.test import Client, TestCase


class StaticUrlTests(TestCase):
    def test_homepage_endpoint(self):
        # Делаем запрос к главной странице и проверяем статус
        response = Client().get("/")
        # Утверждаем, что для прохождения теста код должен быть равен 200
        self.assertEqual(response.status_code, 200)

    def test_coffee_endpoint(self):
        # Делаем запрос к главной странице и проверяем статус
        response = Client().get("/coffee/")
        self.assertEqual(response.status_code, HTTPStatus.IM_A_TEAPOT)
        self.assertEqual(response.content.decode(), "Я чайник")

