
public class maxVowelsSS {

    public static int maxVowelsSSSolution(String s, int k) {
        StringBuilder sb = new StringBuilder(s);
        int j = k - 1;
        int maxCount;
        int count = 0;

        for (int z = 0; z < j+1; z++) {
            if (sb.charAt(z) == 'a' || sb.charAt(z) == 'e' || sb.charAt(z) == 'i' || sb.charAt(z) == 'o' || sb.charAt(z) == 'u') {
                count++;
            }
        }
        maxCount = count;

        int i = 1;
        j = k;
        
        while (j < sb.length()) { 
            if (sb.charAt(i-1) == 'a' || sb.charAt(i-1) == 'e' || sb.charAt(i-1) == 'i' || sb.charAt(i-1) == 'o' || sb.charAt(i-1) == 'u'){
                count = count - 1;
            }
            if (sb.charAt(j) == 'a' || sb.charAt(j) == 'e' || sb.charAt(j) == 'i' || sb.charAt(j) == 'o' || sb.charAt(j) == 'u'){
                count = count  + 1;
            }
            maxCount = Math.max(maxCount, count);
            System.out.println("maxCount now" + maxCount);
            i ++;
            j ++;
        }
        return maxCount;
    }

    public static void main(String[] args) {
        String s = "abciiidef";
        int k = 3;
        System.out.println(maxVowelsSSSolution(s, k));
    }
}
