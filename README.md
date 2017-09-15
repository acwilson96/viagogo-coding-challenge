# viagogo-coding-challenge

## Design Choices

### Number of Events to Generate.

* Given the coordinate system is essentially a 20x20 grid, this means there are 400 possible 'locations' and event can occur. It would seem sensible that there could be up to 80 possible Events. Having a lower bound of 10 Events seems sensible as it would be unlikely that there are no events happening anywhere in our virutal world.

### Event Properties

* I decided a ticket could range in price from $10 to $400. This could include tickets to small events like bar entry at $10 to top football matches at $400.

* Events have 3 classes of tickets: [VIP, Premium, General]:
  * VIP Tickets: Up to 100 available, price ranges between $1000 to $50,000
  * Premium Tickets: Up to 10,000 available, price ranges between $200 to $800.
  * General Tickets: Up to 100,000 available, price ranges between $10 to $200.