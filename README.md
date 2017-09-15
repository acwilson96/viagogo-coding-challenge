# viagogo-coding-challenge

## Design Choices

### Number of Events to Generate.

* Given the coordinate system is essentially a 20x20 grid, this means there are 400 possible 'locations' and event can occur. It would seem sensible that there could be up to 80 possible Events. Having a lower bound of 10 Events seems sensible as it would be unlikely that there are no events happening anywhere in our virutal world.