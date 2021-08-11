##############CLASSES################

class Human:

    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"
    
    # namespaces. Methods(or objects or attributes) like: __init__, __str__,
    # You should not invent such names on your own.
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name

        # Initialize property
        self._age = 0

    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    # Another instance method
    def sing(self):
        return 'Hello Hello! one two three, one two three'

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    # A property is just like a getter.
    # It turns the method age() into a read-only attribute of the same name.
    # There's no need to write trivial getters and setters in Python, though.
    @property
    def age(self):
        return self._age

    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age


# When a Python interpreter reads a source file it executes all its code.
# This __name__ check makes sure this code block is only executed when this
# module is the main program.
if __name__ == '__main__':
    # Instantiate a class
    i = Human(name="Ian")
    i.say("hi")                    
    j = Human("Joel")
    j.say("hello")                  
    # i and j are instances of type Human, or in other words: they are Human objects

    # Call our class method
    i.say(i.get_species())       
    # Change the shared attribute
    Human.species = "H. neanderthalensis"
    i.say(i.get_species())         
    j.say(j.get_species())         

    # Call the static method
    print(Human.grunt())            # => "*grunt*"

    # Static methods can be called by instances too
    print(i.grunt())                # => "*grunt*"

   #####################END##################################
