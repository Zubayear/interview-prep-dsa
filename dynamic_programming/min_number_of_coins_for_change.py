def min_number_of_coins_for_change(total, coins):
    """
    @param total: 6
    @param coins: [1,2,4]
    @return:
    """
    amounts = [float("inf") for _ in range(total+1)]
    amounts[0] = 0 # min number of coin needed to make change for 0 is 0
    for coin in coins:
        for amount in range(len(amounts)):
            # if we can make amount with the coin
            # i.e. can we make amount 1, 2, 3 etc. with $1
            if coin <= amount:
                amounts[amount] = min(amounts[amount], 1 + amounts[amount - coin])
    return amounts[total] if amounts[total] != float("inf") else -1
