'''
7. Write a script which accepts a <number>(int)
from user and generates dictionary in range <number>
where key is <number> and value is <number>*<number>
    e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}

'''

number = int(input('Enter number: '))
my_dict = {i: i*i for i in range(1, number+1)}
print('Generates dictionary in range:', number, '\n', my_dict)
