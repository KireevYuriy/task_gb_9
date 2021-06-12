class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {}
        self.income['wage'] = wage
        self.income['bonus'] = bonus


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_fullname(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self.income['wage'] + self.income['bonus']


a = Position("Ivan", "Ivanov", "Seller", 35000, 6000)
b = Position("Petr", "Petrov", "Driver", 35000, 5000)

print(a.get_fullname())
print(a.get_total_income())
print(b.get_fullname())
print(b.get_total_income())
