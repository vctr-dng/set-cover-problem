from py.custom_types import *
from py.load_scp import load_scp
from tqdm import tqdm
from timeit import Timer
from typing import Any, Tuple

from py.exhaustive_scp import naive_set_cover
from py.greedy_scp import greedy_set_cover


def main(verbose: bool = False):
    # Load data
    universe = set(range(1, 11))
    subsets = [
        {1, 2, 3, 8, 9, 10},
        {1, 2, 3, 4, 5},
        {4, 5, 7},
        {5, 6, 7},
        {6, 7, 8, 9, 10},
    ]

    # universe, subsets, subset_cost_vect = load_scp('./data/scpcyc06.txt')
    # universe, subsets, subset_cost_vect = load_scp("./data/scpd5.txt")

    if verbose:
        print(f"Subsets\n{subsets}")
        print(f"Universe\n{universe}")

    benchmarkedFunctions = [naive_set_cover, greedy_set_cover]

    print("The following functions will be benchmarked: ")
    for func in benchmarkedFunctions:
        print(f"- {func.__name__}")

    print("\n**SOLVING**\n")

    execInfo = {}
    for func in tqdm(benchmarkedFunctions):
        delta, res = time_that_once(func, universe, subsets)
        execInfo[func.__name__] = [delta, res]

    for key, value in execInfo.items():
        print(f"{key}: {'{:.4e}'.format(value[0])}")


# https://stackoverflow.com/questions/20974147/timeit-eats-return-value
def time_that_once(func, *args, **kwargs) -> Tuple[float, Any]:
    output = [None]

    def wrapper():
        output[0] = func(*args, **kwargs)

    timer = Timer(wrapper)
    delta = timer.timeit(1)
    return delta, output[0]


if __name__ == "__main__":
    main()
