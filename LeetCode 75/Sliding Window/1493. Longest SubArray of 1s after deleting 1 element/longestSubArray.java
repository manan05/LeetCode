
public class longestSubArray {

    public static int longestSubArraySolution(int[] nums) {
        int i = 0;
        int j = -1;
        int count = 0;
        int maxCount = 0;
        while (i < nums.length) {
            if (nums[i] == 1) {
                i++;
            } else {
                count++;
                i++;
            }

            while (count > 1) {
                j++;
                if (nums[j] == 0) {
                    count--;
                }
            }

            maxCount = Math.max(maxCount, (i - j - 1));
        }
        return (maxCount - 1);
    }

    public static void main(String[] args) {
        int[] nums = {0, 1, 1, 1, 0, 1, 1, 0, 1};
        System.out.println(longestSubArraySolution(nums));
    }
}
