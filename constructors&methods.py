
#item1 = 'Phone'
#item1_price = 100
#item1_quantity = 5
#item1_price_total = item1_price * item1_quantity

#Even though the labels indicate they're related, python
#reads them as 4 random variables, which are themselves
#instaces of different classes. How to make the relation explicit?

#Run this
#print(type(item1)) #Class: 'str'
#print(type(item1_price)) #Class: 'int'
#print(type(item1_quantity)) #'Class: 'int'
#print(type(item1_price_total)) #'Class: 'int'

#The outcome suggests these data types are actually instances of 
#*classes* called str and ints. Each data type is an object instatiated 
# by a class, i.e an object is an element/instance of a class

#We can tell python to create a custom data type, this will allow for
#code that can be reused in the future. Each instance of this class can
#have attributes that explain related info about it

#Class + [Name of the class]: [code]
from traceback import print_tb

from sortedcollections import ItemSortedDict


class Item :
    pass

#Instance of Class: 'Item'
item1 = Item()
#This is equivalent to
random_str = str('text')

#Assign attributes to instances of classes
#An object is a generic thing while an instance is a single object
#[Object of class].[Attribute Name] = [instance]
item1.name = 'Phone'
item1.price = 100
item1.quantity = 5
#Unlike variables, all these instances have an actual relationship
#via their Class membership

print(type(item1)) #Class: '__main__.Item' <<<------!!!
print(type(item1.name)) #Class: 'Item'
print(type(item1.price)) #Class: 'Item'
print(type(item1.quantity)) #Class: 'Item'
#name, price and quantity don't change bc we assigned str and int
#type atributes to the Item object.
#But note item1, it has a data type of 'Item' now

#We can also create methods (i.e a function inside a class) 
#and execute them. Take for example the .upper() method 
#executed on a str instance
random_str = 'aaa'
print(random_str.upper()) #[OUT]: 'AAA'

#To make methods we write them inside our Class 
#Self represents the instance of the class, is the instance the method is called on
#The __init__ constructor is always called when an object is created,  it allows the 
#class to initialize the attributes of the class
class Item :
    def __init__(self) :
        print("I'm alive father")
    def total_price(self, x, y):
         return x * y
#Define the instances again to avoid '[Class] has not atribute [method]' error
item1 = Item() #[OUT]: I'm alive father
item1.name = 'Phone'
item1.price = 100
item1.quantity = 5

print(item1.total_price(item1.price, item1.quantity)) #[OUT]: 500

#Let's create more instances of Item
item2 = Item() #[OUT]: I'm alive father
item2.name = 'Laptop'
item2.price = 1000
item2.quantity = 3

print(item2.total_price(item2.price, item2.quantity)) #[OUT]: 000

#We can exploit the contructor to avoid writing [Instace].[Attribute] = [Object] each time
#by taking in more parameters
class Item :
    def __init__(self, name, price, quantity) :
        print(f"An instance created: {name}") 
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_price(self, x, y):
         return x * y

item1 = Item('Phone', 100, 5) #[OUT]: An instance created: Phone
item2 = Item('Laptop', 1000, 3) #[OUT]: An instance created: Laptop

print(item1.name) #[OUT]: Phone
print(item1.price) #[OUT]:100
print(item1.quantity) #[OUT]: 5 
print(item2.name ) #[OUT]: Laptop
print(item2.price) #[OUT]: 1000
print(item2.quantity) #[OUT]: 3

#If you don't have a value for a given atribute you can give it 
#default value, that way you don't need to pass it
class Item :
    def __init__(self, name, price, quantity = 0) :
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_price(self, x, y):
         return x * y

item1 = Item('Phone', 100) 
item2 = Item('Laptop', 1000) 
print(item1.quantity) #[OUT]: 0

#You can also assign attributes (not included in the constructor) 
# to specific instances individually
item2.has_numpad = False

#Now we can replace x and y with attributes, they don't need to
#go into the def bc we have access to those attributes throughout
#the methods 
class Item :
    def __init__(self, name, price, quantity = 0) :
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_price(self):
         return self.price * self.quantity

item1 = Item('Phone', 100, 5) 
item2 = Item('Laptop', 1000, 3) 

print(item1.total_price()) #[OUT]: 500

#We have to validate the data types that are being passed
#to avoid situations like [OUT]: 500500500500500 instead of
# an error if we had tem('Phone', '500', 5)
#instead of Item('Phone', 100, 5) 
class Item :
    def __init__(self, name: str, price: float, quantity = 0) : #quantity doesn't need it bc
        self.name = name                                        #the default value determines
        self.price = price                                      #the type
        self.quantity = quantity
    def total_price(self):
         return self.price * self.quantity

