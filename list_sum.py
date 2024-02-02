list1 = []
list2 = []

for i in range(5):
    num1 = int(input('Enter the element of list1: '))
    list1.append(num1)

for i in range(5):
    num1 = int(input('Enter the element of list2: '))
    list2.append(num1)

list3 = []

for i in range(5):
    list3.append(list1[i] + list2[i])

print(list3)
