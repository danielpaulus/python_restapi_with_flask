import unittest
import logging

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.info("test")

    @classmethod
    def tearDownClass(cls):
        #cls._connection.destroy()
        logging.info("test")

    def setUp(self):
        logging.info("bla")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()