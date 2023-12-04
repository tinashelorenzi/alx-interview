def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes_up_to_n(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def play_round(n):
        primes = get_primes_up_to_n(n)
        num_moves = [0] * (n + 1)
        num_moves[0] = num_moves[1] = 1  # 0 and 1 are not prime

        for prime in primes:
            for i in range(prime, n + 1, prime):
                num_moves[i] += 1

        total_moves = sum(num_moves)
        # If the total number of moves is even, Maria wins; otherwise, Ben wins
        return "Maria" if total_moves % 2 == 0 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for round_num in range(x):
        winner = play_round(nums[round_num])
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Test the provided example
# print("Winner: {}".format(isWinner(3, [4, 5, 1])))