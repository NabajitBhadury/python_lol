ch = input("Enter the number: ")

arr = []
if (ch != 'q'):
    arr.append(int(ch))
else:
    exit

while (ch != 'q'):
    ch = input('Enter the number: ')
    if (ch.isdigit()):
        arr.append(int(ch))

print(sum(arr)/len(arr))
