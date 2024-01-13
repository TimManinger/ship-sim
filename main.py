from planet import Planet
from ship import Ship
from sim import Sim
import time

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
