class Event:

    def __init__(self, id, coord, tickets):
        self.id         = id
        self.coord      = coord
        self.tickets    = tickets

    # Returns the Manhattan distance between the provided coordinate and this event.
    def manhattanDistanceTo(self, coord):
        event_x, event_y = self.coord
        x, y = coord
        return abs(event_x - x) + abs(event_y - y)

    # Adds preceding zeros to the ID.
    def formatID(self, id):
        zeros = ""
        for i in range(0, 3 - len(str(id))):
            zeros += "0"
        return zeros + str(id)

    # Makes sure that the price has trailing 0's if necessary.
    def formatPrice(self, price):
        output = format(price, ',.2f')
        return str(output)


    # Returns a string representation of this Event.
    def toString(self):
        x, y = self.coord
        return "Event " + self.formatID(self.id) + " - $" + self.formatPrice(self.price)
