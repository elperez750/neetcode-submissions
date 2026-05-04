class Solution:
    def maxArea(self, heights: List[int]) -> int:
        forward_ptr = 0
        back_ptr = len(heights) - 1
        max_area = 0
        while forward_ptr < back_ptr:
            min_height = min(heights[forward_ptr], heights[back_ptr])
            area = (back_ptr - forward_ptr) * min_height
            if area > max_area:
                max_area = area

            if heights[back_ptr] == min_height:
                back_ptr -= 1
            
            else:
                forward_ptr += 1

        
        return max_area


            

