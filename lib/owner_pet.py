class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        else:
            self.pet_type= pet_type
        self.owner = owner
        self.add_pet_all(self)
        
    def add_pet_all(self, pet):
        self.all.append(pet)



class Owner:
    def __init__(self, name):
        self.name = name 
        self._pets = []  

    def pets(self):
        return Pet.all
    
    def add_pet(self, pet):
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        sorted_pets = sorted(Pet.all, key=lambda pet: pet.name)
        return sorted_pets