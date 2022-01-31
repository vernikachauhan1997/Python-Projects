
#How to access fils in different modes.

'''
'r'= To open a file in read mode
'w'= To open a file in write mode
'a'= To add content to the end of the file
't'- text mode(by default)
'b' = binary mode
'+'= update or read/write mode
'x' = create a file if not already exists
'''
file = "SampleInputFiile.txt"
with open('SampleInputFiile.txt','r',errors='ignore') as f:
    content = f.read()
    print(content)
    f.close
    
f = open(file) #By default, it will open file in read mode
content = f.read()
content2 = f.read(3) #Tt will read 3 characters from file.
print(content)

#line by line read
with open('SampleInputFiile.txt','r',errors='ignore') as f:
    for line in f:
        print(line) #This is how we read line by line.

#readline function
f = open('SampleInputFiile.txt')
print(f.readline())#This will read line from file line by line
print(f.readline())

#readlines function
f = open('SampleInputFiile.txt')
print(f.readlines())

# # Write to the file
f = open('SampleInputFiile.txt','w')
p = f.write("Mei bhut achi hu, thankyou!!")#Write function will return the characters prsent inside the file.
print(p)

# #Append file
f = open('SampleInputFiile.txt','a')
q = f.write("Welcome to my party")
print(q)

# #Read and write
f = open('SampleInputFiile.txt','r+')
f.read()
f.write("Today is my party.You are welcome")

#Seek and tell function
f = open(file)
f.readline()
content = f.tell()#this tell where my pointer is in the file while reading the character
contents = f.seek(45)#this function will help to set my pointer to a particular position which is passed as an arg to seek function.
print(contents)
    