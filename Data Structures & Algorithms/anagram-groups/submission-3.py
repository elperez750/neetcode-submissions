class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            print(word)
            new_string = "".join(sorted(word))
            if new_string in anagrams:
                anagrams[new_string].append(word)
            else:
                anagrams[new_string] = []
                anagrams[new_string].append(word)
        return [arrays for arrays in anagrams.values()]
