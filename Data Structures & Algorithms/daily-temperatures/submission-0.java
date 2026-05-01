
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Deque<Integer> stack = new ArrayDeque<>();
        int[] output = new int[temperatures.length];

        if (temperatures.length == 1) {
            output[0] = 0;
            return output;
        }


        stack.push(0);
        for (int i = 1; i < temperatures.length; i++) {
            
            while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]) {
                int index = stack.pop();
                output[index] = i - index;


            }
                stack.push(i);
        }    
            
            while (!stack.isEmpty()) {
                output[stack.pop()] = 0;
            }

            return output;
        }

        }

        
