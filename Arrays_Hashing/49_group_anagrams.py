# https://leetcode.com/problems/group-anagrams/
# 49
from typing import List

#Time: O(n*mlogm) where n is the number of strings and m is the average length of a string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []

        if len(strs) == 1:
            return [strs]

        # create a dictionary with letters
        letter_dict = {}
        for string in strs:
            num_value = self.calculate_values(string)
            if num_value in letter_dict:
                letter_dict[num_value].append(string)
            else:
                letter_dict[num_value] = [string]
        
        return list(letter_dict.values())
    
    def is_prime(self, num) -> bool:
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_prime_map(self) -> dict:
        primes = []
        num = 2  # Start with the smallest prime
        while len(primes) < 26:
            if self.is_prime(num):
                primes.append(num)
            num += 1

        prime_map = {}
        for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
            prime_map[letter] = primes[i]

        return prime_map
    
    def calculate_values(self, string: str) -> int:
        prime_map = self.generate_prime_map()
        value = 1
        for letter in string:
            value *= prime_map[letter]
        return value


if __name__ == "__main__":
    string = "tea"
    sorted_string = sorted(string)
    # create a dictionary with letters

    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(s.groupAnagrams([""]))
    print(s.groupAnagrams(["a"]))
    print(s.groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]))
