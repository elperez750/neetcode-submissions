class MaxHeap {
    int[] maxHeap;
    int capacity;
    int size;


    public MaxHeap(int capacity, int[] stones) {
        this.capacity = capacity;

        // Array of 0s
        this.maxHeap = new int[capacity];
        this.size = 0;
        
        for (int i = 0; i < stones.length; i++) {
            
            addElement(stones[i]);
            
        }
    }

     public void addElement(int stone) {

        int stoneIdx = this.size;
        int parentIdx = ((stoneIdx - 1) / 2);
        this.maxHeap[stoneIdx] = stone;


        
        while (this.maxHeap[stoneIdx] > this.maxHeap[parentIdx]) {
            int temp = this.maxHeap[stoneIdx];
            this.maxHeap[stoneIdx] = this.maxHeap[parentIdx];
            this.maxHeap[parentIdx] = temp;

            stoneIdx = parentIdx;
            parentIdx = ((stoneIdx - 1) / 2);
            
        }

        this.size += 1;
        
    }

    public int popElement() {
        int i = 0;
        int elementToReturn = this.maxHeap[i];
        this.maxHeap[i] =  this.maxHeap[this.size - 1];
        int parent = maxHeap[i];
        this.maxHeap[this.size - 1] = 0;
     
        int leftChild;
        int rightChild;

         if (((2 * i) + 1) < this.size) {
            leftChild = maxHeap[(2 * i) + 1];

        }
        else{
            leftChild = Integer.MIN_VALUE;

        }
        if (((2 * i) + 2) < this.size) {
             rightChild = maxHeap[(2 * i) + 2];

        }
        else{
            rightChild = Integer.MIN_VALUE;
        }
        
      


        this.size -= 1;


        while((2 * i + 1 < this.size) && ((parent < leftChild) || (parent < rightChild))) {
            
            int max;
            int maxIdx;
            if (leftChild >= rightChild) {
                max = leftChild;
                maxIdx = (2 * i) + 1;
            }
            else {
                max = rightChild;
                maxIdx = (2 * i) + 2;
            }

            int temp = this.maxHeap[i];
            this.maxHeap[i] = max;
            this.maxHeap[maxIdx] = temp;

            i = maxIdx;
            parent = maxHeap[i];
            if (((2 * i) + 1) < this.size) {
                leftChild = maxHeap[(2 * i) + 1];

            }
            else{
                leftChild = Integer.MIN_VALUE;

            }
            if (((2 * i) + 2) < this.size) {
                rightChild = maxHeap[(2 * i) + 2];

            }
            else{
                rightChild = Integer.MIN_VALUE;

            }
                
        
        }   
       

        return elementToReturn;


    }


    }







class Solution {
    public int lastStoneWeight(int[] stones) {
        MaxHeap mx = new MaxHeap(stones.length, stones);

        while (mx.size > 1) {
            int elementOne = mx.popElement();
            int elementTwo = mx.popElement();

            if (elementOne > elementTwo) {
                
                elementOne -= elementTwo;
                mx.addElement(elementOne);

            }
                
        }


        return mx.maxHeap[0];
    }
}
