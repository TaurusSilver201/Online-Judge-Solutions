/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.blindsort;

import java.util.Scanner;

public class BlindSort {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (scanner.hasNextLong()) {
            long n = scanner.nextLong();
            int result = (int) (n - 1 + Math.log(n - 1) / Math.log(2));
            System.out.println(result);
        }
        
        scanner.close();
    }
}
