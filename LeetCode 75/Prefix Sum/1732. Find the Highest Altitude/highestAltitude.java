
public class highestAltitude {

    public static int highestAltitudeSolution(int[] gain) {
        int[] ans = new int[gain.length + 1];
        ans[0] = 0;
        ans[1] = gain[0];
        int max = Math.max(ans[0], ans[1]);
        for (int i = 1; i < gain.length; i++) {
            ans[i + 1] = gain[i] + ans[i];
            if (ans[i + 1] > max) {
                max = ans[i + 1];
            }
        }
        return max;
    }

    public static void main(String[] args) {
        int[] gain = {52,-91,72};
        System.out.println(highestAltitudeSolution(gain));
    }

}
