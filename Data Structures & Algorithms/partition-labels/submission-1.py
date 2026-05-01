class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = {}

        for i in range(len(s)-1, -1, -1):
            if s[i] not in last_occurence:
                last_occurence[s[i]] = i

        
        length = 1
        end = 0
        output = []

        for i in range(len(s)):
            
            if last_occurence[s[i]] > end:
                end = last_occurence[s[i]]
         
            if i == end:
                output.append(length)
                length = 1
            
            else:
                length += 1

        print(output)


        return output


       


        