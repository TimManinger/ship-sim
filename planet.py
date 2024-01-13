from name_generator import randName
from ship import Ship


class Planet():
    def __init__(self,
                 ports: int,
                 ships: int,
                 production: dict,
                 consumption: dict,
                 ):
        self.name = randName('planet')
        self.ports = ports
        self.ships = [Ship() for i in range(ships)]
        self.orbit = self.ships
        self.production = production
        self.consumption = consumption
        self.inventory = {}
        self.rqs = {}
        self.log = [f"PLANET: {self.name} initialized"]

    def __str__(self):
        return self.name

    def update(self) -> str:
        """
        Simulate production, consumption, and ships for one time tick
        """
        self.log.append(f"UPDATE: {self.name}")
        for p in self.production.keys():
            self.inventory[p] += self.production[p]
            self.log.append(f"{p} = {self.inventory[p]}")
            if self.inventory[p] > self.consumption[p] * 256:
                for s in self.orbit:
                    if s.cargo == []:
                        self.inventory[p] = s.load(p, self.inventory[p])
                        self.log.append(f"loading {p} into {s}")
        for c in self.consumption.keys():
            self.inventory[c] -= self.consumption[c]
            if self.inventory[c] <= self.consumption[c]:
                self.rqs[c] = self.consumption[c] * 256
        for s in self.ships:
            print(s.update())
