"""
Cracking the code interview - 16.10
"""
import random

def generate():
    birth = random.randint(0, 300)
    years = random.randint(30, 120)
    return (birth, birth+years)


N_PEOPLE = 5000

people = [
    #(1900, 1980),
    #(1910, 1956)
    generate() for n in range(N_PEOPLE)
]


def most_people_alive(people):
    current_pop = 0
    current_max = 0
    birth = [0 for n in range(301)]
    death = [0 for n in range(302)]
    for indiv in people:
        birth[indiv[0]] += 1
        death[indiv[1]+1] += 1
    for birth_year, death_year in zip(birth, death):
        current_pop += birth_year
        current_pop -= death_year
        if current_pop > current_max:
            current_max = current_pop

    
