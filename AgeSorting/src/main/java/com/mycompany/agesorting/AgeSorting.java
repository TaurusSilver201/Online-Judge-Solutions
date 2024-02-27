
package com.mycompany.agesorting;

import java.util.Scanner;

public class AgeSorting {
    public static final int MAX_AGE = 100;
    public static final int MIN_AGE = 1;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            int N = scanner.nextInt();
            if (N == 0) break;
            
            int[] ageCount = new int[MAX_AGE + 1];
            
            for (int i = 0; i < N; ++i) {
                int age = scanner.nextInt();
                ageCount[age]++;
            }
            
            StringBuilder result = new StringBuilder();
            String sep = "";
            for (int i = MIN_AGE; i <= MAX_AGE; ++i) {
                while (ageCount[i] > 0) {
                    result.append(sep).append(i);
                    sep = " ";
                    ageCount[i]--;
                }
            }
            
            System.out.println(result.toString());
        }
        
        scanner.close();
    }
}
