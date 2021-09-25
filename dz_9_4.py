class Car:
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, 'поехала')

    def stop(self):
        print(self.name, 'остановилась')

    def turn(self):
        print(self.name, 'повернула')

    def show_speed(self):
        print('Текущая скорость', self.name, self.speed, 'км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(self.name, 'превысила скорость более 6о км/ч')
        else:
            print('Текущая скорость', self.name, self.speed, 'км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(self.name, 'превысила скорость более 4о км/ч')
        else:
            print('Текущая скорость', self.name, self.speed, 'км/ч')


class PoliceCar(Car):
    pass


t = TownCar(70, 'red', 'RENO', False)
w = WorkCar(50, 'white', 'BMW', False)
s = SportCar(100, 'black', 'LADA', False)
p = PoliceCar(200, 'blu', 'HYUNDAI', True)
t.go()
w.stop()
s.turn()
t.show_speed()
w.show_speed()
s.show_speed()
p.show_speed()
