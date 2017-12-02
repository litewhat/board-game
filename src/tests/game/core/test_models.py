from unittest import TestCase

from game.core.models import Model


class ModelTestCase(TestCase):
    def test_model_attributes(self):
        m = Model(name='Some test string', age=1, timeout=3)
        self.assertEqual(m.name, 'Some test string')
        self.assertEqual(m.age, 1)
        self.assertEqual(m.timeout, 3)
