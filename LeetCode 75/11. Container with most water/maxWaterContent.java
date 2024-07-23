// Question Link: https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75
// Companies:  Amazon ✯   Microsoft ✯   Adobe ✯   Facebook ✯   Google ✯   Apple   Bloomberg   Swiggy   Goldman Sachs  

public class maxWaterContent {

    public static int maxArea(int[] arr) {
        int i = 0;
        int j = arr.length - 1;
        int myMaxArea = 0;

        while (i < j) {
            int newArea = Math.abs((j - i) * Math.min(arr[i], arr[j]));
            if (newArea > myMaxArea) {
                myMaxArea = newArea;
            }
            if(arr[i] > arr[j]){
                j --;
            }
            else{
                i++;
            }
        }
        return myMaxArea;
    }

    public static void main(String[] args) {
        int[] arr = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        System.out.println(maxArea(arr));
    }
}
