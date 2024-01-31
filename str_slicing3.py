# Write a python program to take 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1.

str1 = input("Enter the string 1: ")
str_len1 = len(str1)
str_mid = str_len1//2

str2 = input("Enter the string 2: ")

slice1 = slice(0, str_mid)
slice2 = slice(str_mid, str_len1)

print(str1[slice1] + str2 + str1[slice2])
