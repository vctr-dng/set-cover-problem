from py.custom_types import *
from py.load_scp import load_scp
from tqdm import tqdm
from py.utils import is_cover


def naive_set_cover(
    universe: Universe, subsets: Subsets, verbose: bool = False
) -> Subsets:
    """Find a collection of families of subsets that covers the universal set"""
    solution_collection = []
    best_solution_cost = len(subsets)  # worst cost ever

    # Explore all the possible solutions by enumeration of integers
    # between 1 and pow(2,n)-1 in binary representation
    for i in range(1, 2 ** len(subsets)):
        # built solution (list of ints)
        solution = []
        bit_string = bin(i)[2:].zfill(len(subsets))
        for c in bit_string:
            solution.append((int(c)))
        if verbose:
            print("essai:", solution)

        # If a cover is found
        if is_cover(universe, subsets, solution) == True:
            # compute cost: nr of subsets in the solution
            solution_cost = sum(solution)

            # if this solution has better or equal cost
            if solution_cost <= best_solution_cost:
                solution_subsets = []
                for idx in range(0, len(solution)):
                    if solution[idx] == 1:
                        solution_subsets.append(subsets[idx])
                if solution_cost < best_solution_cost:
                    best_solution_cost = solution_cost
                    # reset of collection of best solutions
                    solution_collection = []
                # add a solution to the best solution collection
                solution_collection.append(solution_subsets)
    return solution_collection


def main() -> None:
    universe = set(range(1, 11))
    subsets = [
        {1, 2, 3, 8, 9, 10},
        {1, 2, 3, 4, 5},
        {4, 5, 7},
        {5, 6, 7},
        {6, 7, 8, 9, 10},
    ]
    ## Unit Tests
    print("All:", is_cover(universe, subsets, [1, 1, 1, 1, 1]))
    print("Best:", is_cover(universe, subsets, [0, 1, 0, 0, 1]))
    print("Not a cover:", is_cover(universe, subsets, [0, 0, 1, 1, 0]))

    # universe, subsets, subset_cost_vect = load_scp('./data/scpcyc06.txt')
    # universe, subsets, subset_cost_vect = load_scp("./data/scpd5.txt")
    print("Subsets: ", subsets)
    print("Universe: ", universe)
    print("**************** SOLVING ****************")

    best_covers = naive_set_cover(universe, subsets)
    print("Collection of best covers: ", best_covers)


if __name__ == "__main__":
    main()
