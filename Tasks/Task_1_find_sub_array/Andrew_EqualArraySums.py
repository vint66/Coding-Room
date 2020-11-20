# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:00:29 2020

@author: apignata


Split arrays to two subarrays with equal sum of elements or return False.
List is not concurrent as that was not specified 

"""
    

def sortarray(array):
    list_one = []
    list_two = []
    
    #Sort from largest to smallest
    array.sort(reverse = True)
    
    #Quick check to see if the list is even or odd
    if (sum(array) % 2) != 0:
        return False
    
    #Loop to sort the number starting from largest to smallest 
    for num in array:
        #Add the new number into the smaller sum list
        if sum(list_one) <= sum(list_two):
            list_one.append(num)
        else:
            list_two.append(num)
            
    #After sorting check to see if the lists are equal        
    if sum(list_one) == sum(list_two):
        return (list_one, list_two)
    else:
        #print(list_one, list_two)
        return False
        
        
    print(list_one, list_two)
    

#Test cases
array =  [1,3,2,1,7,1,1,2]
array1 = [1,2,3,4,5]
array2 = [2,3,4,4,3,1,1]

print(sortarray(array))
print(sortarray(array1))
print(sortarray(array2))

