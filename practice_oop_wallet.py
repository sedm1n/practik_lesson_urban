class Purse:
    def __init__(self, valuta, name = 'unknown'):
        if valuta not in ('eur','usd'):
            raise ValueError
        self.money = 0.00
        self.valuta = valuta
        self.name = name
    def top_up_balance(self, howmoney):
        self.money = self.money + howmoney
        return howmoney
    def top_down_balance(self, howmoney):
        if self.money - howmoney < 0:
            print("Не достаточно денег ")
            raise ValueError("Не достаточно денег")
        self.money = self.money - howmoney
        return howmoney
    def info(self):
        print('Money ', self.money)
    def __del__(self):
       print("Кошелек удален ", self.name)


x = Purse('usd')
y = Purse('eur', 'y')
x.top_up_balance(100)
y.top_up_balance(300)
x.top_up_balance(y.top_down_balance(9))
x.info()
y.info()
