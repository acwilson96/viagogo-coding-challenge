class Ticket:

    def __init__(self, id, eventID, category, price):
        self.id       = id
        self.eventID  = eventID
        self.category = category
        self.price    = price

        
    def toString(self):
        return self.category + " Ticket: " + str(self.price)