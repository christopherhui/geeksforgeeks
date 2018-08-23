import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    public static boolean palindrome(String str) {
        if (str.length() <= 1) {
            return true;
        }
        else {
            return str.charAt(0) == str.charAt(str.length()-1)
            && palindrome(str.substring(1, str.length()-1));
        }
    }
    
	public static void main (String[] args) {
		Scanner scan = new Scanner(System.in);
		int t = scan.nextInt();
		while (t--> 0) {
		    int n = scan.nextInt();
		    scan.nextLine();
		    String str = scan.nextLine();
		    if (palindrome(str)) {
		        System.out.println("Yes");
		    }
		    else {
		        System.out.println("No");
		    }
		}
	}
}
