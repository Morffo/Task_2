from django.test import Client, TestCase


class StaticUrlTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_pk_endpoint(self):
        response = Client().get("/catalog/0/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_re_pk_positive_endpoint(self):
        response = Client().get("/catalog/re/9/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), str(9))

    def test_catalog_re_pk_negative_endpoint(self):
        response = Client().get("/catalog/re/-9/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_converter_pk_positive_endpoint(self):
        response = Client().get("/catalog/converter/28/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), str(28))

    def test_catalog_converter_pk_negative_endpoint(self):
        response = Client().get("/catalog/converter/-28/")
        self.assertEqual(response.status_code, 404)
