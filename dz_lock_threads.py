#
# Задание:
# Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием
# механизма блокировки потоков.
#
# Класс BankAccount должен отражать банковский счет с балансом и методами для
# пополнения и снятия денег. Необходимо использовать механизм блокировки,
# чтобы избежать проблемы гонок (race conditions) при модификации общего ресурса.
import threading
from threading import Thread


class BankAccount():
    amount = 0

    def deposit(self, amount, lock):
        with lock:
            BankAccount.amount += amount
        print(f"Deposited {amount}, new balance is {BankAccount.amount}")

    def withdraw(self, amount, lock):
        with lock:
            BankAccount.amount -= amount
        print(f"Withdrew {amount}, new balance is {BankAccount.amount}")


# Пример работы:
def deposit_task(account, amount, lock):
    for _ in range(5):
        account.deposit(amount,lock=lock)


def withdraw_task(account, amount,lock):
    for _ in range(5):
        account.withdraw(amount, lock)


account = BankAccount()
lock = threading.Lock()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100, lock))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 50, lock))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

# Вывод в консоль:
# Deposited 100, new balance is 1100
# Deposited 100, new balance is 1200
# Deposited 100, new balance is 1300
# Deposited 100, new balance is 1400
# Deposited 100, new balance is 1500
# Withdrew 150, new balance is 1350
# Withdrew 150, new balance is 1200
# Withdrew 150, new balance is 1050
# Withdrew 150, new balance is 900
# Withdrew 150, new balance is 750
#
#
# Примечание:
# Используйте класс Lock из модуля threading для блокировки доступа к общему ресурсу.
# Ожидается создание двух потоков, один для пополнения счета, другой для снятия денег.
# Используйте with (lock object): в начале каждого метода, чтобы использовать блокировку
