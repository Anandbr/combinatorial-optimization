def can_partition(num, sum):
    n = len(num)
    dp = [False for x in range(sum + 1)]
    dp[0] = True
    for s in range(1, sum + 1):
        dp[s] = num[0] == s
    for i in range(1, n):
        for s in range(sum, -1, -1):
            if not dp[s] and s >= num[i]:
                dp[s] = dp[s - num[i]]

    return dp[sum]

def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()
