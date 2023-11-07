# RSA - Cryptography

You will be writing your own RSA algorithm. This means you will need to calculate 2 unique prime numbers, etc.

## Getting Started Steps

- running "make setup" will install correct dependencies and check for correct python version (3.7+)
- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# RSA

## Requirements

- You must implement a class that handles the below interfaces for calculating RSA.
- The class name must be called "RSA".
- You must implement at least 14 unit tests.
- Must get a 10/10 when running "make style"
- Your unit tests must reach 100% code coverage

## Interface

- The initialization of the class must be RSA(self, prime_size=1024)
    - Within initialize create a dictionary rsa that contains {'message': None, 'encrypted': None, 'decrypted': None, 'p': None, 'q': None, 'phi': None, 'e': None, 'n': None, 'd': None}. This dictionary is used for my testing, so make sure to update any values if they may change.
    - After initializing the dictionary, call any necessary functions to initialize p, q, phi, e, n, and d. If any are invalid, they will remain None.
    - prime_size dictates the largest prime number you will be using in your encryption.
- The function encrypt(self, plain_text) return the encryption of the plain_text, update rsa['encrypted'] and rsa['message']
    - RSA gives a list of numbers for each character, so the encryption will be an array containing integers.
    - example: [274625, 159618, 300763, 218426, 328509, 279634, 357911]
- The function decrypt(self, cipher_text) return the decrypted cipher_text, update rsa['decrypted']
    - cipher_text will be in the same form as the encryption above
    - this should return a string.
- The function get_data(self) return the dictionary self.rsa
- The function get_public_key(self) return public key in tuple form (e, n)
- The function get_private_key(self) return private key in tuple form (d, n)

## Tests

- Check if the various strings can be encrypted and decrypted, resulting in the original string
- Check for values of p, q, e, and phi follow the descriptions given in the rsa slides
- Check that private and public keys are correct
- Check with various prime_size parameters

## Corner Cases

- Invalid prime sizes (<2, None)
- If initialization is invalid, encryption and decryption should return None

## Library

You can only use basic python libraries and you can use "from random import randrange".
