class KthLargest {
    PriorityQueue<Integer> maxHeap;
    int k;
    public KthLargest(int k, int[] nums) {
        this.maxHeap =  new PriorityQueue<>(Collections.reverseOrder());
        this.k = k;
        for (int i = 0; i < nums.length; i++) {
            maxHeap.add(nums[i]);
        }
    }
    
    public int add(int val) {
        int[] temp = new int[this.k - 1];

        this.maxHeap.add(val);

        // Must pop k -1 times
        for (int i = 0; i < this.k - 1; i++) {
            int toAddBack = this.maxHeap.poll();
            temp[i] = toAddBack;
        }
        int kthLargest = this.maxHeap.peek();


        for (int i = 0; i < this.k - 1; i++) {
            int toAddBack = temp[i];
            this.maxHeap.add(toAddBack);

        }


        return kthLargest;




        
    }
}
