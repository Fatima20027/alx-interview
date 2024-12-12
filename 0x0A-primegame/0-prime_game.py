#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game.
    """
    def sieve(n):
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                for j in range(i * i, n + 1, n):
                    prime[j] = False
        return prime

    max_num = max(nums)
    prime_cache = sieve(max_num)

    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if prime_cache[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        total_moves = prime_count[n]
        if total_moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
