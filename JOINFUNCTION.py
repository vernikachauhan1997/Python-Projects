ls = ['Apple','Mango','Pomogranate','Grapes','Orange']
var = 'Fruits'
for items in ls:
    newstr = "/".join(ls) #Join function will accept iterable object like string, tuples and List etc as an argument
    print(newstr)
    
tu = ('1','2','3','4')#example with tuples
string = 'Harry'

for item in tu:
    print(string.join(tu))#Join method accept and return only string
    
d1 = {'Name':'Ashu','lastname': 'Basu'}#example with dictionary
print(','.join(d1.values()))
print(','.join(d1.keys()))