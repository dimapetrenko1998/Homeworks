class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        if isinstance(other, Building):
            return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType
        return False


