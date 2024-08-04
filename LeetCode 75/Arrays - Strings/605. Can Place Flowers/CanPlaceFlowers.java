// Question Link: https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

// Companies:  LinkedIn ✯   Facebook ✯   Amazon ✯   Bloomberg ✯   Yahoo ✯  
import java.util.Scanner;

public class CanPlaceFlowers {

    public static boolean CanPlaceFlowers(int[] arr, int n){
        int m = arr.length;
        int res = 0;
        for(int i =0;i<m;i++){
            if(arr[i] == 0){
                if(m == 1){
                    res++;
                }
                else if(i == 0){
                    if(arr[i+1] == 0){
                        arr[i] = 1;
                        res ++;
                    }
                }
                else if(i == m-1){
                    if(arr[i-1] == 0){
                        arr[i] = 1;
                        res ++;
                    }
                }
                else{
                    if(arr[i+1] == 0 && arr[i -1] == 0){
                        arr[i] = 1;
                        res++;
                    }
                }
            }
        }
        if(res >= n){
            return true;
        }
        else{
            return false;
        }
    }

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.println("Size of flowerbed:");
        int n = scn.nextInt();
        int[] flowerbed = new int[n];
        for(int i = 0; i<n; i++){
            flowerbed[i] = scn.nextInt();
        }
        System.out.println("Extra Flowers?");
        int z = scn.nextInt();
        scn.close();
        System.out.println(CanPlaceFlowers(flowerbed, z));
    }
}
