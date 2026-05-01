class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = "".join(char.lower() for char in s if char.isalnum())
        print(cleaned_string)
        pointer_start = 0
        pointer_end = len(cleaned_string) - 1


        while pointer_end > pointer_start:
            
            if cleaned_string[pointer_start] != cleaned_string[pointer_end]:
                return False
            else:
                pointer_start += 1
                pointer_end -= 1
                
        return True
            
            
