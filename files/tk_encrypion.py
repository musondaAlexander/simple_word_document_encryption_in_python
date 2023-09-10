import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    return key

def save_key_to_file(key, filename):
    with open(filename, "wb") as key_file:
        key_file.write(key)

def load_key_from_file(filename):
    with open(filename, "rb") as key_file:
        key = key_file.read()
    return key

def encrypt_file(input_file, output_file, key):
    cipher_suite = Fernet(key)
    with open(input_file, "rb") as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(output_file, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(input_file, output_file, key):
    cipher_suite = Fernet(key)
    with open(input_file, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(output_file, "wb") as file:
        file.write(decrypted_data)

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])
    return file_path

def main():
    choice = input("Choose an option (1 for encryption, 2 for decryption): ")
    
    if choice == "1":
        # Encryption
        input_file = select_file()
        if not input_file:
            return
        
        output_file = filedialog.asksaveasfilename(defaultextension=".enc")
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
        
        output_file = filedialog.asksaveasfilename(defaultextension=".docx")
        if not output_file:
            return
        
        key = load_key_from_file("encryption_key.key")
        
        decrypt_file(input_file, output_file, key)
        
        print("Decryption complete.")
    
    else:
        print("Invalid choice. Please choose 1 for encryption or 2 for decryption.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    main()