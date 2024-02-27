

package com.mycompany.flipsort;
import java.util.Scanner;
/**
 *
 * @author PC
 */
public class FlipSort {

   public static int bubbleSort(int n, int[] arr) {
        int m = 0;
        
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap arr[j] and arr[j+1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    m++;
                }
            }
        }
        
        return m;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (scanner.hasNext()) {
            int n = scanner.nextInt();
            int[] arr = new int[n];
            
            for (int i = 0; i < n; i++) {
                arr[i] = scanner.nextInt();
            }
            
            int res = bubbleSort(n, arr);
            System.out.println("Minimum exchange operations : " + res);
        }
        
        scanner.close();
    }
}
