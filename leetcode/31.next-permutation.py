#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (38.56%)
# Likes:    17081
# Dislikes: 4353
# Total Accepted:    1.2M
# Total Submissions: 3M
# Testcase Example:  '[1,2,3]'
#
# A permutation of an array of integers is an arrangement of its members into a
# sequence or linear order.
# 
# 
# For example, for arr = [1,2,3], the following are all the permutations of
# arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# 
# 
# The next permutation of an array of integers is the next lexicographically
# greater permutation of its integer. More formally, if all the permutations of
# the array are sorted in one container according to their lexicographical
# order, then the next permutation of that array is the permutation that
# follows it in the sorted container. If such arrangement is not possible, the
# array must be rearranged as the lowest possible order (i.e., sorted in
# ascending order).
# 
# 
# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does
# not have a lexicographical larger rearrangement.
# 
# 
# Given an array of integers nums, find the next permutation of nums.
# 
# The replacement must be in place and use only constant extra memory.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3]
# Output: [1,3,2]
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,1]
# Output: [1,2,3]
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,1,5]
# Output: [1,5,1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        n=len(nums)
        ind = -1
        for i in range(n-2,-1,-1) :
            if(nums[i]<nums[i+1]):
                ind = i
                break
        
        if(ind==-1):
            i=0
            j=n-1
            while(i<=j):
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        else:

            for i in range(n-1,ind,-1):
                if(nums[i]>nums[ind]):
                    nums[i],nums[ind]=nums[ind],nums[i]
                    break
        
            
            i=1
            j=ind+1
            while(j<=n-i):
                nums[j],nums[n-i]=nums[n-i],nums[j]
                j+=1
                i+=1

        
# @lc code=end

