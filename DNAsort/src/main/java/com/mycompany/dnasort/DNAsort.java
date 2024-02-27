
package com.mycompany.dnasort;

import java.util.Scanner;
import java.util.Arrays;

public class DNAsort {
    static class Order {
        int pos;
        int inversion;
        
        Order(int pos, int inversion) {
            this.pos = pos;
            this.inversion = inversion;
        }
    }
    
    static int getInversion(String str) {
        int inv = 0;
        for (int i = 0; i < str.length(); i++) {
            for (int j = i + 1; j < str.length(); j++) {
                if (str.charAt(i) > str.charAt(j)) {
                    inv++;
                }
            }
        }
        return inv;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int test = scanner.nextInt();
        while (test-- > 0) {
            int len = scanner.nextInt();
            int n = scanner.nextInt();
            scanner.nextLine(); // Consume newline
            
            String[] s = new String[n];
            Order[] lis = new Order[n];
            
            for (int i = 0; i < n; i++) {
                s[i] = scanner.nextLine();
                lis[i] = new Order(i, getInversion(s[i]));
            }
            
            Arrays.sort(lis, (a, b) -> Integer.compare(a.inversion, b.inversion));
            
            for (int i = 0; i < n; i++) {
                System.out.println(s[lis[i].pos]);
            }
            
            if (test > 0) {
                System.out.println();
            }
        }
        
        scanner.close();
    }
}
