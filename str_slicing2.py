# Take 2 strings, s1, and s2 return a new string made of the first, middle and last char of each input string.

def returnSlicedStr(str):
    str_len = len(str)
    mid_idx = str_len // 2
    if (str_len < 2):
        print("String length is less than 2")
        exit

    slice_first = slice(0, 1)
    slice_last = slice(str_len - 1, str_len)
    slice_mid = slice(mid_idx, mid_idx+1)
    return str[slice_first] + str[slice_mid] + str[slice_last]


str1 = input("Enter the string 1: ")
str2 = input("Enter the string 2: ")

print(returnSlicedStr(str1) + returnSlicedStr(str2))
