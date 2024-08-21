
import java.util.HashMap;
import java.util.Map;

public class validAnagram {

    public static Boolean isAnagram(String s, String t) {
        Map<Character, Integer> newMap = new HashMap<>();

        for (char ch : s.toCharArray()) {
            if (!newMap.containsKey(ch)) {
                newMap.put(ch, 1);
            } else {
                newMap.put(ch, (newMap.get(ch) + 1));
            }
        }

        // System.out.println(newMap.keySet() +""+ newMap.values());
        for (char ch : t.toCharArray()) {
            if (!newMap.containsKey(ch)) {
                return false;
            }
            else{
                newMap.put(ch, (newMap.get(ch) - 1));
            }
        }

        for(int j: newMap.values()){
            if(j != 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        String s = "anagram";
        String t = "nagaram";
        System.out.println(isAnagram(s, t));
    }
}
