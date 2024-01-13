from name_generator import randName
from planet import Planet
import httpx


class Sim():
    def __init__(self,
                 size: str = 7,):
        self.planets = []
        self.log = []
        for i in range(size):
            self.planets.append(Planet(randName('planet')))

    def worldUpdate(self):
        self.log = [p.update() for p in self.planets]

    def render():
        """rendering in this case is our HTTP POST to the api"""
        pass
