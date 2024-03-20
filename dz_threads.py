import threading
from threading import Thread
from time import sleep
import string

def print_digits():
    for digit in range(1, 11):
        print(digit)
        sleep(1)

def print_letters():
    for letter in string.ascii_lowercase[:10]:
        print(letter)
        sleep(1)

if __name__ == '__main__':
    thread1 = Thread(target=print_digits)
    thread2 = Thread(target=print_letters)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()