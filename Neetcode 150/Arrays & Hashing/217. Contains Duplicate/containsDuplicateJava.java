import java.util.Arrays;
import java.util.HashSet;

public class containsDuplicateJava {

    public static Boolean containsDuplicateONLogN(int[] arr) {
        Arrays.sort(arr);
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == arr[i + 1]) {
                return true;
            }
        }
        return false;
    }

    public static Boolean containsDuplicateON(int[] arr) {
        HashSet<Integer> myHashSet = new HashSet<>();
        for (int num: arr) {
            if(myHashSet.contains(num)){
                return true;
            }
            else{
                myHashSet.add(num);
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int[] arr = {1, 1, 1, 3, 3, 4, 3, 2, 4, 2};
        // System.out.println(containsDuplicateONLogN(arr));
        System.out.println(containsDuplicateON(arr));
    }

}
