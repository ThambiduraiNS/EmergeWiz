from cryptography.fernet import Fernet
from django.conf import settings
import base64
import os

def get_key():
    """
    Load the base64 encoded encryption key from the file specified in settings.
    Returns the decoded key as bytes.
    """
    try:
        key_file_path = settings.ENCRYPTION_KEY_FILE
        print(f"Loading key from: {key_file_path}")
        
        if not os.path.exists(key_file_path):
            raise FileNotFoundError("Encryption key file does not exist.")
        
        with open(key_file_path, 'rb') as key_file:
            encoded_key = key_file.read()
            print(f"Encoded key: {encoded_key}")  # Debugging statement

            # If the key is stored as base64, decode it
            try:
                key = base64.urlsafe_b64decode(encoded_key)
            except base64.binascii.Error as e:
                raise Exception(f"Error decoding the base64 key: {e}")

            print(f"Decoded key: {key}")  # Debugging statement
            return key

    except FileNotFoundError as e:
        raise Exception(f"Encryption key file not found: {e}")
    except IOError as e:
        raise Exception(f"Error reading the encryption key file: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error: {e}")

def encrypt_password(password):
    """
    Encrypt a password using the loaded key.
    
    Args:
        password (str): The password to encrypt.
    
    Returns:
        bytes: The encrypted password.
    """
    try:
        key = get_key()
        print(f"Using key: {key}")
        print(f"Password to encrypt: {password}")

        fernet = Fernet(key)
        encrypted_password = fernet.encrypt(password.encode())
        print(f"Encrypted password: {encrypted_password}")  # Debugging statement

        return encrypted_password

    except Exception as e:
        raise Exception(f"Error encrypting password: {e}")

def decrypt_password(encrypted_password):
    """
    Decrypt a password using the loaded key.
    
    Args:
        encrypted_password (bytes): The encrypted password to decrypt.
    
    Returns:
        str: The decrypted password.
    """
    try:
        key = get_key()
        fernet = Fernet(key)

        decrypted_password = fernet.decrypt(encrypted_password).decode()
        # print(f"Decrypted password: {decrypted_password}")  # Debugging statement

        return decrypted_password

    except Exception as e:
        raise Exception(f"Error decrypting password: {e}")

encrypted_password = b'gAAAAABmsgFh-fP_Ia6kOk6Vy7PZu8qF7ujnbd55Wn6dKnG0ZMfMwpMOOxvIgiS4jX2t_yzJoN9QbazItaPzC-oQn52jFm5wqQ=='
# print(decrypt_password(encrypted_password))