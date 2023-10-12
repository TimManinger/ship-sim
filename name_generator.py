import random
import csv


def randName(type: str = "") -> str:
    with open(f'res/names/{type}names.csv') as names:
        namereader = csv.reader(names, delimiter=',')
        names = [row[0] for row in namereader]
        return random.choice(names)


if __name__ == "__main__":
    for i in range(10):
        print(randName('ship'))
    print('-------')
    for i in range(10):
        print(randName('planet'))
    print('-------')
    for i in range(10):
        print(randName())
