def coin_flips(n):
    if n == 1:
        return ['H', 'T']

    already_flipped = coin_flips(n -  1)
    history_plus_heads = list(el + 'H' for el in already_flipped)
    history_plus_tails = list(el + 'T' for el in already_flipped)
    return history_plus_heads + history_plus_tails

print(coin_flips(3))