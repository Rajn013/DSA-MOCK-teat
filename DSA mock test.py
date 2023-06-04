#!/usr/bin/env python
# coding: utf-8

# Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# 
# Note that you must do this in-place without making a copy of the array.
# 
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Example 2:
# Input: nums = [0]
# Output: [0]
# 
# Constraints:
# a. 1 <= nums.length <= 10^4
# b. -2^31 <= nums[i] <= 2^31 - 1

# In[3]:


def MoveZero(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right]= nums[right], nums[left]
            left += 1
            


# In[5]:


nums =[ 0, 1, 0, 3, 12]
MoveZero(nums)
print(nums)


# In[6]:


nums2 = [0]
MoveZero (nums2)
print(nums2)


# 1<= nums.lenght <= 10^4: the lenght of the nums array will be between 1 and 10000
#     -2^31 <= nums[i]<=2^31 - 1: each element nums[i] in the array will be an integer between -2^31 and 2^31 - 1
#         it has a time complexity of O(N) and the sapce complexity of O(1)
#     where N is the lenght of the input array.

# First Unique Character in a String
# 
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# 
# Example 1:
# Input: s = "leetcode"
# Output: 0
# 
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# 
# Example 3:
# Input: s = "aabb"
# Output: -1
# 
# Constraints:
# a. 1 <= s.length <= 10^5
# b. s consists of only lowercase English letters.

# In[33]:


def firstUniqChar(s):
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i

    return -1

s1 = "leetcode"
print(firstUniqChar(s1))  
s2 = "loveleetcode"
print(firstUniqChar(s2))  
s3 = "aabb"
print(firstUniqChar(s3))  


# the time complexity of O(N) where N is the lenght of the string "s". the space complexity is O(26), which simlifies to O(1), since the number of lowercase 

# In[ ]:




