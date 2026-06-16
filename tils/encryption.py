import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

# Fallback token for local testing; production requires a secure 32-byte key
ENRECO_KEY = os.getenv("STORAGE_ENCRYPTION_KEY", Fernet.generate_key().decode())
cipher = Fernet(ENRECO_KEY.encode())

def encrypt_data_packet(plain_text: str) -> str:
    """Encrypts raw data strings to protect information stored at rest."""
    if not plain_text:
        return ""
    return cipher.encrypt(plain_text.encode()).decode()

def decrypt_data_packet(cipher_text: str) -> str:
    """Decrypts secure storage blocks back into plain text strings."""
    if not cipher_text:
        return ""
    return cipher.decrypt(cipher_text.encode()).decode()
