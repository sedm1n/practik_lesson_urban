class Building:
    def __init__(self):
        self.numberOfFloors = 0
        self.buildingType = ''
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


my_building = Building( )

my_building.numberOfFloors = 4
my_building.buildingType = "text"
my_building


print(my_building.numberOfFloors == 6)
print(my_building.buildingType != '77text')



