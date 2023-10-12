from name_generator import randName
from planet import Planet
import httpx
import time


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


if __name__ == "__main__":
    t = 0.0
    dt = 1000/60
    paused = False
    currentTime = time.time()
    accumulator = 0
    while not paused:
        newTime = time.time()
        frameTime = newTime - currentTime
        currentTime = newTime

        accumulator += frameTime

        while accumulator >= dt:
            worldUpdate()
            accumulator -= dt
            t += dt

        render()
