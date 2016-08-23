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

def selection_sort(list):
    n=len(list)
   for i in range (0,n):
       min = i
       for j in range(i+1,n):
           if list[j]<list[min]:
               min=j
               list[min],list[i]=list[i],list[min]
    return list



list1 = [3,1,2,5,6,9,4]
list2 = copy.copy(list1)
print(bubble_sort(list1))
print (selection_Sort(list2))