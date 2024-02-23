
import os

def chek_dir(root, ignore_dirs):
    for ignor in ignore_dirs:
        if ignor in root:
            return True
    return False
def get_file_list(dirpath:str):
    ignore_dirs = ('.venv', '.git', '.idea')
    python_files = []
    for root, dirs, files in os.walk(dirpath):

            if not chek_dir(root, ignore_dirs):
                [python_files.append(os.path.join(root, file)) for file in files if file.endswith('.py')]

            else:
                continue

    return python_files

def count_string(filepath:str):

   try:
        with open(filepath, 'r') as file:
            list_lines = file.readlines()
        file.close()
        cleared_list = [x for x in list_lines if x.strip() != '']
        return len(cleared_list)

   except FileExistsError:
        print('Файла не существует ')
        return 0
   except PermissionError:
        print("Нет прав на доступ к файлу ")
        return 0
    #     pass
def main():
    count_list = []
    dir_search = ""

    flag = input("""Выбирите вариант: 
    1 Подсчет в текущей деректории
    2 Подсчет в нужной директории(укажите путь к дир)
    """)

    if flag == '1':
        dir_search = os.curdir
    elif flag == '2':
        dir_search = input("Введите путь к каталогу")
    else:
        print("Не верно выбран вариант")

    list_files = get_file_list(dir_search)


    for file in list_files:
       count_list.append(count_string(file))
    print('Всего написано строк ', sum(count_list))

if __name__ == '__main__':
    main()