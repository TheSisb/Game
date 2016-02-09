names = [
    'dial-up',
    'dsl',
    'cable',
    'fios',
    'gigabit'
]
speeds = [
    56,
    3000,
    50000,
    150000,
    1000000
]


class NetworkComponent:
    def __init__(self, level):
        self.level = level
        self.name = names[level]
        self.speed = speeds[level]

    def update_info(self):
        self.name = names[self.level]
        self.speed = speeds[self.level]

    def increase_level(self):
        self.level += 1
        if self.level > 4:
            self.level = 4
        self.update_info()

    def decrease_level(self):
        self.level -= 1
        if self.level < 0:
            self.level = 0
        self.update_info()
