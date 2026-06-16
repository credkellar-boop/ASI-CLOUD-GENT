from utils.encryption import encrypt_data_packet, decrypt_data_packet

def test_data_encryption_cycle():
    """Validates that text data packets can be perfectly obfuscated and restored."""
    secret_payload = "Sensitive User Log File String 123!"
    
    encrypted = encrypt_data_packet(secret_payload)
    assert encrypted != secret_payload
    
    decrypted = decrypt_data_packet(encrypted)
    assert decrypted == secret_payload
