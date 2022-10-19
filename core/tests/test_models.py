from django.test import TestCase

from core import models
from core import factories


class Tag(TestCase):
    def setUp(self):
        self.tag = factories.Tag()

    def test_str(self):
        """Тестирование строкового преставление объекта"""
        print('Tag', self.tag.name)
        self.assertEqual(
            str(self.tag),
            self.tag.name,
            'Строковое преставление объекта должно браться из атрибута name'
        )
