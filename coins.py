"""
Given an amount of money and coin denominations
Find the optimum way dishing out the money in th most optimum way (less coins)
(i.e. $125 can be given as 100 + 20 +5)
Use a for loop through each individual coin, starting with the highest value coin (desceding order).
while using each coin buildup to the desired amount until you have passed and then go on to a smaller coin.
"""

denomintaions = [.01,.05,.1, .25, 1, 2, 5, 10, 20, 50, 100];
of_each = [0] * (len(denomintaions))



def give_change(amount, the_coins):
    total = 0;
    of_each = []
    for coin in reversed(the_coins):
        how_many = -1
        build_up = total
        while (build_up <=  amount):
            how_many = how_many +1
            build_up = build_up + coin
        if(how_many == -1):
            how_many = 0
        build_up =  coin*how_many
        total = total + build_up
        of_each.append(how_many)
    return list(reversed(of_each))


print (give_change(7314.02,denomintaions))
