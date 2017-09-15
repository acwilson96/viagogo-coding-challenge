class Event:

    def __init__(self, id, coord, price, numTickets):
        self.id         = id
        self.coord      = coord
        self.price      = price
        self.numTickets = numTickets

    # Returns the Manhattan distance between the provided coordinate and this event.
    def manhattanDistanceTo(self, coord):
        event_x, event_y = self.coord
        x, y = coord
        return abs(event_x - x) + abs(event_y - y)

    # Returns a string representation of this Event.
    def toString(self):
        x, y = self.coord
        return "Event " + str(self.id) + " - $" + str(self.price) + ", (" + str(x) + ", " + str(y) + ")"