import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet
import logging

# Configure logging
logging.basicConfig(filename='encryption.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def generate_key():
    try:
        key = Fernet.generate_key()
        return key
    except Exception as e:
        logging.error(f"Key generation failed: {str(e)}")
        raise

def save_key_to_file(key, filename):
    try:
        with open(filename, "wb") as key_file:
            key_file.write(key)
    except Exception as e:
        logging.error(f"Failed to save key to file: {str(e)}")
        raise

def load_key_from_file(filename):
    try:
        with open(filename, "rb") as key_file:
            key = key_file.read()
        return key
    except Exception as e:
        logging.error(f"Failed to load key from file: {str(e)}")
        raise

def encrypt_file(input_file, output_file, key):
    try:
        cipher_suite = Fernet(key)
        with open(input_file, "rb") as file:
            file_data = file.read()
        encrypted_data = cipher_suite.encrypt(file_data)
        with open(output_file, "wb") as file:
            file.write(encrypted_data)
    except Exception as e:
        logging.error(f"Encryption failed: {str(e)}")
        raise

def decrypt_file(input_file, output_file, key):
    try:
        cipher_suite = Fernet(key)
        with open(input_file, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        with open(output_file, "wb") as file:
            file.write(decrypted_data)
    except Exception as e:
        logging.error(f"Decryption failed: {str(e)}")
        raise

def select_file():
    try:
        file_path = filedialog.askopenfilename()
        return file_path
    except Exception as e:
        logging.error(f"File selection failed: {str(e)}")
        raise

def main():
    choice = input("Choose an option (1 for encryption, 2 for decryption): ")
    
    try:
        if choice == "1":
            # Encryption
            input_file = select_file()
            if not input_file:
                return

            output_file = filedialog.asksaveasfilename()
            if not output_file:
                return

            key = generate_key()
            save_key_to_file(key, "encryption_key.key")

            encrypt_file(input_file, output_file, key)

            print("Encryption complete. The encryption key is saved in 'encryption_key.key'.")

        elif choice == "2":
            # Decryption
            input_file = select_file()
            if not input_file:
                return

            output_file = filedialog.asksaveasfilename()
            if not output_file:
                return

            key = load_key_from_file("encryption_key.key")

            decrypt_file(input_file, output_file, key)

            print("Decryption complete.")

        else:
            print("Invalid choice. Please choose 1 for encryption or 2 for decryption.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    main()
