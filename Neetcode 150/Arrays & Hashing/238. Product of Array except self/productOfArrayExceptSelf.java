public class productOfArrayExceptSelf {

    public static int[] solution(int[] nums) {

        int n = nums.length;
        int[] res = new int[n];

        for(int i = 0; i<n ; i++) {
            res[i] = 1;
        }

        int pre = 1;
        for (int i =0 ;i < n; i++) {
            res[i] = res[i] * pre;
            pre = pre * nums[i];
        }

        int post = 1;
        for(int i = n-1; i>=0; i--) {
            res[i] = res[i] * post;
            post = post * nums[i];
        }

        return res;
    }

    public static void main(String[] args) {
        int[] nums = {1,2,3,4};
        
        System.out.println(solution(nums));
    }

}
