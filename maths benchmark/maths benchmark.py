from time import time, sleep
from pyperclip import copy

print("Welcome to maths benchmark!")
sleep(1)

a = 1
b = int(input("type in the number of times for this loop to occur: "))

print("Let's go!!!")

t1 = time()
for i in range(b):
    a = a + a
    print(a)

t2 = time()

result = t2 - t1

print("time(s) taken for calculations: ", t2 - t1)
copy(result)
print('the result has been copied to clipboard(now you can paste it anywhere)')

sleep(3)
