'''
4. Write a script that combines three dictionaries by updating the FIRST one
(you can use dicts from the previous task).
'''

print('First dictionary: ', {'foo': 'bar', 'bar': 'buz'})
print('Second dictionary: ', {'dou': 'jones', 'USD': 36})
print('Third dictionary: ', {'AUD': 19.2, 'name': 'Tom'})

dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}
change_dict = input('Change first dictionary: ')
dict_1['bar'] = change_dict

dict_1.update(dict_2)
dict_1.update(dict_3)
print(dict_1)

