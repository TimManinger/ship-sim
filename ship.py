from name_generator import randName
from planet import Planet


LOAD_SPEED = 10


class Ship():
    def __init__(self,
                 name: str,
                 capacity: int,
                 speed: int,
                 ):
        self.name = randName('ship')
        self.capacity = capacity
        self.speed = speed
        self.cargo = {}
        self.port = None
        self.dest = None
        self.dist = 0
        self.log = []

    def __str__(self):
        return self.name

    def update(self) -> str:
        self.log = [f"SHIP: {self.name}"]

    def move(self, dest: Planet) -> None:
        """
        Reduces distance to current dest by speed
        sets dest to None or Home when ship arrives
        """
        if self.dest is None:
            self.dest = dest
            self.log.append(f"set dest to {dest}")
        self.dist -= self.speed if (self.dist > 0) else 0
        self.log.append(f"moved {self.speed} toward {self.dest} now {self.dist} away")
        if self.dist <= 0:
            self.log.append(f"arrived at {self.dest}")
            self.dest = None

    def load(self, product: str, amt: int) -> int:
        """
        takes a product name and an amount available and adds them to cargo
        returns the amount remaining after loading for one timestep
        """
        try:
            self.cargo[product] += LOAD_SPEED
        except KeyError:
            self.cargo[product] = LOAD_SPEED
            self.log.append(f"added {product} to cargo manifest")
        self.log.append(f"{self.cargo[product]} {product}now in cargo")
        return amt - LOAD_SPEED

    def unload(self, product: str, port: Planet) -> None:
        """
        Takes a product name and a destination Planet and shifts that product
        from cargo into the Planet's inventory
        """
        try:
            self.cargo[product] -= LOAD_SPEED
            try:
                port.inventory[product] += LOAD_SPEED
            except KeyError:
                port.inventory[product] = LOAD_SPEED
                self.log.append(f"added {product} to {port} inventory")
            self.log.append(f"{self.cargo[product]} {product} now in cargo")
            self.log.append(f"{port.inventory[product]} {product} now on {port}")
        except KeyError:
            raise Exception(f"ERROR {self.name} has no {product} on {port}")
        if self.cargo[product] <= 0:
            self.cargo.pop(product)
            self.log.append(f"removed {product} from cargo manifest")

    def full(self) -> bool:
        """
        Returns true if the sum of the cargo is >= capacity
        """
        return (True if sum(self.cargo.values()) >= self.capacity else False)
