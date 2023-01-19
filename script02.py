import names

for i in range(5):
    name = names.get_first_name()
    while len(name) != 8:
        name = names.get_first_name()
    print(name)
