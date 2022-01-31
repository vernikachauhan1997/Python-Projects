l1 = ['apple','banana','kiwi','pomogranate','orange']

for index,items in enumerate(l1,start = 0):#It is useful for the loops over list, tuples,string,dictionary where we want index and values
    if index%2 == 0:
        print(index,items)