
import java.util.Scanner;

public class stringCompression {

    public static int stringCompressionSol(char[] chars) {
        StringBuilder sb = new StringBuilder();

        int count = 1;
        int i = 1;

        sb.append(chars[0]);
        while (i < chars.length) {
            if (chars[i - 1] == chars[i]) {
                count++;
                i++;
            } else {
                if (count > 1) {
                    sb.append(count);
                }
                sb.append(chars[i]);
                count = 1;
                i++;
            }
        }
        if(count >1){
            sb.append(count);
        }

        for(int j = 0; j< sb.length(); j++){
            chars[j] = sb.charAt(j);
        }
        return sb.length();
    }

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.println("Size of char array");
        int n = scn.nextInt();
        char[] chars = new char[n];
        for (int i = 0; i < n; i++) {
            chars[i] = scn.next().charAt(0);
        }
        System.out.println(stringCompressionSol(chars));
    }

}
