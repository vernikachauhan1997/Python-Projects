l1 = ['Apple', 'Mango', 'Orange','Banana','Grapes','Kiwi']
l2 = [23,34,45,56,78,89,98]
l1.sort() #sorting method in ascending order
print(l1)
l1.reverse()#reverse method
print(l1)
l1.extend(l2)#extend method.It will add any iterable object to the end of the list
print(l1)
l1.append('Pomogranate')#This will add Pomogranate to the end of the list.
print(l1)
l1.insert(0,'Plum')#Insert method will add the value to  particular index.It accepts 2 args first is the index number and second is the value which we want to insert to particular index.
print(l1)
l1.pop(3)
print(l1)
l1.remove("Apple")#This will remove Apple from list
print(l1)
l1.index(23)
print(l1)
l1.__getitem__(5)
print(l1)

#Tuples-Immutable, same data types, no addition or deletion
t1 = ('Apple',)
print(t1)
