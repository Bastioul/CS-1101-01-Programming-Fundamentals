#the variable name is the object, the list are the values of the objects
bob = ['tango', 'charlie']
vincent = ['vincent', 'operation skunkrepellant', 'operation psychonaut', 'operation mastermind']
spy = [vincent, bob]
#all objects below point to the orignal object's location
bravo = vincent
alpha = vincent
sierra = vincent
tango = vincent
bast = vincent
charlie = bob
lima = bob
november = bob
zebra = bob
def nsa_database_check():
    check = input('Who is the operative?')
    for i in range(len(spy)):
        if spy[i][0] == check:
            #This is to demonstrate 'is' operater code will function the same if this if statement is removed
            if spy[i] is alpha or spy[i] is lima:
                all_known_alias = [name for name, val in globals().items() if val is spy[i]]
                print(f'Here is a list of known aliases for operative {check}')
                for b in range(len(all_known_alias)):
                    print(all_known_alias[b])
                operative = spy[i]
                service_id = id(operative)
                # This is to demonstrate that all objects point to same address, and they have the same identity
                print(f'Opertive ID is {service_id}.')
                print(id(alpha))
                # this is a function that takes an argument and adds to vincent's list of assignments
                def add_assignment(operative):
                    added = input(f'What would you like to assign to {operative[0]}...')
                    operative.append(added)
                    print(f'{operative[0]} is now assigned to..')
                    for i in range(1, len(operative)):
                        print(operative[i])
                    return
                return add_assignment(operative)
        else:
            print('Operative does not exist')
            return nsa_database_check()
nsa_database_check()
