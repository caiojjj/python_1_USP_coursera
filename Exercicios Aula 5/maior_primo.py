def maior_primo(x):
    primo = 0
    i = 1
    if x == 2:
        primo = x
    if x == 3:
        primo = 3
    if x == 5:
        primo = 5
    if x == 7:
        primo = 7
        return primo
    while i < x:
        if i % 2 != 0 and i % 3 != 0 and i % 5 and i % 7 != 0:
            primo = i
        i += 1
    return primo