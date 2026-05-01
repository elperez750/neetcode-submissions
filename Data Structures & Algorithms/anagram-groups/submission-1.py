class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_anagrams = {}

        for word in strs:
            char_count = tuple(sorted(word))
            print(char_count)
            if char_count in all_anagrams:
                all_anagrams[char_count].append(word)
            else:
                all_anagrams[char_count] = [word]

        return [array for array in all_anagrams.values()]