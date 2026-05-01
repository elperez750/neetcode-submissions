# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def merge(left, right):
            result = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i].key <= right[j].key:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            # Add remaining elements from left or right
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        
        def split(array):
            if len(array) <= 1:  # Base case: single element or empty array
                return array
            
            mid = len(array) // 2
            left = split(array[:mid])  # Recursively split left half
            right = split(array[mid:])  # Recursively split right half
           
            # Merge the sorted halves
            return merge(left, right)
        
        return split(pairs)
