class Event:

    def __init__(self, id, coord, price, numTickets):
        self.id         = id
        self.coord      = coord
        self.price      = price
        self.numTickets = numTickets

    def manhattanDistanceTo(self, coord):
        event_x, event_y = self.coord
        x, y = coord
        return abs(event_x - x) + abs(event_y - y)