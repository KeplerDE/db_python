import random
import string



class User:
    """Represents a user that can buy a cinema Seat"""

    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        pass

class Seat:
    """Represents a cinema seat that can be taken from a User"""

    database = "cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        """Get the price of a certain seat"""
        pass

    def is_free(self):
        pass

    def occupy(self):
        """Change value of taken in the database from 0 to 1 if Seat is free"""
        pass
class Card:
    """ Represents a bank card needed to finalize a Seat purchase"""

    database = "banking.db"

    def __init__(self, type, number, cvc, holder):
        self.holder = holder
        self.cvc = cvc
        self.number = number
        self.type = type

    def validate(self, price):
        pass

class Ticket:
    """Represents a cinema Ticket purchased by a User"""

    def __init__(self, user, price, seat_number):
        self.user = user
        self.price = price
        self.id = "".join([random.choice(string.ascii_letters) for i in range(8)])
        self.seat_number = seat_number

    def to_pdf(self):
        pass

if __name__ == "__main__":

    name = input("Your full name: ")
