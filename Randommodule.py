import random

random.seed(50)#Seed is used to initialize random generator
print(random.random())

x = random.getstate()
print(x)

y = random.setstate(x)
print(y)

ran = random.randint(0,18)
print(ran)

ran2 = random.random() *1000 #This will generate floating point number
print(ran2)

print(random.uniform(20,60 ))# return floating pint number between the given range.

L1 = ['Vernika', 'Kartika','Sonali','Rahul']
L2 = ['Apple','Fruit','Papaya']

print(random.choice(L1)) # Choose any random Fruit for list L1
print(random.choices(L2,weights=[20,3,4],k = 24))#Print the list of K elements from the specified sequence L2,

print(random.randrange(1,20))

random.shuffle(L2)#It will shuffle the entire list.
print(L2)

print(random.sample(L1,k = 3))#This will return the list of K numbers from the Sequence L1
