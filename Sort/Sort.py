import copy
def bubble_sort(list):
    length = len(list)
    #first reduce
    for i in range(length):
        #second reduce
        for j in range(1,length-i):
            if list[j-1] > list[j]:
                #replace these two number.
                list[j-1],list[j] = list[j],list[j-1]
    return list

def selection_Sort(list):
    n = len(list)
    for i in range(0,n):
        m = i
        for j in range(i + 1, n):
            if list[m]>list[j]:
                m = j
        list[m],list[i] = list[i], list[m]
    return list

def insertion_sort(list):
    n = len(list)
    for i in range(1,n):
        temp = list[i]
        j = i
        while j > 0 and temp < list[j-1]:
            list[j] = list[j-1]
            j -= 1
        list[j] = temp
    return list
def shell_sort(list):
    n = len(list)
    #initial step
    step = 2
    gap = n / step
    while gap > 0:
        for i in range(0,gap):
            j = i + gap
            while j < n:
                k = j - gap
                key = list[j]
                while k >= 0:
                    if list[k] > key:
                        list[k + gap] = list[k]
                        list[k] = key
                    k -= gap
                j += gap
        gap /= step
    return list



list = [3,1,2,5,6,9,4]
list1 = copy.copy(list)
list2 = copy.copy(list)
list3 = copy.copy(list)
list4 = copy.copy(list)

print bubble_sort(list1)
print selection_Sort(list2)
print insertion_sort(list3)
print shell_sort(list4)