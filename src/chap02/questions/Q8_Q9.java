package chap02.questions;

import java.util.Scanner;

public class Q8_Q9 {
    static int[][] mdays = {
            {31,28,31,30,31,30,31,31,30,31,30,31},
            {31,29,31,30,31,30,31,31,30,31,30,31}
    };

    static int isLeap(int year){
        return (year % 4 == 0 && year % 100 != 0 || year % 400 == 0) ? 1 : 0;
    }

    static int dayOfYear(int y, int m, int d){
        while(--m>0) d += mdays[isLeap(y)][m-1];
        return d;
    }

    static int leftDayOfYear(int y,int m,int d){
        return 365 + isLeap(y) - dayOfYear(y,m,d);
    }

    public static void main(String[] args){
        Scanner stdIn = new Scanner(System.in);
        int retry=0;

        do {
            System.out.print("년 : ");
            int year = stdIn.nextInt();
            System.out.print("월 : ");
            int month = stdIn.nextInt();
            System.out.print("일 : ");
            int day = stdIn.nextInt();

            System.out.printf("그 해 %d일째입니다", dayOfYear(year, month, day));
            System.out.printf("그 해 %d일 남았습니다", leftDayOfYear(year,month,day));
            System.out.print("한번더 -> 1 -> ");
            retry = stdIn.nextInt();
        } while(retry==1);
    }
}
