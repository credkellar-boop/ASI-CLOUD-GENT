import sys
from uagents.crypto import generate_keypair

def mint_secure_agent_credentials():
    print("🔐 Compiling new cryptographic key sets for the ASI network...")
    
    # Generate cryptographic private/public keys
    private_key, public_key = generate_keypair()
    
    print("\n--- COPY DATA BELOW INTO YOUR SECURE LOCAL .env FILE ---")
    print(f'ASI_AGENT_SEED="{private_key}"')
    print("------------------------------------------------------\n")
    print("Keep this string safe. Do not commit this string to any public git repositories.")

if __name__ == "__main__":
    mint_secure_agent_credentials()
