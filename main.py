class cat:
    # this is called the constructor
    # it will create a cat for us in code
    # to create a cat5, we need a given_name and given_colour
    # self is the current cat we are creating
    def __init__(self, given_name, given_colour):
        self.name = given_name
        self.colour = given_colour
        # init stands for initializer 
# An instance of cat
# An instance is a specific occurence of a class 
mimi = cat("mimi", "Brown")
print(mimi.name)