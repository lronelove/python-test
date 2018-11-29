import HtmlTestRunner
import unittest
import json
from test_case import myDict
from post_test.base_post import post_ajax

for item in myDict['post']:
    print(item)

class TestStringMethods(unittest.TestCase):
    """ Example test for HtmlRunner. """
    def test_postman_post(self):
        for item in myDict['post']:
            data = post_ajax(item['url'], item['payload'])
            data = json.loads(data)
            self.assertEqual(data, { 'username': 'jack', 'password': 'jack'})

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
