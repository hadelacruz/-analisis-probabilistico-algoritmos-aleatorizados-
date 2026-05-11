import random
from math import e, factorial


def expected_comparisons(n):
    """Expected comparisons in Theorem 2: sum_{k=1}^{n-1} 1/k!."""
    if n < 2:
        return 0.0
    return sum(1 / factorial(k) for k in range(1, n))


def count_comparisons_until_decision(permutation):
    comparisons = 0
    for i in range(len(permutation) - 1):
        comparisons += 1
        if permutation[i] > permutation[i + 1]:
            break
    return comparisons


def simulate(n, trials=100_000, seed=42):
    random.seed(seed)
    base = list(range(1, n + 1))
    total = 0

    for _ in range(trials):
        arr = base[:]
        random.shuffle(arr)
        total += count_comparisons_until_decision(arr)

    return total / trials


def print_tail_sum_table(n):
    accumulated = 0.0
    print("k | P[I_k] = 1/k! | suma acumulada")
    print("--+----------------+----------------")
    for k in range(1, n):
        probability = 1 / factorial(k)
        accumulated += probability
        print(f"{k:2d}| {probability:14.9f} | {accumulated:14.9f}")


if __name__ == "__main__":
    n = 10
    trials = 1_000_000

    print_tail_sum_table(n)
    print()
    print(f"E[C] teorico para n={n}: {expected_comparisons(n):.6f}")
    print(f"Limite e - 1:            {e - 1:.6f}")
    print(f"Simulacion ({trials}):      {simulate(n, trials):.6f}")
