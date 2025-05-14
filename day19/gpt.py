def count_valid_designs(towels, designs):
    towels = set(towels.strip().split(","))  # Store towels in a set for O(1) lookups
    total_count = 0

    for design in designs.split("\n"):
        n = len(design)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: There's 1 way to form an empty string

        for i in range(1, n + 1):  # i is the end index of substring
            for j in range(max(0, i - max(map(len, towels))), i):  # Only check reasonable split points
                if design[j:i] in towels:
                    dp[i] += dp[j]  # Add ways from previous valid split

        total_count += dp[n]  # Add number of ways to fully segment this design

    return total_count

if __name__ == "__main__":
    with open("day19.txt") as f:
        towels, designs = f.read().split("\n\n")

    print(count_valid_designs(towels, designs))
