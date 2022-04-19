from item import Item

class Phone(Item):

    # Add extra attribute to constructor
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0) :
        
        super().__init__( # We can also acces 'all = []' from the parent Class

            name, price, quantity
        )

        #Run validations to the received arguments
        assert broken_phones >= 0, f"Number of broken phones {broken_phones} is negative!"

        #Assign to self objects
        self.broken_phones = broken_phones