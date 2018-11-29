import HtmlTestRunner
import unittest
import json
from postman import get_ajax
from postjson import get_ajax_json
from posttest import post_test

class TestStringMethods(unittest.TestCase):
    """ Example test for HtmlRunner. """
    def test_post_test(self):
        live = post_test()
        live = json.loads(live)
        self.assertEqual(live, { 'username': 'jack', 'password': 'jack' })

    def test_postman_json(self):
        love = get_ajax_json()
        love = json.loads(love)
        self.assertEqual(love, {'code': 0, 'msg': 'hello world'})

    def test_postman(self):
        data = get_ajax()
        self.assertEqual(data, 'hello world')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_error(self):
        """ This test should be marked as error one. """
        raise ValueError

    def test_fail(self):
        """ This test should fail. """
        self.assertEqual(1, 2)

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
