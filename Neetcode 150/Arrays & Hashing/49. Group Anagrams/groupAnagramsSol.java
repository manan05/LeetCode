
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class groupAnagramsSol {

    public static List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> newMap = new HashMap<>();

        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String sortedChars = new String(chars);
            if(!newMap.containsKey(sortedChars)){
                newMap.put(sortedChars, new ArrayList<>());
            }
            newMap.get(sortedChars).add(s);
        }

        return new ArrayList<>(newMap.values());
    }

    public static void main(String[] args) {
        String[] strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
        System.out.println(groupAnagrams(strs));
    }
}
