
package com.mycompany.blackbook;

import java.util.Scanner;
import java.util.TreeMap;

public class BlackBook {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        TreeMap<String, String> listNames = new TreeMap<>();
        
        int departments = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        for (int i = 0; i < departments; i++) {
            String department = scanner.nextLine();
            String data;
            while (!(data = scanner.nextLine()).isEmpty()) {
                int lastNameIdx = data.indexOf(',');
                String lastName = data.substring(0, lastNameIdx);
                String newData = department + data.substring(lastNameIdx);
                listNames.put(lastName, newData);
            }
        }
        
        for (String data : listNames.values()) {
            System.out.println("----------------------------------------");
            String[] fields = data.split(",");
            System.out.println(fields[0] + " " + fields[1] + " " + fields[2]);
            System.out.println("Department: " + fields[3]);
            System.out.println("Home Phone: " + fields[4]);
            System.out.println("Work Phone: " + fields[5]);
            System.out.println("Campus Box: " + fields[6]);
        }
        
        scanner.close();
    }
}

