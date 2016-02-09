from Character import Character
from NetworkComponent import NetworkComponent
from CpuComponent import CpuComponent


class Enemy(Character):
    def __init__(self, name='Mob', network=1, cpu=1, money=5):
        super(Enemy, self).__init__(
            name=name,
            network=NetworkComponent(network),
            cpu=CpuComponent(cpu),
            money=money
        )
