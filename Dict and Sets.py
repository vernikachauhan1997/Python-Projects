#Empty dictionary
'''
dict = {}

#Normal Dictionary

d1 = {'Vernika':'Samosa',   #Dict value can be list, tuple, dict.
      'Kartika':'Dosa',
      'Arjun':'Momos'}

print(d1)
print(d1['Vernika']) #To access specific values of a key in dict
print(d1['Arjun'])

d1['Ritesh'] = 'DalChawal'#To add new Key into dictionary
print(d1)

del(d1['Arjun'])#To delete key from dictionary
print(d1)

d1['Riya'] = {'B': 'Alooparatha',
              'L': 'CholeBhature',
              'D': 'Paneer'}

print(d1)

d2 = d1.copy()
del(d2['Kartika'])
print(d2)
print(d1)

d1.update({"Prachi":"Burger"}) #To add new key into dict.
print(d1)

print(d1.values())#To access all the values of Dict
print(d1.items())#To access all the keys and their values from dict.
print(d1.get('Riya\n'))#To access specific values of a key in dict
print(d1.popitem())
'''

#Sets

a = set()#empty set
s = set({1,2,3,4,5,5,5})
s.update({7,8})
s.add(1)
s.discard(0)