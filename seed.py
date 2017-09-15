from random import randint
from random import uniform
from Event import Event
from Ticket import Ticket

class World:

    def __init__(self, verbose):
        self.events, self.coords  = self.genWorld(verbose)

    # Prints an ASCII version of the World.
    def printASCII(self):

        print('Printing ASCII of World\n')
        # Set up each line to print with the y axis numbers.
        lines = ["" for x in range(21)]
        linenum = 10
        for line in range(21):
            if (linenum < 10 and linenum >= 0):
                lines[line] += '   ' + str(linenum) + '  '
            elif (linenum == -10):
                lines[line] += '  ' + str(linenum) + ' '
            else:
                lines[line] += '  ' + str(linenum) + '  '
            linenum = (linenum - 1)

        # Loop through the coordinate system filling positions with x's or spaces.
        for x in range(-10,11):
            for y in [10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]:
                coord = (x, y)
                line = 10 - y
                if (coord in self.coords):
                    if (y == 0):
                        lines[line] += '-x--'
                    else:
                        lines[line] += ' x  '
                else:
                    if (y == 0):
                        lines[line] += '----'
                    elif (x == 0):
                        lines[line] += ' |  '
                    else:
                        lines[line] += '    '
                
        print('      -10 -9  -8  -7  -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6   7   8   9   10 \n')
        for line in lines:
            print line
        print('\n\n')

    # Function that generates a world model of Events; returns a list of Events.
    def genWorld(self, verbose):

        # List of Events and list of coordinates that are in use.
        events = []
        coords = []

        # Number of Events to generate.
        numEvents = randint(10, 80)
        if (verbose):
            print('Generating ' + str(numEvents) + ' Events.')

        # Loop for as many Events as we are generating.
        for eventID in range(0, numEvents):
            # Keep running until we get a coordinate that is not in use.
            while True:
                # Generate a coordinate for this event.
                coord = self.genCoord()
                # Check that this coordinate is not in use.
                if coord not in coords:
                    # Create a new Event.
                    if (verbose):
                        print('\nGenerated Event ' + str(eventID) + ' @ ' + str(coord) + ' with:')
                    event = Event(eventID, coord, self.genTickets(eventID, verbose))
                    # Append this used coordinate, and this new Event to their appropriate lists.
                    coords.append(coord)
                    events.append(event)
                    break
        return events, coords

    # Generates a 2D coordinate in a plane ranging from -10 to 10 in both x and y axis.
    def genCoord(self):
        return (randint(-10, 10), randint(-10, 10))

    # Generates a list of Tickets based on 3 categories: [VIP, Premium, General]
    def genTickets(self, eventID, verbose):

        output = []

        # Generate number of each Ticket category.
        numVIPTickets       = randint(0, 100)                   # There can be between 0 and 100 VIP Tickets.
        numPremiumTickets   = randint(0, 10000)                 # There can be between 0 and 10,000 Premium Tickets.
        numGeneralTickets   = randint(0, 100000)                # There can be between 0 and 100,000 General Tickets.

        # Generate price of each Ticket category.
        vipTicketPrice      = round(uniform(1000, 50000), 2)    # A VIP Ticket is priced between $1,000 and $50,000.
        premiumTicketPrice  = round(uniform(200, 800), 2)       # A Premium Ticket is priced between $200 and $800.
        generalTicketPrice  = round(uniform(10, 200), 2)        # A General Ticket is priced between $10 and $200.

        # Generate VIP Tickets.
        for i in range(0, numVIPTickets):
            ticket = Ticket(i, eventID, 'VIP', vipTicketPrice)
            output.append(ticket)

        # Generate Premium Tickets.
        for i in range(0, numPremiumTickets):
            ticket = Ticket(i, eventID, 'Premium', premiumTicketPrice)
            output.append(ticket)

        # Generate General Tickets.
        for i in range(0, numGeneralTickets):
            ticket = Ticket(i, eventID, 'General', generalTicketPrice)
            output.append(ticket)

        if (verbose):
            print(str(numVIPTickets) + ' VIP tickets @ $' + str(vipTicketPrice) + ' a ticket.')
            print(str(numPremiumTickets) + ' Premium tickets @ $' + str(premiumTicketPrice) + ' a ticket.')
            print(str(numGeneralTickets) + ' General tickets @ $' + str(generalTicketPrice) + ' a ticket.')

        return output