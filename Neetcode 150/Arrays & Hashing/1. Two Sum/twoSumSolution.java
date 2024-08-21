// Question link: https://leetcode.com/problems/two-sum/
// Companies:  Amazon ✯   Adobe ✯   Google ✯   Apple ✯   Microsoft ✯   Facebook   Bloomberg   Uber   Spotify   Goldman Sachs   Expedia   Oracle   Yahoo   Zoho   Visa   Morgan Stanley   IBM   Paypal   JPMorgan   Walmart Global Tech   Intel   Salesforce   Dell   American Express   Accenture   Samsung   Intuit   Zillow   Zoom   Zomato  

import java.util.HashMap;

public class twoSumSolution {

    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> newMap = new HashMap<>();

        // Building the HashMap
        for(int i = 0 ; i< nums.length; i ++) {
            newMap.put(nums[i], i);
        }

        for(int j = 0; j< nums.length; j++) {
            int diff = target - nums[j];
            if(newMap.containsKey(diff) && j != newMap.get(diff)){
                return new int[] {j, newMap.get(diff)};
            }
        }
        return new int[] {};
    }

    public static void main(String[] args) {
        int[] nums = {2,7,11,15};
        int target = 9;
        System.out.println(twoSum(nums, target));
    }
}
