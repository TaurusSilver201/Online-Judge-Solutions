
package com.mycompany.meta_loopless;
import java.util.Scanner;

public class Meta_Loopless {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int tc = scanner.nextInt();
        
        while (tc-- > 0) {
            int n = scanner.nextInt();
            System.out.println("program sort(input,output);\nvar");
            
            for (int i = 0; i < n - 1; ++i)
                System.out.print((char)('a' + i) + ",");
            
            System.out.println((char)('a' + n - 1) + " : integer;\nbegin\n  readln(");
            
            backtrack(1, "a", n);
            
            System.out.println("end.");
            
            if (tc > 0)
                System.out.println();
        }
        
        scanner.close();
    }

    static void backtrack(int idx, String str, int n) {
        if (idx == n) {
            System.out.printf("%swriteln(", repeatString(idx * 2, ' '));

            for (int i = 0; i < idx - 1; ++i)
                System.out.printf("%c,", str.charAt(i));

            System.out.printf("%c)\n", str.charAt(idx - 1));

            return;
        }

        String tmpStr;

        for (int i = idx - 1; i >= 0; --i) {
            System.out.print(repeatString(idx * 2, ' '));

            if (i != idx - 1)
                System.out.print("else ");
            
            System.out.printf("if %c < %c then\n", str.charAt(i), (char)('a' + idx));

            tmpStr = str;

            if (i + 1 > idx - 1)
                tmpStr += (char)('a' + idx);
            else
                tmpStr = tmpStr.substring(0, i + 1) + (char)('a' + idx) + tmpStr.substring(i + 1);

            backtrack(idx + 1, tmpStr, n);
        }

        System.out.print(repeatString(idx * 2, ' '));
        System.out.println("else");
        backtrack(idx + 1, (char)('a' + idx) + str, n);
    }

    static String repeatString(int n, char c) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(c);
        }
        return sb.toString();
    }
}


