
import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		Scanner scan = new Scanner(System.in);
		int t = scan.nextInt();
		while (t--> 0) {
		    int n = scan.nextInt();
		    int[] arr = new int[n];
		    for (int i = 0; i < n; i++) {
		        arr[i] = scan.nextInt();
		    }
		    int max = 0;
		    int secondMax = 0;
		    for (int j = 0; j < n; j++) {
		        if (arr[j] > max) {
		            secondMax = max;
		            max = arr[j];
		        }
		        else if (arr[j] > secondMax) {
		            secondMax = arr[j];
		        }
		    }
		    System.out.println(secondMax);
		}
	}
}
