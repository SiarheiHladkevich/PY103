class Tomato:
    states = {
        1: 'First true leaves',
        2: 'Growth',
        3: 'Active vegetative growth',
        4: 'Bloom',
        5: 'Formation of fetus',
        6: 'Fetus maturation'
    }

    def __init__(self, index):
        self._index = index
        self._state = 1

    def grow(self):
        self._state += 1

    def cur_state(self):
        self.current = self._state
        return self.current

    def cur_name(self):
        return self.states.get(self.current)

    def is_ripe(self):
        if self._state == 6:
            # print('The fetus is ripe')
            return True
        else:
            # print(f'The fetus isn\'t yet ripe. Because state is yet {self._state}')
            return False


class TomatoBush:
    def __init__(self, amount):
        self.amount = amount
        self.tomatoes = [Tomato(index=i) for i in range(1, self.amount + 1)]

    def grow_all(self):
        for _ in self.tomatoes:
            _.grow()

    def all_are_rip(self):
        count = 0
        for _ in self.tomatoes:
            if _.is_ripe():
                count += 1
        if count == self.amount:
            return True

    def number_state(self):
        self.number = 0
        while self.number < 1:
            for _ in self.tomatoes:
                self.number = _.cur_state()
        return self.number

    def name_state(self):
        self.name = ''
        if self.name == '':
            for _ in self.tomatoes:
                self.name = _.cur_name()
        return self.name

    def dive_away_all(self):
        if self.all_are_rip():
            self.tomatoes.clear()
        return self.tomatoes


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        self.foo = self._plant.number_state()
        self.bar = self._plant.name_state()
        if self._plant.all_are_rip():
            print('The harvest is ripe')
        else:
            print(f'The harvest isn\'t yet ripe. The process is in the state {self.foo} - "{self.bar}"')

    @staticmethod
    def knowledge_base():
        print('Gardening is the practice of growing and cultivating plants as '
              'part of horticulture. In gardens, ornamental plants are often '
              'grown for their flowers, foliage, or overall appearance; useful '
              'plants, such as root vegetables, leaf vegetables, fruits, and '
              'herbs, are grown for consumption, for use as dyes, or for '
              'medicinal or cosmetic use.')


Gardener.knowledge_base()
bush = TomatoBush(3)
jim = Gardener('Jim', bush)
jim.work()
jim.work()
jim.harvest()
jim.work()
jim.work()
jim.work()
jim.harvest()
