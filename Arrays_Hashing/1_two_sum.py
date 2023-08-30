#https://leetcode.com/problems/two-sum/
#1
from typing import List

#Time: O(n)
#Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = dict()
        
        for i in range(len(nums)):
            number = nums[i]
            if number not in dict_nums:
                dict_nums[number] = [i]
            else:
                dict_nums[number].append(i)
        
        updated_nums = nums
        for j in range(len(updated_nums)):
            updated_nums[j] = target - updated_nums[j]
        
        
        for x in range(len(updated_nums)):
            current_index = x
            number_to_look_for = updated_nums[current_index]
            if number_to_look_for in dict_nums:
                dict_entry = dict_nums[number_to_look_for]
                for j in range(len(dict_entry)):
                    position_in_array = dict_entry[j]
                    if position_in_array != current_index:
                        return [current_index, position_in_array]