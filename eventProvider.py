import operator

# Finds the k closest events to coords
def closestEvents(k, eventsList, coords):

    # Populate list of (distance, Event) pairs.
    eventDistance = []
    for event in eventsList:
        # Get the distance from coords to the current Event.
        distance = event.manhattanDistanceTo(coords)
        eventDistance.append((distance, event))
    
    # Sort the list based on distance.
    eventDistance = sorted(eventDistance, key=lambda x: x[0])
    
    # Extract the first k elements.
    output = eventDistance[:k]

    return output

def printEvent(eventNum, events):
    sortedEvents = sorted(events, key=operator.attrgetter('id'))
    print(sortedEvents[eventNum].fullInfoString() + '\n\n')
