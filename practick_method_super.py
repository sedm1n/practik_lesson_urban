class Robot():
   def __init__(self, model):
       self.model = model
   def __str__(self):
       return "Class {}, Model {}".format(self.__class__.__name__, self.model)
   def operate(self):
       print("Robot go ")

class VacuumCleaningRobot(Robot):

    def __init__(self, model):
        super().__init__(model=model)
        self.dust_bug = 0
    def operate(self):
        print("Робот пылесосит пол, заполненность мешка {}".format(self.dust_bug))
class WarRobot(Robot):
    def __init__(self, model, gun):
        super().__init__(model=model)
        self.gun = gun
    def operate(self):
        super().operate()
        print("Робот охраняет", self.gun)


def main():
    robot = Robot('CP2')
    print(robot)
    vacuum = VacuumCleaningRobot('Vac1')
    print(vacuum)
    vacuum.operate()
    warrobot = WarRobot('R2D1', 'Pushka')
    warrobot.operate()

if (__name__ == '__main__'):
    main()