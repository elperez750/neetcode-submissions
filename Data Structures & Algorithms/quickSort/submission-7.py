# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def quickSortHelper(arr, start, end):
            if start >= end:  # Base case: Subarray has 1 or no elements
                return

            pivot_index = end  # Use the last element as the pivot
            partition_index = start  # Tracks position to place smaller elements

            for i in range(start, end):
                if arr[i].key < arr[pivot_index].key:
                    # Swap smaller elements to the front
                    arr[i], arr[partition_index] = arr[partition_index], arr[i]
                    partition_index += 1

            # Swap pivot into its correct position
            arr[partition_index], arr[pivot_index] = arr[pivot_index], arr[partition_index]

            # Recursively sort left and right subarrays
            quickSortHelper(arr, start, partition_index - 1)  # Left subarray
            quickSortHelper(arr, partition_index + 1, end)  # Right subarray

        quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
