**Problem**
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

**test case**
Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

**Solution**
A naive solution would be to check if every character in the first string is mapped to the same character in the second string for all its occurrences. But even then, two characters in the first string might still be mapped to the same character in the second string. So, we have to repeat the process for the second string as well, i.e., check if every character in the second string is mapped to the same character in the first string for all its occurrences.

