from numpy import sqrt


def check_prime(num):
    if (num == 0 or num == 1 or num == 2):
        return False
    else:
        for flag in range(3, int(sqrt(num)) + 1):
            if (num % flag == 0):
                return False
        else:
            return True


num = int(input("Enter the range upto which you want to print the prime number: "))
for val in range(0, num):
    if (check_prime(val)):
        print(val)
    else:
        continue
