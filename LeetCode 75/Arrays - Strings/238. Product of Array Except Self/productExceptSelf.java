// Question link: https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

// Company: Amazon, Facebook, Microsoft, Asana, Apple, Uber, Adobe, Bloomberg, Oracle
// must write an algo that runs O(n) without division operation

import java.util.Arrays;
import java.util.Scanner;

public class productExceptSelf {
    public static int[] productExceptSelfSol(int[] arr){
        int n = arr.length;
        int[] res = new int[n];
        Arrays.fill(res, 1);

        int pre = 1;
        for(int i = 0; i< n; i++){
            res[i] *= pre;
            pre *= arr[i];
        }

        int post = 1;
        for(int i = n-1; i>=0; i --){
            res[i] *= post;
            post *= arr[i];
        }

        return res;
    }

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i<n ; i++){
            arr[i] = scn.nextInt();
        }
        
        System.out.println(productExceptSelfSol(arr));
    }
}
