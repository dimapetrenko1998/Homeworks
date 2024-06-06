class Building:
    total = 0

    def __init__(self):
        Building.total += 1


for _ in range(40):
    building = Building()
    print(building)
