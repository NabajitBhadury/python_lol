# Take a string of length greater than 2, return a string except 1 st and last characters.

str = input("Enter the string: ")
str_len = len(str)

if (str_len < 2):
    print("String length is less than 2")
    exit

# Here in this code we have made a slice object that takes two parameter from where to slice and till how much
slice_obj = slice(1, str_len - 1)

print(str[slice_obj])
