# Parent Class
class vehicle: 

    wheels = 4 # class level attribute assigned to all objects from the class
   
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year

        # method that we can perform on the object
        def __str__(self):
            #return a string representing the vehicle object
            return f"vehicle: {self.make}, Model {self.model}, Year: {self.year}"