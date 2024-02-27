

package com.mycompany.median;


import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Median {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>();
        
        while (scanner.hasNextInt()) {
            int d = scanner.nextInt();
            list.add(d);

            Collections.sort(list);
            
            int n1 = list.get(list.size() / 2);
            if (list.size() % 2 == 0) {
                int n2 = list.get(list.size() / 2 - 1);
                n1 = (n1 + n2) / 2;
            }
            
            System.out.println(n1);
        }
        
        scanner.close();
    }
}

