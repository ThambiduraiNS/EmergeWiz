from cryptography.fernet import Fernet
import base64
import os

# Define the path to the key file
key_file_path = os.path.join('secure_keys', 'keyfile.key')

# Ensure the directory exists
os.makedirs(os.path.dirname(key_file_path), exist_ok=True)

# Generate a new key
key = Fernet.generate_key()

# Encode the key in base64
encoded_key = base64.urlsafe_b64encode(key)

# Save the base64-encoded key to a file
with open(key_file_path, 'wb') as key_file:
    key_file.write(encoded_key)

print(f"Key has been saved to {key_file_path}")
