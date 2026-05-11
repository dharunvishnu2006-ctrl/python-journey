class Restaurant:
    def __init__(self, name, location, rating):
        self.name = name
        self.location = location
        self.rating = rating
    
    def describe(self): 
        print(f"{self.name} is located in {self.location} with rating {self.rating}")

murugan = Restaurant("Murugan Idli Shop", "Chennai", 4.5)
saravana = Restaurant("Saravana Bhavan", "Mumbai", 4.2)

murugan.describe() 
saravana.describe()