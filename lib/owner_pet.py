class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type.")
        self.pet_type = pet_type

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner.")
        self._owner = owner

        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        if not isinstance(new_owner, Owner):
            raise Exception("Owner must be an instance of Owner.")
        self._owner = new_owner

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Associate a Pet with this Owner."""
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet.")
        pet.owner = self

    def get_sorted_pets(self):
        """Return pets sorted alphabetically by their names."""
        return sorted(self.pets(), key=lambda pet: pet.name)