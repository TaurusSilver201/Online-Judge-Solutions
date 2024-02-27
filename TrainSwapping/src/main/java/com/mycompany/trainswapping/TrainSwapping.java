

package com.mycompany.trainswapping;

import java.util.Scanner;

public class TrainSwapping {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int tCase = scanner.nextInt();
        for (int k = 0; k < tCase; k++) {
            int count = 0;
            int n = scanner.nextInt();
            int[] train = new int[n];
            
            for (int i = 0; i < n; i++) {
                train[i] = scanner.nextInt();
            }
            
            for (int i = 0; i < n - 1; i++) {
                for (int j = 0; j < n - i - 1; j++) {
                    if (train[j] > train[j + 1]) {
                        count++;
                        int temp = train[j];
                        train[j] = train[j + 1];
                        train[j + 1] = temp;
                    }
                }
            }
            
            System.out.println("Optimal train swapping takes " + count + " swaps.");
        }
        
        scanner.close();
    }
}
