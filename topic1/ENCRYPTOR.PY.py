from cryptography.fernet import Fernet
import os


encrypted_folder_path = 'encrypted_reports'
if not os.path.exists(encrypted_folder_path):
    os.makedirs(encrypted_folder_path)


key = Fernet.generate_key()
fernet = Fernet(key)


def encrypt_file(file_path, encrypted_folder_path, fernet):
    with open(file_path, 'rb') as file:
        data = file.read()


    encrypted_data = fernet.encrypt(data)

    encrypted_file_path = os.path.join(encrypted_folder_path, os.path.basename(file_path))
    with open(encrypted_file_path, 'wb') as file:
        file.write(encrypted_data)


def encrypt_files_without_c(folder_path, encrypted_folder_path, fernet):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt") and 'c' not in filename.lower():
            file_path = os.path.join(folder_path, filename)
            print(f"Encrypting file: {file_path}")
            encrypt_file(file_path, encrypted_folder_path, fernet)


key_file_path = 'encryption_key.key'
with open(key_file_path, 'wb') as key_file:
    key_file.write(key)


folder_path = 'decrypted_reports'
encrypt_files_without_c(folder_path, encrypted_folder_path, fernet)
