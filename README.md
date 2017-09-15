# viagogo-coding-challenge

## Design Choices

### Event/Ticket Assumptions/Decisions

* Given the coordinate system is essentially a 20x20 grid, this means there are 400 possible 'locations' and event can occur. It would seem sensible that there could be up to 80 possible Events. Having a lower bound of 10 Events seems sensible as it would be unlikely that there are no events happening anywhere in our virutal world.

* Events have 3 classes of tickets: [VIP, Premium, General]:
  * VIP Tickets: Up to 100 available, price ranges between $1000 to $50,000
  * Premium Tickets: Up to 10,000 available, price ranges between $200 to $800.
  * General Tickets: Up to 100,000 available, price ranges between $10 to $200.

## Installation/Usage

### Installation
* Requires python version 2.7.10
* Open the terminal
* Clone the repo using `git clone https://github.com/acwilson96/viagogo-coding-challenge.git`
* Change directory to the repo using `cd viagogo-coding-challenge`


### Usage
* `python app.py` to start the script.
* Arguments:
  * `-v` to have verbose output of world generation.