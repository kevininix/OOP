import csv

class Item :
    
    pay_rate = 0.8 #pay rate after 20% discount
       
    all = []

    def __init__(self, name: str, price: float, quantity = 0) :
        
        #Run validations to the received arguments
        assert price >= 0, f"Price {price} is negative!" #custom error message
        assert quantity >= 0, f"Quantity {quantity} is negative!"

        #Assign to self objects
        self.name = name                                        
        self.price = price                                      
        self.quantity = quantity

        #Append to 'all' list every instace created
        Item.all.append(self)  
        
    def total_price(self):
         return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    # Call from csv with a class method
    @classmethod  
    def instantiate_from_csv(cls): 
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')), #specify it's a float to avoid error
                quantity = int(item.get('quantity'))
            )
    
    #Check if number is an int with a static method
    @staticmethod
    def is_integer(num): #Notice the color, static methods don't take 'self' as first parameter but as a regular entry 
        #.0 decimals should count as int
        if isinstance(num, float):
            return num.is_integer() # e.g 5.0 --> True
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})" 

phone1 = Item('JscPhonev10', 500, 5)
phone2 = Item('JscPhonev20', 700, 5)

# What attributes could represent irl phones? e.g a phone being broken
phone1.broken_phones = 1
phone2.broken_phones = 1
# These are unsellable, so we need a method that substracts them 
# from the quantity attribute
# We can't add it to the class since broken_phones is an attribute 
# only meaninful for phones not for items in general

# We'll create a separate class that inherits the functionalities
# from the Item Class
class Phone(Item):

    all = []
    # Add extra attribute to constructor
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0) :
        
        #Run validations to the received arguments
        assert price >= 0, f"Price {price} is negative!" #custom error message
        assert quantity >= 0, f"Quantity {quantity} is negative!"
        assert broken_phones >= 0, f"Number of broken phones {broken_phones} is negative!"

        #Assign to self objects
        self.name = name                                        
        self.price = price                                      
        self.quantity = quantity
        self.broken_phones = broken_phones
    
        # Actions to execute
        Phone.all.append(self)

phone1 = Phone('JscPhonev10', 500, 5, 1)
phone2 = Phone('JscPhonev20', 700, 5, 1)

# Methods from the parent class should still work
print(phone1.total_price()) # [OUT]: 2500

# We can use the Super function to avoid having to rewrite all the parent's attributes/methods
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
    

phone1 = Phone('JscPhonev10', 500, 5, 1)
phone2 = Phone('JscPhonev20', 700, 5, 1)
print(phone1.total_price()) # [OUT]: 2500 

# print(Item.all) --> [OUT]: [Item('JscPhonev10', 500, 5), Item('JscPhonev20', 700, 5)]
# print(Phone.all) --> [OUT]: [Item('JscPhonev10', 500, 5), Item('JscPhonev20', 700, 5)]

# Instead of Item in the __repr__ method we should write self.__class__.__name__
# to avoid the result from above
print(Item.all) # [OUT]: [Item('JscPhonev10', 500, 5), Item('JscPhonev20', 700, 5)]
print(Phone.all) # [OUT]: [Phone('JscPhonev10', 500, 5), Phone('JscPhonev20', 700, 5)]

