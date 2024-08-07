
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

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

    public static int oNSolution(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        int count = 0;
        for(int i = 0; i< nums.length; i++) {
            int res = k - nums[i];
            if(map.containsKey(res)) {
                count ++;
                if(map.get(res) == 1) {
                    map.remove(res);
                }
                else{
                    map.put(res, map.get(res) -1);
                }
            }
            else {
                map.put(nums[i], map.getOrDefault(nums[i], 0) +1);
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
