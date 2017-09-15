# viagogo-coding-challenge

## Design Choices

### Assumptions/Decisions

* Given the coordinate system is essentially a 20x20 grid, this means there are 400 possible 'locations' and event can occur. It would seem sensible that there could be up to 80 possible Events. Having a lower bound of 10 Events seems sensible as it would be unlikely that there are no events happening anywhere in our virutal world.

* Events have 3 categories of tickets: [VIP, Premium, General]:
  * I felt that assigning classes to tickets like this meant that tickets of any category can be created in the future. It might have been wise to create a parent class of type Ticket, and then have Sub-Classes for these specific Ticket types. But as I saw no advantage to using this for the purposes of this exercise, I opted to keep the ticket type as a string attribute.
  * VIP Tickets: Up to 100 available, price ranges between $1000 to $50,000
  * Premium Tickets: Up to 10,000 available, price ranges between $200 to $800.
  * General Tickets: Up to 100,000 available, price ranges between $10 to $200.

* It is possible to query for events outside of the World; i.e. -100, -100 or 25,25. It would be easy to prevent/validate this, but letting our extra-terrestrial friends outside of earth know about events is always friendly :)

## Installation/Usage

### Installation
* Tested using Python 2.7.10 on macOS Sierra, and Python 2.7.11 on Ubuntu 16.04
* Open the terminal
* Clone the repo using `git clone https://github.com/acwilson96/viagogo-coding-challenge.git`
* Change directory to the repo using `cd viagogo-coding-challenge`


### Usage
* `python app.py` to start the script.
* Arguments:
  * `-v` to have verbose output of world generation.
  * `-m` to have the World coordinates printed on creation. (Shows minimal data about existence of Events)
* Enter `m` at any point to see the map.

## Future Thoughts

### Multiple Events at same Location
* This could potentially cause complications if more than 5 Events exist at once location, meaning that the closest 5 Events would be debatebly incorrect.
* In terms of what I would change with my program:
  * Seeding: I would only have to alter the seeding algorithm to stop checks for existing Events at a given location.
  * Searching: As mentioned prior, we could have the situation where more than 5 Events could exist in one location. We could either display all those Events at that single location, and inform the user that more exist there. Or perhaps show only one Event per location (but inform user that more Events exist at that location). We could also choose to display more than 5 Events, if more than 5 exist in one single location, since it could be hard to determine which of the 5+ Events are 'closest'.

### Larger Data set and Scalability
* My program is limited in that the runtime of the search algorithm is `O(NlogK)` where N is the number of Events, and K is the number of closest Events to find. This is obviously not ideal, and so perhaps implementing a regional system where a large dataset of Events are clustered into smaller sets of 'regions', such as United Kingdom, or Netherlands, or perhaps even smaller in places like London (where there are bound to be more Events that the Scottish borders). Then when a user queries a coordinate in those region's, the program only queries the Events in that region, to avoid comparisons with the entire worlds set of Events.