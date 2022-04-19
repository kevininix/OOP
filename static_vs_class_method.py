#When to use class method vs static method


#Static should be used when doing something not unique to the class instances
class Item:
    @staticmethod
    def is_integer():
#could also have been written as

def is_integer():
    '''
    
    '''

class Item:
    '''
    '''
#The first one is still a better option bc the method it's somehow related to the Class

#Class methods should be used for instanciating from some strictured data elsewhere
class Item:
    @classmethod
    def instantiate_from_something(cls):
        '''
        '''