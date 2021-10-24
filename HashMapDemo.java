import java.io.*;
import java.util.*;
 
class HashMapDemo {
 
    public static void main(String args[])
    {
        HashMap<Integer, String> hmIntStr = new HashMap<>();
 
        HashMap<String, String> hmStrStr = new HashMap<String, String>();
 
        hmIntStr.put(1, "first");
        hmIntStr.put(2, "second");
        hmIntStr.put(3, "last");
 
        hmStrStr.put("first", "one");
        hmStrStr.put("second", "two");
        hmStrStr.put("last", "three");
 
        System.out.println("HashMap hmIntStr are : "
                           + hmIntStr);
 
        System.out.println("HashMap hmStrStr are : "
                           + hmStrStr);
    }
}
