from item import Item
from phone import Phone

Item.instantiate_from_csv()
print(Item.all) # OUT[]: [Item('Phone', 100.0, 1), Item('Laptop', 1000.0, 3), etc..]

# Override a value
item1 = Item('MyItem', 500)
# item1.name = 'OtherItem'
# print(item1.name) # ---> OUT[]: OtherItem

# What if we want to restrict this so that we can't chage values 
# after the initial instantiation? e.g item1 = ('MyItem', 500). This 
# is called Encapsulation and is done from the item.py and/or phone.py 
# files

# print(item1.read_only_name)
# item1.read_only_name = 'BBB' ---> OUT[]: Error

# name now corresponds to the function name(self) under @property
print(item1.name) # [OUT]: MyItem
# item1.name = 'OtherTime'
# print(item1.name) # ---> [OUT]: Error

# We can also add a special method to set a new value using the 
# @[function(self) under @property].setter decorator
item1.name = 'OtherItem'
print(item1.name) # OUT[]: OtherItem