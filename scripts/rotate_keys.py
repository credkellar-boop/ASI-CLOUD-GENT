import os
from cryptography.fernet import Fernet

def execute_key_rotation():
    print("🔄 Generating secondary cryptographic storage token...")
    new_key = Fernet.generate_key().decode()
    
    print("\nAction Required: Update your production infrastructure deployment configuration.")
    print(f"STORAGE_ENCRYPTION_KEY='{new_key}'")
    print("Ensure to run data re-encryption scripts if shifting legacy cold data stores.")

if __name__ == "__main__":
    execute_key_rotation()
