**Problem Statement**

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

**test case**:

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

**Constraints**:
-2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

**Approach**:

For each element that we iterate through in nums, we store their complements as keys in the hash map with their values being in the current index. 
Note that we’re only storing these key-value pairs if the current element is not a present key in our hash map. 
If the current element exists as a key, then we can return an array with the current index and its corresponding value in the hash map since this element was inserted in a previous iteration. 
Let’s now check out the time and space complexities of this new approach.