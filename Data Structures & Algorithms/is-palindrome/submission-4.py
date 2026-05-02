class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = "".join(char.lower() for char in s if char.isalnum())
        start_ptr = 0
        end_ptr = len(cleaned) - 1
       
        while start_ptr <= end_ptr:
            if cleaned[start_ptr] != cleaned[end_ptr]:
                return False
            else:
                start_ptr += 1
                end_ptr -= 1

        return True
