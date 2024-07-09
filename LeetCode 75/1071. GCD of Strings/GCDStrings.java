
import java.util.Scanner;

class GCDStrings {

    public static String GCDofStrings(String s1, String s2) {
        int m = s1.length();
        int n = s2.length();
        for (int i = Math.min(m, n); i > 0; i--) {
            if (m % i == 0 && n % i == 0) {
                int base1 = m / i;
                int base2 = n / i;
                String ss1 = s1.substring(0,i);
                String ss2 = s2.substring(0,i);
                if (ss1.repeat(base2).equals(s2) && ss2.repeat(base1).equals(s1)) {
                    return s1.substring(0,i);
                }
            }
        }
        return "";
    }

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        String s1 = scn.next();
        String s2 = scn.next();
        System.out.println(GCDofStrings(s1, s2));
    }
}
