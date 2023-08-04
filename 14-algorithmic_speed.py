if __name__ == "__main__":
    from random import randint
    from timeit import repeat

    def run_sorting_algorithm(algorithm, array):
        # algorithm function if it's not the built-in `sorted()`.
        setup_code = f"from __main__ import {algorithm}" \
            if algorithm != "sorted" else ""

        stmt = f"{algorithm}({array})"

        # Execute the code ten different times and return the time
        # in seconds that each execution took
        times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

        # minimum time it took to run
        print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")