#We can further specify what subgroup of the datatype we 
#can allow, e.g only positive numbers for price and quant
class Item :
    def __init__(self, name: str, price: float, quantity = 0) :
        
        #Run validations to the received arguments
        assert price >= 0, f"Price {price} is negative!" #custom error message
        assert quantity >= 0, f"Quantity {quantity} is negative!"

        #Assign to self objects
        self.name = name                                        
        self.price = price                                      
        self.quantity = quantity
        
    def total_price(self):
         return self.price * self.quantity

#Global/Class attributes, i.e an attribute shared by all instances of a class
class Item :
    
    pay_rate = 0.8 #pay rate after 20% discount
    
    def __init__(self, name: str, price: float, quantity = 0) :
        
        #Run validations to the received arguments
        assert price >= 0, f"Price {price} is negative!" #custom error message
        assert quantity >= 0, f"Quantity {quantity} is negative!"

        #Assign to self objects
        self.name = name                                        
        self.price = price                                      
        self.quantity = quantity
        
    def total_price(self):
         return self.price * self.quantity

item1 = Item('Phone', 100, 5) 
item2 = Item('Laptop', 1000, 3) 

print(Item.pay_rate) #[OUT]: 0.8
#We can also acess it from within an instance
print(item1.pay_rate) #[OUT]: 0.8
print(item2.pay_rate) #[OUT]: 0.8

#Look up attributes belonging to the class and the instances
print(Item.__dict__) #[OUT]: {..., 'pay_rate': 0.8, .....}  All attributes for class level
print(item1.__dict__) #[OUT]: {'name': 'Phone', 'price': 100, 'quantity': 5}, all attributes for instance level

#Method for applying discount
class Item :
    
    pay_rate = 0.8 #pay rate after 20% discount
    
    def __init__(self, name: str, price: float, quantity = 0) :
        
        #Run validations to the received arguments
        assert price >= 0, f"Price {price} is negative!" #custom error message
        assert quantity >= 0, f"Quantity {quantity} is negative!"

        #Assign to self objects
        self.name = name                                        
        self.price = price                                      
        self.quantity = quantity
        
    def total_price(self):
         return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * Item.pay_rate

item1 = Item('Phone', 100, 5) 
item2 = Item('Laptop', 1000, 3) 

print(item1.price) #[OUT]: 100
item1.apply_discount() 
print(item1.price) #[OUT]: 80.0

#Assign a different discount rate without editing pay_rate
item2.pay_rate = 0.7 #Overwrites variable at instance level but not at class level
item2.apply_discount()
#It still applies the 0.8 pay_rate bc the def has Item.pay_rate so it calls  
#the value at the class level, we need to change it to self.pay_rate so it's
#level sensitive
print(item2.price) #[OUT]: 800.0



class Item :
    
    pay_rate = 0.8 #pay rate after 20% discount
    
    def __init__(self, name: str, price: float, quantity = 0) :
        
        #Run validations to the received arguments
        assert price >= 0, f"Price {price} is negative!" #custom error message
        assert quantity >= 0, f"Quantity {quantity} is negative!"

        #Assign to self objects
        self.name = name                                        
        self.price = price                                      
        self.quantity = quantity
        
    def total_price(self):
         return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item('Phone', 100, 5) 
item2 = Item('Laptop', 1000, 3) 

item2.pay_rate = 0.7 
item2.apply_discount()
print(item2.price) #[OUT]: 700.0

#Add code to return a list of instances
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
    
    #Makes it so print(Item.all) returns the instaces' names instead of the 
    #self.__module__, type(self).__name__, hex(id(self))) format
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})" #Recommended way of return it 

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

for instance in Item.all: #[OUT]: Phone // Laptop // Cable // Mouse // Keyboard
    print(instance.name) 

print(Item.all) #[OUT]: [Item('Phone', 100, 1), Item('Laptop', 1000, 3), etc...]

#Using a csv file to store the instances
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
    
    # Since we're not calling an instance but instantiating the objects themselves
    # from a file, so we need to convert this method into a class method 
    @classmethod  #A decorator changes the behavior of a function without overwriting it
    def instantiate_from_csv(cls): #The class object Item itself is passed as a first argument
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')), #to avoid errord specify it's a float
                quantity = int(item.get('quantity'))
            )

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})" 

Item.instantiate_from_csv()
print(Item.all) #[OUT]: [Item('Phone', 100, 1), Item('Laptop', 1000, 3), etc...]

#Static methods
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
        return f"Item('{self.name}', {self.price}, {self.quantity})" 

print(Item.is_integer(7.5))