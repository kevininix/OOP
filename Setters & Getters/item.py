import csv

class Item :
    
    pay_rate = 0.8 #pay rate after 20% discount
       
    all = []

    def __init__(self, name: str, price: float, quantity = 0) :
        
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is negative!" #custom error message
        assert quantity >= 0, f"Quantity {quantity} is negative!"

        # Assign to self objects
        # Add a _ to attribute to use with @property
        self._name = name                                        
        self.price = price                                      
        self.quantity = quantity

        #Append to 'all' list every instace created
        Item.all.append(self)  
    
    # Add a decorator to allow for encapsulation
    # property decorator = read-only attribute
    @property
    def name(self):
        return self._name

    # Allow a specific way of changing value of attribute
    @name.setter
    def name(self, value):
        self._name = value

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
    
    # Check if number is an int with a static method
    @staticmethod
    def is_integer(num): # Notice the color, static methods don't take 'self' as first parameter but as a regular entry 
        # .0 decimals should count as int
        if isinstance(num, float):
            return num.is_integer() # e.g 5.0 --> True
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})" 