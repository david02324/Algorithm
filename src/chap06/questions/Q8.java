package chap06.questions;

import java.util.Scanner;

public class Q8 {
    static void BinaryInsertionSort(int[] a, int n){
        a[0] = -50000;
        for(int i = 1; i<n; i++){
            int tmp = a[i];
            int pl = 1;
            int pr = i;
            int target = -1;
            do{
                int pc = (pl + pr) / 2;
                if(a[pc] == tmp){
                    target = pc+1;
                    break;
                } else if (a[pc] < tmp){
                    pl = pc + 1;
                } else {
                    pr = pc - 1;
                }
            } while(pl <= pr);

            if(target==-1){
                target = pl;
            }

            for(int j = i;j>target;j--){
                a[j] = a[j-1];
            }
            a[target] = tmp;
        }
    }

    public static void main(String[] args){
        Scanner stdIn = new Scanner(System.in);
        System.out.println("단순 삽입 정렬(1번 인덱스부터 데이터 저장)");
        System.out.print("요솟수 : ");
        int nx = stdIn.nextInt() + 1;
        int[] x = new int[nx];

        for(int i = 1; i < nx; i++){
            System.out.print("x[" + i + "]:");
            x[i] = stdIn.nextInt();
        }

        BinaryInsertionSort(x,nx);

        System.out.println("오름차순으로 정렬했습니다");
        for(int i = 1; i < nx; i++)
            System.out.println("x[" + i + "]=" + x[i]);
    }
}
