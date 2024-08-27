
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class topKFrequentSolution {

    public static int[] topKFrequent(int[] nums, int k){
        // init hashmap
        HashMap<Integer, Integer> newMap = new HashMap<>();

        // filling hashmap
        for(int i: nums) {
            newMap.put(i, 1 + newMap.getOrDefault(i, 0));
        }
        
        // init freq array of empty arrays
        List<Integer>[] freq = new ArrayList[nums.length+1];
        System.out.println(freq);
        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        for(HashMap.Entry<Integer, Integer> entry : newMap.entrySet()) {
            int frequency = entry.getValue();
            freq[frequency].add(entry.getKey());
        }

        int[] res = new int[k];
        int idx = 0;
        for(int i = freq.length -1 ; i > 0; i--) {
            for(int j: freq[i]){
                res[idx] = j;
                idx++;
                if(idx == k){
                    return res;
                }
            }
        }      
        
        return new int[0];
}

    public static void main(String[] args) {
        int[] nums = {1,1,1,2,2,3};
        int k = 2;
        
        System.out.println(topKFrequent(nums, k));
    }
}
