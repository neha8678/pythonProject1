class Car :
    name = None
    make = None
    model = None

    def __init__(self,o_name,o_make,o_model):  #Constructor created...  #Special F(n) . called object is created...
        self.name = o_name
        self.make = o_make
        self .model = o_model

    def start_engine(self):
        print("Starting a car with the name " +self.name)
        print("Starting a car with the name " + self.make)
        print("Starting a car with the name " + self.model)

lambo=Car("lambo" , "V2" , "2024")  #Object Creation...
lambo.start_engine()

CRV = Car("CRV", "Hybrid","2024")
CRV.start_engine()