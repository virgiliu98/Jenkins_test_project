a = [1, 2, '3', 4, 5, 6]
b = [2*x for x in a]
print(a.index(4 and 5))  # list comprehension

# generator in list comprehension
# e = [print(x+1) for x in range(10)]

d = {}
d['nome'] = 'ciao'
d['robe'] = a
print(d)

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

print(portfolio[1][1])  # usare il dizionario con le tuple
