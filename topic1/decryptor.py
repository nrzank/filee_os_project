import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

encrypted_reports_folder = r'spy_reports'
decrypted_reports_folder = r'decrypted_reports'

encryption_key = os.getenv('ENCRYPTION_KEY')
cipher_suite = Fernet(encryption_key.encode())

files_to_check = [
    b'01_10_2023_cachalot.txt',
    b'03_10_2023_whale.txt',
    b'06_10_2023 cheetah.txt',
    b'07_10_2023 gorilla.txt',
    b'10_10_2023_dolphin.txt',
    b'13_10_2023 tiger.txt',
    b'18_10_2023_elephant.txt',
    b'19_10_2023 _giraffe.txt',
    b'21_10_2023_penguin.txt',
    b'28_10_2023 _koala.txt'
]
try:
    if not os.path.exists(decrypted_reports_folder):
        os.makedirs(decrypted_reports_folder)

    for file_name in files_to_check:
        report_path = os.path.join(encrypted_reports_folder, file_name.decode())

        if os.path.exists(report_path):
            with open(report_path, 'rb') as file:
                encrypted_data = file.read()

            decrypted_data = cipher_suite.decrypt(encrypted_data)
            decrypted_report_path = os.path.join(decrypted_reports_folder, file_name.decode())
            with open(decrypted_report_path, 'wb') as file:
                file.write(decrypted_data)
        else:
            print(f'Отчет {file_name.decode()} не найден')
except FileNotFoundError:
    print('Файл не найден!')
except Exception as e:
    print('Ошибка при оброботе файла')

print('Все отчеты проверены и обработаны')
