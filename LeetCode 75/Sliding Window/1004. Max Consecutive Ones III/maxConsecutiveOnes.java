
public class maxConsecutiveOnes {

    public static int maxConsecutiveOnesSolution(int[] nums, int k) {
        int i = 0;
        int j = -1;
        int zeroCount = 0;
        int maxSize = 0;

        while (i < nums.length) {
            if (nums[i] == 0) {
                i++;
                zeroCount++;
            }
            else{
                i ++;
            }

            while(zeroCount > k) {
                j ++;
                if(nums[j] == 0){
                    zeroCount --;
                }
            }

            maxSize = Math.max((i-j-1), maxSize);
        }
        return maxSize;
    }

    public static void main(String[] args) {
        int[] nums = {0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1};
        int k = 3;

        System.out.println(maxConsecutiveOnesSolution(nums, k));
    }
}
