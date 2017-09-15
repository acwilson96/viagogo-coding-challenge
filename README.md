# viagogo-coding-challenge

## Design Choices

### Assumptions/Decisions

* Given the coordinate system is essentially a 20x20 grid, this means there are 400 possible 'locations' and event can occur. It would seem sensible that there could be up to 80 possible Events. Having a lower bound of 10 Events seems sensible as it would be unlikely that there are no events happening anywhere in our virutal world.

* Events have 3 classes of tickets: [VIP, Premium, General]:
  * VIP Tickets: Up to 100 available, price ranges between $1000 to $50,000
  * Premium Tickets: Up to 10,000 available, price ranges between $200 to $800.
  * General Tickets: Up to 100,000 available, price ranges between $10 to $200.

* It is possible to query for events outside of the World; i.e. -100, -100 or 25,25. It would be easy to prevent this, but letting martians outside of earth know about events is always friendly :)

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