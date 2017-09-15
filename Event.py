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

    def fullInfoString(self):

        numVIP      = 0
        numPremium  = 0
        numGeneral  = 0

        for ticket in self.tickets:
            if (ticket.category == 'VIP'):
                vipPrice        = ticket.formatPrice(ticket.price)
                numVIP += 1
            if (ticket.category == 'Premium'):
                premiumPrice    = ticket.formatPrice(ticket.price)
                numPremium += 1
            if (ticket.category == 'General'):
                generalPrice    = ticket.formatPrice(ticket.price)
                numGeneral += 1

        ticketOpts = '  - General Ticket: $' + str(generalPrice) + ' Available: ' + str(numGeneral) + '\n  - Premium Ticket: $' + str(premiumPrice) + ' Available: ' + str(numPremium) + '\n  - VIP Ticket: $' + str(vipPrice) + ' Available: ' + str(numVIP)
        return "\nEvent " + self.formatID(self.id) + " at " + str(self.coord) + ' with ticket options:\n' + ticketOpts