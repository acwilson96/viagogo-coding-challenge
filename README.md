# viagogo-coding-challenge

## Design Choices

### Number of Events to Generate.

* Given the coordinate system is essentially a 20x20 grid, this means there are 400 possible 'locations' and event can occur. It would seem sensible that there could be up to 80 possible Events. Having a lower bound of 10 Events seems sensible as it would be unlikely that there are no events happening anywhere in our virutal world.

### Event Properties

* I decided a ticket could range in price from $10 to $400. This could include tickets to small events like bar entry at $10 to top football matches at $400.

* I decided that the number of tickets an Event could host would be within [50, 100000] I chose 50 as a lower bound in the example of an exclusive VIP event. I chose 100,000 as the upper bound as Old Trafford Stadium has a capacity of roughly 75,000 people, so a stadium in the US could easilly be larger.