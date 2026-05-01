class Solution:

    def encode(self, strs: List[str]) -> str:
        result_string = ""
       
        for string in strs:
            result_string += str(len(string)) + "#" + string
            print('result string')
        print(result_string)
        return result_string
            
      
     



    def decode(self, s: str) -> List[str]:
        res = []
        
        current = 0


        


        while current < len(s): 
            delimiter_index = s.find("#", current)
            count = int(s[current:delimiter_index])


            current = delimiter_index + 1
            res.append(s[current:current+count])


            current += count


        return res
            



