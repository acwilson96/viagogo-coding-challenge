import operator

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

    # Returns the cheapest ticket available.
    def getCheapestTicket(self):
        sortedTickets = sorted(self.tickets, key=operator.attrgetter('price'))
        return sortedTickets[0]

    # Returns a string representation of this Event.
    def toString(self):
        x, y = self.coord
        return "Event " + self.formatID(self.id) + " - " + self.getCheapestTicket().toString()
