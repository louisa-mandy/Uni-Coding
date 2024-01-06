#class inheritance

class Animal : 
    def __init__(self,name):
        self.name = name 
    
    def display_info(self):
        print(f"{self.name} is an animal")

class Mamal (Animal):
    def __init__(self,name):
        super().__init__(name)
        self.is_warm_blooded = True 

    def display_info(self):
        super().display_info()
        print(f"{self.name} is a warm blooded animal")


class NonMarineMamal (Mamal):
    def __init__(self,name):
        super().__init__(name)
        self.can_swim = False 
    
    def display_info(self):
        super().display_info()
        
        if self.can_swim:
            print(f"{self.name} can swim")
        else:
            print(f"{self.name} cannot swim")
            
class NonWingedMamal (Mamal):
    def __init__(self,name):
        super().__init__(name)
        self.can_fly = True
    
    def display_info(self):
        super().display_info()
        
        if self.can_swim:
            print(f"{self.name} can fly")
        else:
            print(f"{self.name} cannot fly")


class Dog(NonMarineMamal, NonWingedMamal):
    def __init__(self,name):
        super().__init__(name)
        self.has_legs = 4 
        self.can_fly = False 

    def display_info(self):
        super().display_info()
        
        if self.can_swim:
            print(f"{self.name} doesn't have 4 legs")
        else:
            print(f"{self.name} has 4 legs")



# initiate dog 

dog = Dog("Dog")
dog.display_info()

# initiate non marine object (bat)

bat = NonMarineMamal("Bat")
bat.display_info()