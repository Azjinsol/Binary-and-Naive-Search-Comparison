import random
import time

#naive search scans the entire list to find the target
def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

#binary search scans in the middle of the list to find the target
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    
    
    midpoint = (low + high) // 2

    if high < low:
        return -1

    if l[midpoint] == target:
        return midpoint

    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        #target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)


if __name__=='__main__':

    length = 1000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    #Comparing both searches by its seconds
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive seart time: ", (end - start)/length, "second")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary seart time: ", (end - start)/length, "second")
