from random import randint
from random import uniform
from Event import Event

class World:

    def __init__(self):
        self.events = self.genWorld()
    
    # Function that generates a world model of Events; returns a list of Events.
    def genWorld(self):

        # List of Events and list of coordinates that are in use.
        events = []
        coords = []

        # Number of Events to generate.
        numEvents = randint(10, 80)

        # Loop for as many Events as we are generating.
        for i in range(0, numEvents):
            # Keep running until we get a coordinate that is not in use.
            while True:
                # Generate a coordinate for this event.
                coord = self.genCoord()
                # Check that this coordinate is not in use.
                if coord not in coords:
                    # Create a new Event.
                    event = Event(i, coord, self.genPrice(), self.genTicketNum())
                    # Append this used coordinate, and this new Event to their appropriate lists.
                    coords.append(coord)
                    events.append(event)
                    break
        return events

    # Generates a 2D coordinate in a plane ranging from -10 to 10 in both x and y axis.
    def genCoord(self):
        return (randint(-10, 10), randint(-10, 10))

    # Generates a non-zero float with two decimal places.
    def genPrice(self):
        return round(uniform(10, 400), 2)

    # Generates a non-zero integer.
    def genTicketNum(self):
        return randint(10, 100000)