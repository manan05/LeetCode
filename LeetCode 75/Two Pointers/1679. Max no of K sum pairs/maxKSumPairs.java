
import java.util.Arrays;

// Question link : https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75
// Companies: Amazon

// O(N LogN) solution
public class maxKSumPairs {

    public static int solution(int[] nums, int k) {
        Arrays.sort(nums);
        int count = 0;
        int i = 0;
        int j = nums.length - 1;

        while (i < j) {
            int sum = nums[i] + nums[j];
            if ( sum == k) {
                count ++;
                i ++;
                j --;
            }
            else if(sum > k) {
                j --;
            }
            else {
                i ++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int[] nums = {3, 1, 3, 4, 3};
        var k = 6;
        System.out.println(solution(nums, k));
    }
}
