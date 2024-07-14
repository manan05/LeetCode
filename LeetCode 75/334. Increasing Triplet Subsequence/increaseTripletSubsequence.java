
import java.util.Scanner;

public class increaseTripletSubsequence {
    public static Boolean solution(int[] arr){
        int first = Integer.MAX_VALUE;
        int second = Integer.MAX_VALUE;

        int fIdx = -1;
        int sIdx = -1;

        for(int i = 0; i< arr.length; i++){
            if(arr[i] <= first && i > fIdx){
                first = arr[i];
                fIdx = i;
            }
            else if (arr[i] <= second && i > sIdx) {
                second = arr[i];
                sIdx = i;
            }
            else{
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.println("Size of arr:");
        int n = scn.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i < n;i++){
            arr[i] = scn.nextInt();
        }

        System.out.println(solution(arr));
    }
}
