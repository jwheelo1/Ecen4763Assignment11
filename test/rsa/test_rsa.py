"""test rsa implementation."""

import unittest

from cryptography.rsa import rsa


class RSATest(unittest.TestCase):
    """Class TowerTest."""

    def setUp(self):
        """setUp."""
        self.rsa = rsa.RSA()

    def test_rsa(self):
        """pointless test."""
        self.assertEqual(0, 0)
