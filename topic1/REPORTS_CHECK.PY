import os


def process_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            print(f"Processing file: {file_path}")
            with open(file_path, 'r') as file:
                decrypted_data = file.read()
                print(decrypted_data)

            with open(file_path, 'r') as file:
                data = file.read()
                modified_data = data.replace('Вра', 'Дру').replace('вра', 'дру')
            with open(file_path, 'w') as file:
                file.write(modified_data)

            with open(file_path, 'a') as file:
                file.write('\nПроверено!')


folder_path = r'/topic1/decrypted_reports'

process_files_in_folder(folder_path)
