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
class TomatoBush:
    def __init__(self, count):
        self.tomatoes = [Tomato(index) for index in range(1, count +1)]
    def grow_all(self):
        print('Помидор растет')
        for i_tomato in self.tomatoes:
            i_tomato.grow()
    def all_are_ripe(self):
        for i_tomato in self.tomatoes:
            if not i_tomato.is_ripe():
                print('Помидор не созрел')
            break
        else:
            print('Все помидоры созрели')
class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self.plant = plant

    def gardener_info(self):
        print('Имя садовника: {}\nСколько собрал помидоров: {}\n'.format(self.name, self.plant))

    def tend(worker, my_garden):
        while True:
            if all([i_tomato.is_ripe() for i_tomato in my_garden.tomatoes]):
                question = int(input('Собрать помидор? \n1 - да 2 - нет\n'))
                if question == 1:
                    tomato_count = 0
                    for i_tomato in my_garden.tomatoes:
                        worker.plant += 1
                        tomato_count += 1
                    i_tomato.state = 0

                    print('{} собрал {} помидоров!'.format(worker.name, tomato_count))
                    worker.gardener_info()
                    break

                else:
                    print("Прошло некоторое время\n")

            else:
                question = int(input('Отправить {}а ухаживать за помидорами? \n 1 - да, 2 - нет '.format(worker.name)))
                if question == 1:
                    my_garden.grow_all()
                    my_garden.are_all_ripe()
                else:
                    print("Прошло некоторое время\n")


my_garden = TomatoBush(5)
worker = Gardener('Петрович', 0)
Gardener.tend(worker, my_garden)














