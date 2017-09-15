from seed import World
from eventProvider import closestEvents, printEvent
import sys

# Determine if using Verbose mode.
argv = str(sys.argv)
if ('-v' in argv):
    verboseMode = True
else:
    verboseMode = False

if ('-m' in argv):
    showMap = True
else:
    showMap = False


# Get our events.
numClosest = 5
world      = World(verboseMode, showMap)
events     = world.events

# Print instructions.
print("Enter coordinates in form: x,y\nEnter: m to view the map again.\n")
print("---------------------------------\n")

# Always run the CLI.
while True:

    # Capture the input.
    userCoords = raw_input("\n\nPlease Input Coordinates:\n\n> ")
    if (userCoords == 'm'):
        world.printASCII()
    elif (userCoords == 'Event'):
        userEvent = raw_input("Enter Event number:\n    > ")
        try:
            eventNum = int(userEvent)
        except:
            print('Invalid Event number')
        printEvent(eventNum, events)
    else:
        tokens = userCoords.split(',')

        # Check correct format of coordinates provided.
        if (len(tokens) < 2 or len(tokens) > 3):
            print("Enter coordinates in form: x,y\n")
            print("------------------------------")
        else:
            try:
                # Try to parse the input.
                x_coord = int(tokens[0])
                y_coord = int(tokens[1])
            except:
                print("Input coordinates in form: x,y")

            # Start working with our parsed input.
            coord   = (x_coord, y_coord)
            print("\nClosest Events to " + str(coord) + ":")

            # Find Events closest to this coordinate.
            closeEvents = closestEvents(numClosest, events, coord)

            for eventPair in closeEvents:
                distance, event = eventPair
                print(event.toString() + ", Distance " + str(distance))