class Event:

    def __init__(self, id, x, y, price, numTickets):
        self.id         = id
        self.x          = x
        self.y          = y
        self.price      = price
        self.numTickets = numTickets

    def manhattanDistanceTo(self, x, y):
        return abs(self.x - x) + abs(self.y - y)