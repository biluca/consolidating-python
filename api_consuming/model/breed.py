class Breed:

    def __init__(self, breed, country, origin, coat, pattern):
        self.breed = breed
        self.country = country
        self.origin = origin
        self.coat = coat
        self.pattern = pattern

    def __str__(self) -> str:
        return f"Breed:{self.breed}, Country:{self.country}, Origin:{self.origin}, Coat:{self.coat}, Pattern:{self.pattern}"


class BreedConverter:

    def convert(self, breed) -> Breed:
        new_breed = breed['breed']
        new_country = breed['country']
        new_origin = breed['origin']
        new_coat = breed['coat']
        new_pattern = breed['pattern']

        return Breed(new_breed, new_country, new_origin, new_coat, new_pattern)
