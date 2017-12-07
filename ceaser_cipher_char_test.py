import unittest
from unittest_data_provider import data_provider
from ceaser_cipher_char import Ceaser_cipher_char as ccc

ccc = ccc()

class TestCeaserCipherChar(unittest.TestCase):
    def test_ceaser_cipher_char(self, ciphered_value, input):
        self.assertEqual('a', ccc.genCipher('a','z'))


if __name__ == '__main__':
    unittest.main()
