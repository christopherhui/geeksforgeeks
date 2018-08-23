import java.util.*;
import java.lang.*;
import java.io.*;

public class arrayreverse {
    public static void main (String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        for (int i = 0; i < t; i++) {
            int n = scan.nextInt();
            int[] arr = new int[n];
            for (int j = 0; j < n; j++) {
                arr[j] = scan.nextInt();
            }
            for (int x = arr.length - 1; x >= 0; x-- ) {
                System.out.print(arr[x] + " ");
            }
            System.out.println();
        }
    }
}