"""This RSA Module can be used to Encrypt and Decrypt text using RSA algorithm."""

from random import randrange


class RSA():
    """Class represents the RSA Algorithm."""

    def __init__(self, prime_size=1024, max_iterations=10):
        """Intialize all values."""
        self.rsa = {}
        options = ['message', 'encrypted', 'decrypted', 'p', 'q', 'phi', 'e', 'n', 'd']
        for option in options:
            self.rsa[option] = None

        # todo add in more code here

    def calc_p_and_q(self, size):
        pass

    def calc_phi(self):
        pass

    def calc_e(self, phi):
        pass

    def calc_n(self):
        pass

    def mod_inv(self, number, modular):
        pass

    def gcd(self, num_one, num_two):
        pass

    def generate_prime_number(self, size):
        pass

    def is_prime(self, number):
        pass

    def get_data(self):
        """Return all data associated with RSA."""
        return self.rsa

    def get_public_key(self):
        """Return public key in tuple form (e, n)."""
        return (self.rsa['e'], self.rsa['n'])

    def get_private_key(self):
        """Return private key in tuple form (d, n)."""
        return (self.rsa['d'], self.rsa['n'])

    def encrypt(self, plain_text):
        pass

    def decrypt(self, cipher_text):
        pass
