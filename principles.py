import csv

import jinja2_time

#1. Encapsulation

# refers to a mechanism of restricting direct access to some
# attributes in a program  

#Write the price discount so that it follows the encapsulation principle
class Item :
    
    pay_rate = 0.8 #pay rate after 20% discount
       
    all = []

    def __init__(self, name: str, price: float, quantity = 0) :
        
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is negative!" #custom error message
        assert quantity >= 0, f"Quantity {quantity} is negative!"

        # Assign to self objects
        self._name = name  
        #left-click change all occurences to _price                                      
        self._price = price                                      
        self.quantity = quantity

        #Append to 'all' list every instace created
        Item.all.append(self) 
    
    @property
    def price(self):
        return self._price 
    
    def apply_discount(self):
        self._price = self._price * self.pay_rate
    
    def apply_increment(self, increment_value):
        self._price = self._price + increment_value
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception('The name is too long')
        else:
            self._name = value

    def total_price(self):
        return self._price * self.quantity
    
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
        return f"{self.__class__.__name__}('{self.name}', {self._price}, {self.quantity})" 

item1 = Item('MyItem', 700, 6)
# Encapsulation recommends changing the value of attributes using methods 
# and not directly
item1.apply_increment(0.2)
print(item1) # [OUT]: 900

# 2. Abstraction

# only show the necessary attributes and hide unnecessary information 

# e.g sending an email involves a lot of new methods, we can make them
# inaccessible outside the Class
class Item :
    
    pay_rate = 0.8 #pay rate after 20% discount
       
    all = []

    def __init__(self, name: str, price: float, quantity = 0) :
        
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is negative!" #custom error message
        assert quantity >= 0, f"Quantity {quantity} is negative!"

        # Assign to self objects
        self._name = name  
        #left-click change all occurences to _price                                      
        self._price = price                                      
        self.quantity = quantity

        #Append to 'all' list every instace created
        Item.all.append(self) 
    
    @property
    def price(self):
        return self._price 
    
    def apply_discount(self):
        self._price = self._price * self.pay_rate
    
    def apply_increment(self, increment_value):
        self._price = self._price + increment_value
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception('The name is too long')
        else:
            self._name = value

    def total_price(self):
        return self._price * self.quantity
    
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
        return f"{self.__class__.__name__}('{self.name}', {self._price}, {self.quantity})" 
 
    # add double underscore to make functions private
    def __connect(self, smtp_server):
        pass
    
    def __prepare_body(self):
        return f'''
        something in the way uuuuhuuuh
        We have {self.quantity} {self.name}
        '''

    def __send(self):
        pass

    def send_email(self):
        self.__connect("")
        self.__prepare_body()
        self.__send()


item1 = Item('MyItem', 700, 6)
item1.send_email()

# 3. Inhertitance

# a mechanism that allows us to reuse code across clases
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

item1 = Phone('jscPhone', 1000, 3)
item1.send_email()
item1.apply_increment(0.2) # [OUT]: 1200


#4. Polymorphism

# refers to the use of a single type entity to represent different types
# in different scenarios

# e.g the built-in len() function
name = 'Jim'
print(len(name)) # [OUT]: 3

some_list = ['some', 'name']
print(len(some_list)) # [OUT]: 2

# e.g the apply_discount method
item1 = Phone('jscPhone', 1000, 3)
item1.apply_discount() # [OUT]: 800

item1 = Item('MyItem', 700, 6)
item1.apply_discount() # [OUT]: 560


