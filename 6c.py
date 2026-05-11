import random
from math import factorial


def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True


def shuffle(arr, rng=random):
    """Fisher-Yates shuffle. Returns the number of swaps performed."""
    swaps = 0
    for i in range(len(arr) - 1, 0, -1):
        j = rng.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
        swaps += 1
    return swaps


def bogo_sort_iterations(n, max_iterations=1_000_000, rng=random):
    """Runs bogo-sort from a non-sorted input of size n."""
    arr = list(range(n, 0, -1))

    if is_sorted(arr):
        return 0, 0, False

    iterations = 0
    swaps = 0

    while iterations < max_iterations:
        swaps += shuffle(arr, rng)
        iterations += 1

        if is_sorted(arr):
            return iterations, swaps, False

    return iterations, swaps, True


def geometric_probability(n, k):
    p = 1 / factorial(n)
    return ((1 - p) ** (k - 1)) * p


def simulate(n, trials=20_000, seed=42):
    rng = random.Random(seed)
    total_iterations = 0
    total_swaps = 0
    timeouts = 0

    for _ in range(trials):
        iterations, swaps, timed_out = bogo_sort_iterations(n, rng=rng)
        if timed_out:
            timeouts += 1
            continue
        total_iterations += iterations
        total_swaps += swaps

    valid_trials = trials - timeouts
    return {
        "trials": trials,
        "valid_trials": valid_trials,
        "timeouts": timeouts,
        "avg_iterations": total_iterations / valid_trials,
        "avg_swaps": total_swaps / valid_trials,
    }


if __name__ == "__main__":
    n = 4
    trials = 20_000
    n_factorial = factorial(n)
    result = simulate(n, trials)

    print(f"n = {n}")
    print(f"n! = {n_factorial}")
    print(f"P(exito por shuffle) = 1/{n_factorial}")
    print()
    print(f"E[I] teorico       = {n_factorial}")
    print(f"E[I] simulado      = {result['avg_iterations']:.2f}")
    print(f"E[swaps] teorico   = {(n - 1) * n_factorial}")
    print(f"E[swaps] simulado  = {result['avg_swaps']:.2f}")
    print(f"ensayos validos    = {result['valid_trials']} de {result['trials']}")
    print()
    print("Primeros valores de la distribucion geometrica:")
    for k in range(1, 6):
        print(f"P(I = {k}) = {geometric_probability(n, k):.6f}")
