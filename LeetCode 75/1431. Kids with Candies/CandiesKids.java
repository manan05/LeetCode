// Question Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

// Company: Amazon

import java.util.Arrays;
import java.util.Scanner;

public class CandiesKids {
    public static Boolean[] candiesKids(int[] candies, int extraCandies){
        int maxNum = maxArray(candies);
        Boolean[] res = new Boolean[candies.length];
        for(int i = 0; i< candies.length;i++){
            if(candies[i] + extraCandies >= maxNum){
                res[i] = true;
            }
            else{
                res[i] = false;
            }
        }
        return res;
    }

    public static int maxArray(int[] arr){
        int m = Integer.MIN_VALUE;
        for(int i = 0; i< arr.length; i++){
            if(arr[i]> m){
                m = arr[i];
            }
        }
        return m;
    }

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.println("Size of Candies array:");
        int n = scn.nextInt();
        int[] candies = new int[n];
        for(int i = 0; i<n ; i++){
            candies[i] = scn.nextInt();
        }
        System.out.println("ExtraCandies:");
        int extraCandies = scn.nextInt();
        System.out.println(Arrays.toString(candiesKids(candies, extraCandies)));
    }
}
