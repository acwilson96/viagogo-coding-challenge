# Finds the k closest events to coords
def closestEvents(k, eventsList, coords):

    # Populate list of (distance, Event) pairs.
    eventDistance = []
    for event in eventsList:
        # Get the distance from coords to the current Event.
        distance = event.manhattanDistanceTo(coords)
        eventDistance.append((distance, event))
    
    for eventPair in eventDistance:
            distance, event = eventPair
            print(event.toString() + ", Distance " + str(distance))

    # Sort the list based on distance.
    eventDistance = sorted(eventDistance, key=lambda x: x[0])

    print()
    for eventPair in eventDistance:
            distance, event = eventPair
            print(event.toString() + ", Distance " + str(distance))

    print()
    # Extract the first k elements.
    output = eventDistance[:k]

    return output