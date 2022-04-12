#Insertion_Sort(сортировка вставкой)

import numpy
def random_ar():
    random_array=numpy.random.random_integers(1,100,12)
    print('Array: ', random_array)
    return(random_array)
'''
def sort_array_insertion(array):
    for i in range(1, len(array)):
        insertion_item=array[i]
        j=i-1
        while j>=0 and array[j]>insertion_item:
            array[j+1]=array[j]
            j-=1
        array[j+1]=insertion_item
sort_array_insertion(random_array)
print(random_array)
'''
#random_ar()
