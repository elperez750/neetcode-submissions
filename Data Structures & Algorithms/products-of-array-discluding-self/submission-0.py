class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = []
        postfix_product = []


        output = []

        total_prefix = 1
        total_postfix = 1


        for num in nums:
            total_prefix *= num

            prefix_product.append(total_prefix)


        for num in reversed(nums):

            total_postfix *= num
            postfix_product.append(total_postfix)

        
        postfix_product = postfix_product[::-1]


        print(postfix_product)

        for i in range(len(nums)):

            prefix_pointer = i - 1
            postfix_pointer = i + 1


            if prefix_pointer == -1:
                product = 1 * postfix_product[postfix_pointer]
            
            elif postfix_pointer == len(nums):
                product = prefix_product[prefix_pointer] * 1

            else:
                product = prefix_product[prefix_pointer] * postfix_product[postfix_pointer]


            output.append(product)


        return output




        

        


