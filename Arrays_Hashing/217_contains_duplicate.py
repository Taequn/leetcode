#https://leetcode.com/problems/contains-duplicate/
#217
from typing import List

#Complexity: O(n)
#Space: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        set_nums = set(nums)
        if len(set_nums) == len(nums):
            return False

        return True
    
if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
        