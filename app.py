from seed import genWorld

events = genWorld()

for event in events:
    print(event.toString())

