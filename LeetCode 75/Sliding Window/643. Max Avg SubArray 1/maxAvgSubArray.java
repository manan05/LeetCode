public class maxAvgSubArray {
    public static double maxAvgSubArraySol(int[] nums, int k) {
        int currSum = 0;
        for(int i=0; i<k; i++){
            currSum +=nums[i];
        }

        double maxSum = (double) currSum;
        int z = 1;
        for (int j = k; j < nums.length; j++) {
            currSum += nums[j] - nums[z-1];
            maxSum = Math.max(maxSum, (double)currSum);
            z ++;
        }
        return (double)(maxSum/k);
    }
    public static void main(String[] args) {
        int[] nums = {1, 12, -5, -6, 50, 3};
        int k = 4;
        System.out.println(maxAvgSubArraySol(nums, k));
    }
}
