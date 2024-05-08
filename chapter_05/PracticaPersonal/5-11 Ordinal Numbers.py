numbers = [1,2,3,4,5,6,7,8,9]
ordinals = []
for number in numbers:
    if number == 1:
        ordinals.append('1st')
    elif number == 2:
        ordinals.append('2nd')
    elif number == 3:
        ordinals.append('3rd')
    else:
        ordinals.append(f'{number}th')

for ordinal in ordinals:
    print(ordinal)