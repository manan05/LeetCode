
public class pivotIndex {

    public static int findPivotIndex(int[] nums) {
        int[] lsum = new int[nums.length];
        lsum[0] = 0;
        int sum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            sum += nums[i];
            lsum[i] = lsum[i - 1] + nums[i - 1];
        }

        for (int i = 0; i < nums.length; i++) {
            int left = lsum[i];
            int right = sum - left - nums[i];

            if(left == right) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] nums = {1, 7, 3, 6, 5, 6};
        System.out.println(findPivotIndex(nums));
    }
}
