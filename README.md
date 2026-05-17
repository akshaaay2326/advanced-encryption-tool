# Advanced Encryption Tool

**COMPANY:** CODTECH IT SOLUTIONS
**NAME:** AKSHAY ARAVIND AV
**INTERN ID:** CTIS7815
**DOMAIN:** CYBER SECURITY & ETHICAL HACKING
**DURATION:** 12 WEEKS
**MENTOR:** NEELA SANTOSH


## Description

The Advanced Encryption Tool is a Python-based cybersecurity project developed to encrypt and decrypt files using the AES-256 algorithm. AES-256 (Advanced Encryption Standard with 256-bit key) is one of the strongest encryption standards used worldwide by governments and security professionals. In this project, the cryptography library is used to implement AES-256 encryption in a simple and user-friendly way.

The main goal of this project is to protect sensitive files from unauthorized access by converting them into an unreadable encrypted format. Only users with the correct password can decrypt and access the original file. This is important in cybersecurity because data breaches and unauthorized file access are among the most common security threats today.

The program provides a simple menu-driven interface where the user can choose to encrypt or decrypt a file. The user enters the file path and a password. The password is processed using a key derivation function (PBKDF2) to generate a secure 256-bit encryption key. The file is then encrypted using AES-256 and saved with an `.enc` extension. During decryption, the same password is used to reverse the process and recover the original file.

This project helped in understanding important concepts such as symmetric encryption, AES algorithm, key derivation, file handling, and cryptography basics. It also improved Python programming skills and knowledge of how encryption is used to protect data in real-world cybersecurity applications.


## Technologies Used
- Python 3.12
- cryptography library (Fernet / AES-256)


## Files
- `encryption_tool.py` - Main encryption and decryption script

## Installation

Install dependencies:
pip install cryptography

Run the tool:
python encryption_tool.py

## Features
- AES-256 file encryption
- AES-256 file decryption
- Password-based key generation
- Simple menu-driven interface
- Supports any file type

---

## Disclaimer
This tool is for educational purposes only.
Use responsibly and only on files you own or have permission to encrypt.

#Output

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/064858be-c0c5-4595-a58e-deab283b606b" />
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/87b03ea6-ec48-4e6b-b3b8-edda066932e7" />
