class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.color} {self.name} поехала!'

    def stop(self):
        return f'{self.color} {self.name} остановилась!'

    def turn(self, direction):
        self.direction = direction
        return f'{self.color} {self.name} повернула {self.direction}'

    def show_speed(self):
        return f'{self.color} {self.name} едет со скоростью {self.speed}'


class PoliceCar(Car):
    def check_police(self):
        if self.is_police is True:
            return f'{self.color} {self.name} полицейская машина'
        else:
            return f'{self.color} {self.name} машина не полицейская'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'{self.color} {self.name} едет со скоростью {self.speed}\n' \
                   f'Разрешенная максимальная скорость: 60. Сбросьте скорость!'
        return f'{self.color} {self.name} едет со скоростью {self.speed}'


class SportCar(Car):
    def show_speed(self):
        if self.speed < 80 and self.speed > 60:
            return f'{self.color} {self.name} едет со скоростью {self.speed}\n' \
                   f'Вы едете на спорткаре по шоссе.'
        return f'{self.color} {self.name} едет со скоростью {self.speed}'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'{self.color} {self.name} едет со скоростью {self.speed}\n' \
                   f'Разрешенная максимальная скорость: 40. Сбросьте скорость!'
        return f'{self.color} {self.name} едет со скоростью {self.speed}'


car_one = Car(70, 'Blue', 'BMW', True)
car_two = Car(50, 'Red', 'Ford', False)

print(car_one.go())
print(car_two.go())
print(car_one.turn('Направо'))
print(car_two.turn('Направо'))
print(car_one.turn('Налево'))
print(car_two.turn('Налево'))
print(car_one.show_speed())
print(car_two.show_speed())
print(PoliceCar.check_police(car_one))
print(PoliceCar.check_police(car_two))
print(SportCar.show_speed(car_one))
print(TownCar.show_speed(car_two))
print(car_one.stop())
print(car_two.stop())
