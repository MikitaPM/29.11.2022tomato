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








