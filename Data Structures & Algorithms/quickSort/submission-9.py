# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def helper(arr, s, e):
            if e <= s:
                return arr

            pivot = e
            pts = s
            print(pivot, pts)
            for i in range(s, e):
                if arr[i].key < arr[pivot].key:
                    arr[i], arr[pts] = arr[pts], arr[i]
                    pts += 1
            

            arr[pivot], arr[pts] = arr[pts], arr[pivot]

            helper(arr, s, pts-1)
            helper(arr, pts+1, e)

            

        helper(pairs, 0, len(pairs)-1)

        return pairs

        