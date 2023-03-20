import random

from custom_types import *


def is_cover(
    universe: Universe, subsets: Subset, poss_solution: PossibleSolution
) -> bool:
    # Subsets and poss_solition must have the same size
    if len(poss_solution) != len(subsets):
        print("Pb with the size of the solution")
        return False
    # If so, continue and compute what the solution covers
    covered = set()
    for i in range(0, len(poss_solution)):
        if poss_solution[i] == 1:
            covered |= subsets[i]
    # If the solution covers the universe then OK
    if universe == covered:
        # print('It is a cover !')
        return True
    else:
        # print('Not a cover')
        return False


def get_random_bit(nb_One: int = 3) -> int:
    """Return a random char from the allowed charmap."""
    """ Pour augmenter la rapidité de l'initialisation 1=2/3 et 0=1/3 """
    l = [0]
    l.extend([1 for i in range(0, nb_One)])
    random.shuffle(l)
    return int(l[0])


def get_random_individual(universe: Universe, subsets: Subsets) -> List[int]:
    """Create a new random individual."""
    new_poss_individual = [get_random_bit() for _ in range(len(subsets))]
    while not (is_cover(universe, subsets, new_poss_individual)):
        new_poss_individual = [get_random_bit() for _ in range(len(subsets))]

    return new_poss_individual


def get_random_population(
    universe: Universe, subsets: Subsets, size_of_population: int
) -> List[int]:
    """Create a new random population, made of `POPULATION_COUNT` individual."""
    return [get_random_individual(universe, subsets) for _ in range(size_of_population)]


def weighted_random_order(
    list, proba
):  # Fonction modifiée : passer de sélection à ordonct.
    Proba_by_position = []
    Selected_items = []
    Min_Proba = min(proba)
    Ratio_to_One = 1 / Min_Proba

    for s, p in zip(list, proba):
        for i in range(0, (int(round((p * Ratio_to_One), 0)) + 1)):
            Proba_by_position.append(s)

    while len(Proba_by_position) >= 1:
        random.shuffle(Proba_by_position)
        selected_item = Proba_by_position[0]
        Selected_items.append(selected_item)

        Proba_by_position = [i for i in Proba_by_position if i != selected_item]

    return Selected_items
