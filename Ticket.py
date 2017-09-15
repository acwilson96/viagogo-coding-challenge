class Ticket:

    def __init__(self, id, eventID, category, price):
        self.id       = id
        self.eventID  = eventID
        self.category = category
        self.price    = price

    # Makes sure that the price has trailing 0's if necessary.
    def formatPrice(self, price):
        output = format(price, ',.2f')
        return str(output)

    def toString(self):
        return self.category + " Ticket: $" + str(self.formatPrice(self.price))