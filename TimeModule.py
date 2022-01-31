import time #Datetime and calendar module

# initial = time.time()
# for i in range(13):
#     print("My name is Harry")
# print('Time to run for loop is',time.time() -initial)

# initial1 = time.time()
# n = 0
# while n<13:
#     print("My name is Harry")
#     n+=1
# print('Time to run while loop is',time.time() -initial1)

todaytime = time.asctime(time.localtime(time.time()))
print(todaytime)

print(time.asctime(time.gmtime()))