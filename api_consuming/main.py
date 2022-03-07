from client import *
from model.fact import *
from model.breed import *


def get_single_fact():
    factDTO = get_fact()
    factConverter = FactConverter()
    fact = factConverter.convert(factDTO)
    print(fact)


def get_multiple_facts():
    factsDTO = get_facts()
    factsList = factsDTO['data']
    factConverter = FactConverter()
    facts = []
    for fact in factsList:
        facts.append(factConverter.convert(fact))

    for fact in facts:
        print(fact.get_fact())


def get_multiple_breeds():
    breedsDTO = get_breeds()
    breedsList = breedsDTO['data']
    breedConverter = BreedConverter()
    breeds = []

    for breed in breedsList:
        breeds.append(breedConverter.convert(breed))

    for breed in breeds:
        print(breed)


get_single_fact()
get_multiple_facts()
get_multiple_breeds()
