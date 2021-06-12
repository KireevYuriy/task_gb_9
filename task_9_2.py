class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def mass_asphalt(self, mass, thickness):
        print(self.length * self.width * mass * thickness)


r = Road(20, 5000)
r.mass_asphalt(25, 5)
