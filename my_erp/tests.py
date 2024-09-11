from django.test import TestCase

# Create your tests here.
from .models import NomencBook


class NomencBookTest(TestCase):
    def test_id_generation(self):
        # Создаем новый экземпляр модели без id
        obj = NomencBook(name='Test Nomenclature')

        # Вызываем метод Write, который должен сгенерировать id
        obj.write()

        # Убеждаемся, что id сгенерирован
        self.assertIsNotNone(obj.id, "UUID should be generated and assigned to id field")

        # Проверяем, что длина id соответствует бинарному представлению UUID (16 байт)
        self.assertEqual(len(obj.id), 16, "id field should be 16 bytes long for BinaryField")
