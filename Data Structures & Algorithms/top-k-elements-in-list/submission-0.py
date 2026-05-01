class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency_array = [[] for i in range(len(nums)+1)]
        

        #[1, 2, 2, 3, 3, 3]
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            frequency_array[c].append(n)


        res = []
        for i in range(len(frequency_array)-1, 0, -1):
            
            for n in frequency_array[i]:
                res.append(n)
                if len(res) == k:
                    return res

        print(frequency_array)
        

        #{1:1, 2:2, 3:3}

