from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256c
import os

PRIVATE_KEY_FILE = os.path.expanduser("~/.ssh/my_keypair")

ENCRYPTED_MESSAGE_FILE = "visitor_message.enc"

with open(PRIVATE_KEY_FILE, "r", encoding="utf8") as key_file:
    private_key = RSA.import_key(key_file.read())

ENCRYPTED_MESSAGE_FILE = "visitor_message.enc"

with open(ENCRYPTED_MESSAGE_FILE, "rb") as f:
    encrypted_message_from_file = f.read()

private_key_cipher = PKCS1_OAEP.new(private_key, hashAlgo=SHA256)

decrypted_message = private_key_cipher.decrypt(encrypted_message_from_file)
print(f"Decrypted message: {decrypted_message.decode('utf-8')}")

