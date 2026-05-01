# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        def quickSortHelper(start, end):
            pivot = end
            left = i = start


            if start >= end:
                return

            for _ in range(start, end):
                print(pairs[i].key)
                if pairs[i].key < pairs[pivot].key:
                    pairs[left], pairs[i] = pairs[i], pairs[left]
                    print(pairs[left].key, pairs[i].key)
                    left += 1

                i += 1

            


            pairs[pivot], pairs[left] = pairs[left], pairs[pivot]
        
            quickSortHelper(start, left-1)
            quickSortHelper(left+1, end)
        
        quickSortHelper(0, len(pairs)-1)

        return pairs
