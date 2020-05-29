
import unittest
from full_name import full_name

class NameTestCase(unittest.TestCase):
    """Тесты для функции full_name"""

    def test_first_last_name(self):
        """Именна вида 'Андриевский Андрей' работют нормально? """
        format_name = full_name('Андриевский', 'Андрей')
        self.assertEqual(format_name, 'Андриевский Андрей')


if __name__ == "__name__":
    unittest.main()
