# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def mergeArrays(arr, s, m, e):
            
            left = arr[s:m+1]
            right = arr[m+1:e+1]

            j = 0 #pointer for left
            k = 0 #pointer for right
            l = s # pointer for array

            while j < len(left) and k < len(right):
                if left[j].key <= right[k].key:
                    arr[l] = left[j]
                    j += 1
                else:
                    arr[l] = right[k]
                    k += 1

                l += 1

            
            while j < len(left):
                arr[l] = left[j]
                l += 1
                j += 1

            while k < len(right):
                arr[l] = right[k]
                l += 1
                k += 1


          

            print(f"The length of left is {len(left)}")
            print(f"The length of right is {len(right)}")
            for i in left:
                print(f" left: {i.key}")


            for j in right:
                print(f"right {j.key}")



            

            

        def mergeSortHelper(pairs, s, e):
            if (e-s) + 1 <= 1:
                return pairs

            
            m = (e + s) // 2

            mergeSortHelper(pairs, s, m)
            mergeSortHelper(pairs, m + 1, e)
            mergeArrays(pairs, s, m, e)


            return pairs


        return mergeSortHelper(pairs, 0, len(pairs)-1)