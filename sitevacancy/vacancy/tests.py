from django.test import TestCase
from django.urls import reverse


class GetPagesTestCase(TestCase):
    def setUp(self):
        "Инициализация перед выполнением каждого теста"

    def test_mainpage(self):
        path = reverse('home')
        response = self.client.get(path)
        print(response)

    def test_case_2(self):
        pass

    def tearDown(self):
        "Действие после выполнения каждого теста"
