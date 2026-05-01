# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def quickSortHelper(arr, s, e):
            if s >= e:
                return
            
            pivot = e
            position = s
            for i in range(s, e):
                if arr[i].key < arr[pivot].key:
                    arr[i], arr[position] = arr[position], arr[i]
                    position += 1
            
            arr[position], arr[pivot] = arr[pivot], arr[position]
            
            quickSortHelper(arr, s, position - 1)
            quickSortHelper(arr, position + 1, e)

        quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
