# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def mergeTogether(array, l, m, r):
            left_array = array[l:m+1]
            right_array = array[m+1:r+1]
            #left array = [3]
            #right array = [2]

            i = 0 #pointer for left array
            j = 0 #pointer for right array
            k = l #pointer for pairs

            while i < len(left_array) and j < len(right_array):
                if left_array[i].key <= right_array[j].key:
                    array[k] = left_array[i]
                    i += 1
                else:
                    array[k] = right_array[j]
                    j+= 1
                k+= 1


            while i < len(left_array):
                array[k] = left_array[i]
                i += 1
                k += 1
            

            while j < len(right_array):
                array[k] = right_array[j]
                j += 1
                k+= 1



        def mergeSortHelper(array, l, r):
            if r - l + 1 <= 1:
                return array

            m = (r + l) // 2
            mergeSortHelper(array, l, m)
            mergeSortHelper(array, m+1, r)
            mergeTogether(pairs, l, m, r)


            return array

        return mergeSortHelper(pairs, 0, len(pairs)-1)