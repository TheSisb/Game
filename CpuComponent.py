names = [
    'Shitty',
    'Less',
    'Meh',
    'Good',
    'Great'
]
speeds = [
    4.77,
    100,
    1000,
    3000,
    5500
]


class CpuComponent:
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

