from django.test import Client, TestCase


class StaticUrlTests(TestCase):
    def test_about_endpoint(self):
        # Делаем запрос к главной странице и проверяем статус
        response = Client().get("/about/")
        # Утверждаем, что для прохождения теста код должен быть равен 200
        self.assertEqual(response.status_code, 200)
