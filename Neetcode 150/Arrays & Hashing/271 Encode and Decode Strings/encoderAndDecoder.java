
import java.util.ArrayList;
import java.util.List;

public class encoderAndDecoder {

    public static String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String s: strs){
            sb.append(s);
            sb.append("#*");
        }
        return sb.toString();
    }

    public static List<String> decode(String str) {
        int init = 0;
        ArrayList<String> res = new ArrayList<>();
        for(int i = 0; i< str.length(); i++){
            if(str.charAt(i) == '#' && str.charAt(i+1) == '*') {
                res.add(str.substring(init, i));
                if(i+1 == str.length()) {
                    break;
                }
                init = i+2;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        ArrayList<String> strs = new ArrayList<>();
        strs.add("neet");
        strs.add("code");
        strs.add("love");
        strs.add("you");
        
        String s = encode(strs);
        System.out.println(decode(s));
    }
}
