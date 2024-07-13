
import java.util.Scanner;


public class reverseWordsString {
    public static String reverseWords(String s){
        s = s.strip();
        StringBuilder sb = new StringBuilder();
        String[] arr = s.split(" ");
        for(int i = arr.length -1; i >= 0; i--){
            if(arr[i] != ""){
                sb.append(arr[i]);
                sb.append(" ");
            }
        }
        return sb.toString().strip();
    }

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        String s = scn.nextLine();
        System.out.println(reverseWords(s));
        scn.close();
    }
}
