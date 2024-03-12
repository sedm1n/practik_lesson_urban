import os
import time

directory = '.'
for root, dir, files in os.walk(directory):
    if files:
        for file in files:
            file_path = os.path.join(root, file)
            file_time = time.ctime(os.path.getmtime(file_path))
            file_size = os.path.getsize(file_path)
            print(f"Обнаружен файл {file} изменен {file_time} \
                  размер {file_size}\nрод-кая дир. {os.path.dirname(file_path)}\
                  \nПолный путь {file_path}")


