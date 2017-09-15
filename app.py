from seed import genWorld

# Get our events.
events = genWorld()

# Print instructions.
print("\n\nEnter coordinates in form: x,y\n")
print("---------------------------------")

# Always run the CLI.
while True:
    # Capture the input.
    userCoords = raw_input("\n\nPlease Input Coordinates:\n\n> ")
    tokens = userCoords.split(',')

    # Check correct format of coordinates provided.
    if (len(tokens) < 2 or len(tokens) > 3):
        print("\Enter coordinates in form: x,y\n")
        print("------------------------------")
    else:
        try:
            x_coord = int(tokens[0])
            y_coord = int(tokens[1])
            print("\nClosest Events to (" + str(x_coord) + ", " + str(y_coord) + "):")
        except:
            print("Input coordinates in form: x,y")
