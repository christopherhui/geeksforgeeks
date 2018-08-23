
import java.util.*;
import java.lang.*;
import java.io.*;

public class removespaces {
    public static void main (String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        scan.nextLine();
        while (t--> 0) {
            String[] str = scan.nextLine().split(" ");
            for (String i: str) {
                System.out.print(i);
            }
            System.out.println();
        }
    }
}