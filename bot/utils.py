from cryptography.fernet import Fernet
import os

def load_key():
    return os.getenv("ENCRYPTION_KEY").encode()

def encrypt_data(data, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data.encode())
    return encrypted.decode()

def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_data.encode())
    return decrypted.decode()
