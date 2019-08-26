import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))
my_randoms
print(my_randoms)
"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""
for number in range(1, 10):
    if number in my_randoms:
        print(f"my_randoms includes the number {number}")
    else:
        print(f"my_randoms does not include the number {number}")

"""
Using IF...IN to check if number is in my_randoms list
"""