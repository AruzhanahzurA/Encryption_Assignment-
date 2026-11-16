from pathlib import Path

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

# Load the CEU's public key
key_bytes = Path("my_keypair.pub").read_bytes()
public_key = serialization.load_ssh_public_key(key_bytes)

# Ask me (the visitor) for a short message and convert it to bytes.
message = input("Enter a short message for CEU: ").encode("utf-8")

# Encrypt the message using CEU's public key.
encrypted_message = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

Path("visitor_message.enc").write_bytes(encrypted_message)
print("Saved visitor_message.enc")