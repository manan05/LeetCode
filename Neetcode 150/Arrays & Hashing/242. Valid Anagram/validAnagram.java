
import java.util.HashMap;

public class validAnagram {

    public static Boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> newMap = new HashMap<>();

        for (char ch : s.toCharArray()) {
            if (!newMap.containsKey(ch)) {
                newMap.put(ch, 1);
            } else {
                newMap.put(ch, (newMap.get(ch) + 1));
            }
        }
        for (char ch : t.toCharArray()) {
            if (!newMap.containsKey(ch)) {
                return false;
            }
            else{
                newMap.put(ch, (newMap.get(ch) - 1));
                if(newMap.get(ch) <0){
                    return false;
                }
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
