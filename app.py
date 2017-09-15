from seed import World
from eventProvider import closestEvents


# Get our events.
numClosest = 5
world      = World()
events     = world.events

# Print instructions.
print("\n\nEnter coordinates in form: x,y\n")
print("---------------------------------")

# Always run the CLI.
while True:

    # Capture the input.
    userCoords = raw_input("\n\n\n\nPlease Input Coordinates:\n\n> ")
    tokens = userCoords.split(',')

    # Check correct format of coordinates provided.
    if (len(tokens) < 2 or len(tokens) > 3):
        print("\nEnter coordinates in form: x,y\n")
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

