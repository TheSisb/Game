from Character import Character
from NetworkComponent import NetworkComponent
from CpuComponent import CpuComponent


class Player(Character):
    def __init__(self, name='Noob'):
        super(Player, self).__init__(
            name=name,
            network=NetworkComponent(2),
            cpu=CpuComponent(1),
            money=0
        )
