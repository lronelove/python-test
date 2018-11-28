import unittest

class NamesTestCase(unittest.TestCase):
    def test_fullname(self):
        fullname = get_fullname('jack', 'rose')
        self.assertEqual(fullname, 'jack rose')

unittest.main()


