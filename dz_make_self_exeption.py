
class InvalidDataExeption(Exception):
    pass

class ProcessingExeption(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Кастомная обработка {self.message}"


def generateExeptions(var1):
    if var1 == 'cod':
        raise InvalidDataExeption
    elif var1 == 'proc':
        raise ProcessingExeption('my raise')

def invalidData(var1):

    try:
        generateExeptions('cod')

    except InvalidDataExeption:
        print("Invalid data")
        raise NameError('Ошибка в имени')

def process(var1):
    try:
        generateExeptions('proc')
    except ProcessingExeption as ex:
        print("Error Processing", ex)


try:
    invalidData('cod')
except NameError as ex:
    print(f"Neme Eroor {ex}")


try:
    process('proc')
except NameError as ex:
    print(f"Neme Eroor {ex}")