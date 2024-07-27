person1 = {
    'name': 'matt',
    'age': 30,
    'sex': 'boy'
}

person2 = {
    'name': 'george',
    'age': 45,
    'sex': 'boy'
}

person3 = {
    'name': 'kara',
    'age': 26,
    'sex': 'girl'
}

person4 = {
    'name': 'madonna',
    'age': 40,
    'sex': 'girl'
}

person5 = {
    'name': 'jack',
    'age': 60,
    'sex': 'boy'
}

person6 = {
    'name': 'max',
    'age': 28,
    'sex': 'boy'
}

person7 = {
    'name': 'kass',
    'age': 20,
    'sex': 'girl'
}

person8 = {
    'name': 'sousie',
    'age': 34,
    'sex': 'girl'
}


people = [person1,person2,person3,person4,person5,person6,person7,person8]
boy = []
girl = []
above = []
below = []
sort_by = input('how would you like to sort people?\nage or sex\n')
if sort_by == 'sex':
    for p in people:
        if p['sex'] == 'boy':
            boy.append(p)
        elif p['sex'] == 'girl':
            girl.append(p)

    print(f'boys')
    for o in boy:
        print(o)
    print(f'girls')
    for i in girl:
        print(i)

elif sort_by == 'age':
    split = int(input('what age do you want to split by?'))
    for p in people:
        if p['age'] >= split:
            above.append(p)
        elif p['age'] < split:
            below.append(p)

    print(f'People above {split}')
    for a in above:
        print(a)
    print(f'people below {split}')
    for a in below:
        print(a)
else:
    print('invalid input')