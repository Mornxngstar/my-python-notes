
friends = [
    ("Rachel", 19),
    ("Monica", 18),
    ("Phoebe",17),
    ("Joey", 16),
    ("Chandler", 21),
    ("Ross", 20)
]

age = lambda data:data[1] >= 18

over_18 = list(filter(age, friends))

for i in over_18:
    print(i)
