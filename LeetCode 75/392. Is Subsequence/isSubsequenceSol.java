// Question link : https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75
// Companies name:  Amazon ✯   Bloomberg ✯   Facebook ✯   Microsoft ✯   Pinterest ✯   Zoho   Accolite   Tesco   PayTM   Quadrical AI   Google   Rootstock Software   Unthinkable Solutions   Josh Technologies   Yandex   Adobe

public class isSubsequenceSol {

    public static Boolean isSubsequence(String s, String t) {
        int i = 0;
        int j = 0;
        while (i < s.length() && j < t.length()) {
            if (s.charAt(i) == t.charAt(j)) {
                i++;
                j++;
            } else {
                j++;
            }
        }
        return i == s.length();
    }

    public static void main(String[] args) {
        String s = "abc";
        String t = "ahbgdc";
        System.out.println(isSubsequence(s, t));
    }
}
