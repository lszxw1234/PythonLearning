import copy
def bubble_Sort(list):
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

def insertion_Sort(list):
    n = len(list)
    for i in range(1,n):
        temp = list[i]
        j = i
        while j > 0 and temp < list[j-1]:
            list[j] = list[j-1]
            j -= 1
        list[j] = temp
    return list

def shell_Sort(list):
    n = len(list)
    #initial step
    step = 2
    gap = n // step
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
        gap = gap // step
    return list


def heap_Sort(list):
    # create max heap
    for start in range((len(list) - 2) // 2, -1, -1):
        sift_Down(list, start, len(list) - 1)

    # heap sort
    for end in range(len(list) - 1, 0, -1):
        list[0], list[end] = list[end], list[0]
        sift_Down(list, 0, end - 1)
    return list


# adjust max heap.
def sift_Down(lst, start, end):
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break


def merge_Sort(list):
    if len(list) <= 1:
        return list
    middle = len(list)//2
    left = merge_Sort(list[:middle])
    right = merge_Sort(list[middle:])
    return merge(left,right)

def merge(left,right):
    l, r = 0,0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result



#Test
list = [3,1,2,5,6,9,4]
list1 = copy.copy(list)
list2 = copy.copy(list)
list3 = copy.copy(list)
list4 = copy.copy(list)
list5 = copy.copy(list)
list6 = copy.copy(list)

print (bubble_Sort(list1))
print (selection_Sort(list2))
print (insertion_Sort(list3))
print (shell_Sort(list4))
print (heap_Sort(list5))
print (merge_Sort(list6))