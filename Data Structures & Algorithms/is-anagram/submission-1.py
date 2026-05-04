class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_one = {}
        dict_two = {}

        for i in range(len(s)):
            if s[i] in dict_one:
                dict_one[s[i]] += 1
            else:
                dict_one[s[i]] = 1

        
            if t[i] in dict_two:
                dict_two[t[i]] += 1
            
            else:
                dict_two[t[i]] = 1


        return dict_one == dict_two