def minimalNumberOfCoins(coins, price):
    '''
    U- Use the least amount of coins to buy something given an array of coin values and a price.
    P- begining with the largest coin, use floor division to find the 
    number of those coins that can be used, then send the remaining price to the next largest coin until the price is covered.
    E-
    '''
    num_coins = 0
    i = len(coins)-1
    while price != 0:
        if price >= coins[i]:
            num_coins += price//coins[i]
            price = price % coins[i]
        i -= 1
    return num_coins