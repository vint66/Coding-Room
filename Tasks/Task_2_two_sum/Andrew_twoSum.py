# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 13:50:27 2020

@author: apignata


Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


"""

class Solution(object):
    def twoSum(nums, target):
        #Define length to save lookups
        length = len(nums)
        #Add a combination of the two number to see if they reach the target value 
        for i in range(length):
            #print(nums[i])
            #O(n)^2
            for j in range((i+1), length):
                #print(nums[i], nums[j])
                if nums[i] + nums[j] == target:
                    return [i, j]
        
                
                
    nums =  [3,3]             
    print(twoSum(nums, target=6))