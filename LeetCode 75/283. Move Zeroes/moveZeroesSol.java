// # Question Link:https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

// # Company:  Facebook ✯   Microsoft ✯   Apple ✯   Amazon ✯   Yandex ✯   Bloomberg   tcs   Uber   Adobe   IBM   Expedia   tiktok  


public class moveZeroesSol {

    public static void moveZeroes(int[] arr) {
        int i = 0;
        int j = 1;

        while (j < arr.length) {
            if (arr[i] == 0) {
                if (arr[j] != 0) {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;

                    i++;
                    j++;
                }
                else{
                    j++;
                }
            }
            else{
                i++;
                j++;
            }
        }
        for (int k: arr){
            System.out.println(k + ",");
        }
    }

    public static void main(String[] args) {
        int[] arr = {0, 1, 0, 3, 12};
        moveZeroes(arr);
    }
}
