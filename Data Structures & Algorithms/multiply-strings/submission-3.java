class Solution {
    public String multiply(String num1, String num2) {

        if (num1.equals("0") || num2.equals("0")) {
            return "0";
        }
        
        int[] result = new int[num1.length() + num2.length()];
        StringBuilder sb  = new StringBuilder();


        for (int i = (num1.length() - 1); i >= 0; i--) {
            
            for (int j = (num2.length() - 1); j>= 0; j--) {
                int mult = (num1.charAt(i) - '0') * (num2.charAt(j) - '0');
                result[i+j+1] += mult % 10;
                result[i+j] += mult / 10;

            }
            
    
        }

        for (int i = result.length - 1; i > 0; i--) {
            result[i - 1] += result[i] / 10;
            result[i] %= 10;
        }
       

        int startingIdx = findIndex(result);
        for (int i = startingIdx; i < result.length; i++) {
            sb.append(result[i]);
        }

        return sb.toString();
    }



    int findIndex(int[] array) {
        int i = 0;
        while (array[i] == 0) {
            i += 1;
        }

        return i;
    }



    
}
