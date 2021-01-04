package DoItAlgorithmTutorial.chap03;

import java.util.Scanner;

// 이진 검색(Binary Search)은 검색 시마다 다음 범위의 중간으로 이동하여 검색
// 이미 정렬된 배열이 존재해야
public class BinSearch {
    static int binSearch(int [] a,int n,int key) {
        int pl = 0;
        int pr = n - 1;

        do {
            int pc = (pl + pr) / 2;
            if (a[pc] == key)
                return pc;
            else if (a[pc] < key)
                pl = pc + 1;
            else
                pr = pc - 1;
        } while (pl <= pr);

        return -1;
    }

    public static void main(String[] args){
        Scanner stdIn = new Scanner(System.in);

        System.out.print("요솟수 : ");
        int num = stdIn.nextInt();
        int x[] = new int[num];

        System.out.println("오름차순으로 입력하세요");

        System.out.print("x[0]:");
        x[0] = stdIn.nextInt();

        for (int i = 1; i < num; i++){
            do{
                System.out.print("x[" + i + "]:");
                x[i] = stdIn.nextInt();
            } while(x[i] < x[i-1]);
        }

        System.out.print("검색할 값 : ");
        int ky = stdIn.nextInt();

        int idx = binSearch(x,num,ky);

        if(idx == -1)
            System.out.println("찾는 값이 없습니다");
        else
            System.out.println(ky + "는 x[" + idx + "] 의 값입니다");
    }
}
