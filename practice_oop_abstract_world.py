class Road:
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class WereHouse:
    def __init__(self, name, content):
        self.name = name
        self.content = content
        self.road_out = None
        self._set_road_out = None
        self.queue_in = []
        self.queue_out = []

    def __str__(self):
        return f"Склад {self.name}, груз {self.content}"

    def set_road_out(self, road):
        self.road_out = road

    def truck_arrived(self, truck):
        self.queue_in.append(truck)
        print(f"На склад {self.name} Прибыл грузовик {truck.name}")

    def get_next_truck(self):
        if self.queue_in:
            truck = self.queue_in.pop()
            return truck

    def truck_ready(self, truck):
        self.queue_out.append(truck)
        print(f"На складе {self.name} грузовик {truck.name}  Готов")

    def act(self):
        while self.queue_out:
            truck = self.queue_out.pop()
            truck.go_to(road=self.road_out)


class Vehicle:
    feel_rate = 0
    total_fuel = 0

    def __init__(self, model):
        self.name = model
        self.fuel = 0

    def __str__(self):
        return f"model {self.name}, fuel {self.fuel} "

    def act(self):
        if self.fuel < 10:
            self.tank_up()
            return False
        return True
    def tank_up(self):
        # заправляемся
        self.fuel += 1000
        Vehicle.total_fuel += 1000
        print(f"Tank up {self.name}, fuel {self.fuel} ")


class Truck(Vehicle):
    fuel_rate = 50
    daed_time = 0
    def __init__(self, model, body_space=1000):
        super().__init__(model=model)
        self.model = model
        self.body_space = body_space
        self.cargo = 0
        self.velocity = 100
        self.place = None
        self.distance_to_target = 0

    def __str__(self):
        res = super().__str__()
        return res + f" груза {self.cargo} "
        pass

    def ride(self):
        self.fuel -= self.fuel_rate
        if self.distance_to_target > self.velocity:
            self.distance_to_target -= self.velocity
            print(f"{self.model} едет по дороге, ostalos {self.distance_to_target}")
        else:
            self.place = self.place.end
            self.place.truck_arrived(self)
            print(f"{self.model} доехал ")

    def go_to(self, road):
        self.place = road
        self.distance_to_target = road.distance
        print(f"{self.model} выехал")


    def act(self):
        if super().act():
            if isinstance(self.place, Road):
                self.ride()
            else:
                Truck.daed_time +=1


class AutoLoader(Vehicle):
    fuel_rete = 30
    def __init__(self, model, backet_capacity=100, werehouse=None, role='loader'):
        super().__init__(model=model)
        self.model = model
        self.backet_capacity = backet_capacity
        self.wherehouse = werehouse
        self.role = role
        self.truck = None

    def __str__(self):
        res = super().__str__()
        return res + f" груза {self.truck}"

    def act(self):
        if self.fuel < 10:
            self.tank_up()
        elif self.truck is None:
            self.truck = self.wherehouse.get_next_truck()
            print(f"{self.model} Vzyal {self.truck}")
        elif self.role == 'loader':
            self.load()
        else:
            self.unload()

    def load(self):
        if self.wherehouse.content == 0:
            print(f"Sklad {self.wherehouse} pustoi")
            if self.truck:
                self.wherehouse.truck_ready(self)
                self.truck = None
            return

        self.fuel -= self.fuel_rete
        truck_cargo_rest = self.truck.body_space - self.truck.cargo

        if truck_cargo_rest >= self.backet_capacity:
            cargo = self.backet_capacity# self.wherehouse.content -= self.backet_capacity
            # self.truck.cargo += self.backet_capacity
        else:
            cargo = truck_cargo_rest
            if self.wherehouse.content < cargo:
                cargo = self.wherehouse.content
                self.wherehouse.content -= cargo
                self.truck.cargo += cargo
                print(f"{self.model} Gruzit {self.truck}")
        if self.truck.cargo == self.truck.body_space:
            self.wherehouse.truck_ready(self.truck)
            self.truck = None

    def unload(self):
        self.fuel -= self.fuel_rete
        if self.truck.cargo >= self.backet_capacity:
            self.wherehouse.content += self.backet_capacity
            self.truck.cargo -= self.backet_capacity
        else:
            self.wherehouse.content -= tself.truck.cargo
            self.truck.cargo += self.truck.cargo
            print(f"{self.model} Ruzgruzil {self.truck}")
        if self.truck.cargo == 0:
            self.wherehouse.truck_ready(self.truck)
            self.truck = None


TOTAL_CARGO = 100000
moscow = WereHouse(name='Moscow', content=TOTAL_CARGO)
piter = WereHouse(name='Piter', content=0)

moscow_piter = Road(moscow, piter, 700) #инициализация дороги
piter_moscow = Road(piter, moscow, 700)

# выгружаем со склада
moscow.set_road_out(moscow_piter)
piter.set_road_out(piter_moscow)

# Погрузчики
loader_1 = AutoLoader(model='BobCat', backet_capacity=1000, werehouse=moscow, role='loader')
loader_2 = AutoLoader(model='Jewtlin', backet_capacity=100, werehouse=piter, role='unloader')

truck_1 = Truck(model='Kamaz', body_space=6000)
truck_3 = Truck(model='Volvo', body_space=4000)
truck_2 = Truck(model='Gaz', body_space=2000)

moscow.truck_arrived(truck_1)
moscow.truck_arrived(truck_2)
moscow.truck_arrived(truck_3)

hour = 0

while piter.content < TOTAL_CARGO:
    hour += 1
    print('---------------------------{}'.format(hour))

    truck_1.act()
    truck_2.act()
    truck_3.act()
    loader_1.act()
    loader_2.act()
    moscow.act()
    piter.act()
    print(truck_1)
    print(truck_2)
    print(truck_3)
    print(moscow)
    print(piter)


print(f"Vsego topliva {Vehicle.total_fuel}")
