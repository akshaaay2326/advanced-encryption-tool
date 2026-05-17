from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import scrypt
import os

# Generate AES key from password
def generate_key(password, salt):
    key = scrypt(password, salt, 32, N=2**14, r=8, p=1)
    return key

# Encrypt File
def encrypt_file(file_name, password):
    salt = get_random_bytes(16)
    key = generate_key(password.encode(), salt)

    cipher = AES.new(key, AES.MODE_GCM)

    with open(file_name, 'rb') as f:
        data = f.read()

    ciphertext, tag = cipher.encrypt_and_digest(data)

    encrypted_file = file_name + ".enc"

    with open(encrypted_file, 'wb') as f:
        f.write(salt)
        f.write(cipher.nonce)
        f.write(tag)
        f.write(ciphertext)

    print(f"File encrypted successfully: {encrypted_file}")

# Decrypt File
def decrypt_file(file_name, password):
    with open(file_name, 'rb') as f:
        salt = f.read(16)
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    key = generate_key(password.encode(), salt)

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    data = cipher.decrypt_and_verify(ciphertext, tag)

    decrypted_file = "decrypted_" + file_name.replace(".enc", "")

    with open(decrypted_file, 'wb') as f:
        f.write(data)

    print(f"File decrypted successfully: {decrypted_file}")

# Main Menu
print("===== Advanced Encryption Tool =====")
print("1. Encrypt File")
print("2. Decrypt File")

choice = input("Enter choice: ")

file_name = input("Enter file name with extension: ")
password = input("Enter password: ")

if choice == '1':
    encrypt_file(file_name, password)

elif choice == '2':
    decrypt_file(file_name, password)

else:
    print("Invalid Choice")