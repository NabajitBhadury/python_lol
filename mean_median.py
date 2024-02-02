# Write a python program to find the mean and median of a set of elements.

from numpy import sort


def calculate_mean(numbers):
    total = sum(numbers)
    mean = total/len(numbers)
    return mean


def calcualte_median(numbers):
    sorted_numbers = sort(numbers)
    length = len(sorted_numbers)

    if (length % 2 == 0):
        mid = length // 2
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        median = sorted_numbers[length//2]
    return median


list_numbers = [12, 69, 23, 53, 96]

print(calculate_mean(list_numbers))
print(calcualte_median(list_numbers))
