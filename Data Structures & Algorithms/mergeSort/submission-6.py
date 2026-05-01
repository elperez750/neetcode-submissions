# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def mergeHelper(s, m, e, arr):
            # s = 0
            # e = 1
            # m = 1
            L = arr[s: m + 1]
            R = arr[m+1: e+1]


            #pointer for left array
            i = 0
            #pointer for right array
            j = 0
            #pointer for where to place element in array
            k = s



            while i < len(L) and j < len(R):
                if L[i].key <= R[j].key:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j+= 1    
                k += 1



            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1



        def split(s, e, arr):
            if e - s + 1 <= 1:
                return arr

            m = (s + e) // 2

            split(s, m, arr)
            split(m+1, e, arr)

            mergeHelper(s, m, e, arr)

            return arr




        return split(0, len(pairs)-1, pairs)
