class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0; i < nums.length; i++) {
            maxHeap.add(nums[i]);
        }

        for (int j = 0; j < k -1; j++) {
            maxHeap.poll();
        }


        return maxHeap.peek();
    }
}
