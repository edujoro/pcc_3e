favorite_numbers = {}
favorite_numbers['patricia'] = ['5']
favorite_numbers['brunella'] = ['10','2',]
favorite_numbers['chio'] = ['11','30']
favorite_numbers['brenda'] = ['12']
favorite_numbers['betty'] = ['14','6','8']
favorite_numbers['britani'] = ['25','1','4','8']

for key,numbers in favorite_numbers.items():
    print(f'{key}')
    print('los numeros favoritos son:')
    for number in numbers:
        print(f'{number}')