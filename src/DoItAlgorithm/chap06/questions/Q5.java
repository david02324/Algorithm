package DoItAlgorithm.chap06.questions;

import java.util.Scanner;

public class Q5 {
    static void swap(int[] a,int idx1,int idx2){
        int t = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = t;
    }

    static int bubbleSort(int[] a,int n){
        int lastLeft = 0;
        int lastRight = n - 1;
        int passCount = 0;
        int tempL,tempR;
        while(lastLeft < lastRight){
            if(++passCount % 2 == 0){
                tempR = 0;
                for(int j = lastLeft;j<lastRight;j++){
                    if(a[j+1] < a[j]) {
                        swap(a, j + 1, j);
                        tempR = j;
                    }
                }
                lastRight = tempR;
            } else{
                tempL = n - 1;
                for(int j = lastRight;j>lastLeft;j--){
                    if(a[j] < a[j-1]){
                        swap(a,j-1,j);
                        tempL = j;
                    }
                }
                lastLeft = tempL;
            }
        }
        return passCount;
    }

    public static void main(String[] args){
        Scanner stdIn = new Scanner(System.in);

        System.out.println("버블 정렬");
        System.out.print("요솟수 : ");
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for(int i = 0; i < nx; i++){
            System.out.print("x[" + i + "] : ");
            x[i] = stdIn.nextInt();
        }
        
        System.out.println("오름차순으로 정렬했습니다. 패스 수 : " + bubbleSort(x,nx));
        for(int i = 0;i < nx;i++)
            System.out.println("x[" + i + "]=" + x[i]);
    }
}
