import java.util.*;
import java.lang.*;
import java.io.*;

public class missingnum {
	public static void main (String[] args) {
		Scanner scan = new Scanner(System.in);
		int t = scan.nextInt();
		while (t--> 0) {
		    int n = scan.nextInt();
		    int[] arr = new int[n - 1];
		    int sum = 0;
		    for (int i = 0; i < n - 1; i++) {
		        arr[i] = scan.nextInt();
		        sum += arr[i];
		    }
		    int firstNum = arr[0];
		    int lastNum = arr[n - 2];
		    int actualSum = 0;
		    for (int j = 1; j <= n; j++) {
		        actualSum += j;
		    }
		    System.out.println(actualSum - sum);
		}
	}
}
