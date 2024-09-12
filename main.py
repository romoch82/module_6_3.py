class Horse:
    def __init__(self):
        self.x_distance = 0   # пройденный путь
        self.sound = 'Frrr'   # издает звук
        super().__init__()

    def run(self, dx):
        self.x_distance += dx  # изменение дистанции

class Eagle:
    def __init__(self):
        self.y_distance = 0  # высота полета
        self.sound = 'I train, eat, sleep, and repeat'  # издает звук
    def fly(self, dy):
        self.y_distance += dy  # изменение высоты

class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        self.run(dx)  # 8
        self.fly(dy)  # 15

    def get_pos(self):
        return (self.x_distance, self.y_distance)  # возврат на исходную
    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()