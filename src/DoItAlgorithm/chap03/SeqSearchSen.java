package DoItAlgorithm.chap03;

import java.util.Scanner;

// 보초법(sentinel method)는 배열 마지막 요소에 키 값을 일부러 넣어서
// 종료 조건을 매번 검사하는 일을 생략
public class SeqSearchSen {
    static int seqSearchSen(int a[],int n,int key){
        int i = 0;

        a[n] = key;

        while(true){
            if(a[i]==key)
                break;
            i++;
        }

        return i == n ? -1 : i;
    }

    public static void main(String[] args){
        Scanner stdIn = new Scanner(System.in);

        System.out.print("요솟수 : ");
        int num = stdIn.nextInt();
        int[] x = new int[num+1];

        for(int i = 0; i<num; i++){
            System.out.print("x[" + i + "] : ");
            x[i] = stdIn.nextInt();
        }

        System.out.print("검색할 값 : ");
        int ky = stdIn.nextInt();

        int idx = seqSearchSen(x,num,ky);
        if(idx == -1)
            System.out.println("찾는 값이 없습니다");
        else
            System.out.println(ky + "는 x[" + idx + "] 의 값입니다");
    }
}
