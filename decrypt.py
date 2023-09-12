import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet
import os
import threading

# Function to generate a list of random Fernet keys
def generate_fernet_keys(num_keys):
    keys = [Fernet.generate_key() for _ in range(num_keys)]
    return keys

# Function to perform brute force decryption with a list of keys
def brute_force_decrypt(file_path, keys):
    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        for key in keys:
            cipher_suite = Fernet(key)
            try:
                decrypted_data = cipher_suite.decrypt(encrypted_data)
                print("Decryption succeeded with key:", key.hex())
                return decrypted_data
            except Exception as e:
                pass  # Decryption failed with this key, continue trying

        print("Brute force decryption completed. Key not found.")
        return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None

# Create a Tkinter file dialog for selecting the encrypted file
root = tk.Tk()
root.withdraw()  # Hide the root window
file_path = filedialog.askopenfilename(title="Select an encrypted file")

if file_path:
    num_keys = 1000  # Number of keys to pre-generate and test
    keys = generate_fernet_keys(num_keys)
    
    # Split keys into batches for parallel processing
    batch_size = 100  # Adjust batch size as needed
    key_batches = [keys[i:i+batch_size] for i in range(0, len(keys), batch_size)]

    # Use threads for parallel processing
    threads = []
    for key_batch in key_batches:
        thread = threading.Thread(target=brute_force_decrypt, args=(file_path, key_batch))
        threads.append(thread)

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Close the Tkinter window (optional)
root.destroy()
