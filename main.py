class Tomato:
    states = {1:"Зеленый",
              2: "Бланжевый",
              3: "Красный"}
    def __init__(self, index):

        self.index = index
        self.state = 1
    def grow(self):
        if self.state < 3:
            self.state +=1
    def is_ripe(self):
        if self.state() == 3:
            return True
        return False
class TomatoBush(Tomato):
    def __init__(self, count):
        self.tamatoes = [Tomato(index) for index in range(1, count +1)]
    def grow_all(self):
        print('Помидор растет')
        for i in self.tamatoes:
            i.grow()
    def all_are_ripe(self):
        for i in self.tamatoes:
            if not i.is_ripe():
                print('Помидор не созрел')
            break
        else:
            print('Все помидоры созрели')















