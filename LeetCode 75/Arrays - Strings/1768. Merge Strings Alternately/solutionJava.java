// # problem link: https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
// # company tags: Uber
import java.util.Scanner;

class solutionJava {

    public static String mergeAlternately(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        String res = "";
        int i = 0;
        while (i < m && i < n) {
            res = res + word1.charAt(i);
            res = res + word2.charAt(i);
            i++;
        }
        if(m<n){
            String remaining = word2.substring(m, n);
            res += remaining;
        }
        else if(n<m){
            String remaining = word1.substring(n,m);
            res += remaining;
        }

        return res;
    }

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        String word1 = scn.next();
        String word2 = scn.next();
        System.out.println(mergeAlternately(word1, word2));
        scn.close();
    }
}
