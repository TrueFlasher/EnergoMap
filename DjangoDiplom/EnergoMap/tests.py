from django.test import TestCase
from django.urls import reverse
from .models import FDData

class CFOViewTestCase(TestCase):
    def setUp(self):
        # Создаем объект FDData для тестирования
        FDData.objects.create(name="Test FDData", production=100, consumption=50)

    def test_cfo_view(self):
        # Получаем объект FDData для проверки
        test_fd_data = FDData.objects.get(name="Test FDData")

        # Проверяем, что объект FDData успешно создан
        self.assertEqual(test_fd_data.production, 100)
        self.assertEqual(test_fd_data.consumption, 50)

        # Запрашиваем представление 'CFO'
        response = self.client.get(reverse('CFO'))

        # Проверяем, что запрос завершился успешно
        self.assertEqual(response.status_code, 200)

        # Проверяем, что объект FDData передан в контекст представления
        self.assertIn('cfo_data', response.context)

        # Проверяем, что переданный объект FDData соответствует созданному
        cfo_data = response.context['cfo_data']
        self.assertEqual(cfo_data.name, "Test FDData")
        self.assertEqual(cfo_data.production, 100)
        self.assertEqual(cfo_data.consumption, 50)
