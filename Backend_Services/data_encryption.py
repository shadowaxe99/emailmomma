```python
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import os

class DataEncryption:

    def __init__(self):
        self.backend = default_backend()
        self.salt = os.urandom(16)
        self.iv = os.urandom(16)

    def generate_key(self, password):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=self.backend
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key

    def encrypt_data(self, data, key):
        f = Fernet(key)
        encrypted_data = f.encrypt(data)
        return encrypted_data

    def decrypt_data(self, encrypted_data, key):
        f = Fernet(key)
        decrypted_data = f.decrypt(encrypted_data)
        return decrypted_data

    def encrypt_data_aes(self, data, key):
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data) + padder.finalize()
        cipher = Cipher(algorithms.AES(key), modes.CBC(self.iv), backend=self.backend)
        encryptor = cipher.encryptor()
        ct = encryptor.update(padded_data) + encryptor.finalize()
        return ct

    def decrypt_data_aes(self, ct, key):
        cipher = Cipher(algorithms.AES(key), modes.CBC(self.iv), backend=self.backend)
        decryptor = cipher.decryptor()
        data = decryptor.update(ct) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        data = unpadder.update(data) + unpadder.finalize()
        return data

def encryptData():
    data_encryption = DataEncryption()
    password = b"password"
    data = b"secret data"
    key = data_encryption.generate_key(password)
    encrypted_data = data_encryption.encrypt_data(data, key)
    return encrypted_data

def decryptData(encrypted_data):
    data_encryption = DataEncryption()
    password = b"password"
    key = data_encryption.generate_key(password)
    decrypted_data = data_encryption.decrypt_data(encrypted_data, key)
    return decrypted_data
```