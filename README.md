# File Encryption and Decryption Tool
# Overview
This is a Python script that provides a simple graphical user interface (GUI) for encrypting and decrypting files. It uses the cryptography library to perform encryption and decryption operations. The program allows you to choose files for encryption or decryption and securely manages encryption keys.

# Features
Encryption of any file type.
Decryption of previously encrypted files.
Random key generation for each encryption operation.
Secure storage of encryption keys in a separate key file.
Error handling and logging for robustness.
Simple GUI for file selection.
# Getting Started
# Prerequisites
- Python 3.x
- Cryptography library
# Installation
1. Clone this GitHub repository to your local machine:
git clone https://github.com/musondaAlexander/simple_word_document_encryption_in_python.git
2. pip install cryptography
# Usage
1. python tk_encryption.py
2. Choose an option:

- Enter 1 for encryption.
- Enter 2 for decryption.
Follow the prompts in the GUI to select input and output files.

3. The program will generate a random encryption key for encryption and save it to a file named encryption_key.key. Make sure to keep this file secure.

4. For decryption, load the encryption key from encryption_key.key.

5. Encrypted files will have the .enc extension.

6. The program logs events and errors to a file named encryption.log.

# Note
- I added a decrypt file that tries to decrypt the file without providing the key and it shows that the algorithm is Very reliable because i failed to decrypt it on my machine. If You know a way to do this you can write to me on my email. musondaalexander97@gmail.com  

# Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests if you have suggestions, improvements, or bug fixes.



