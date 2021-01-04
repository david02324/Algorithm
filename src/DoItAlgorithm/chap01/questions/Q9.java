package DoItAlgorithm.chap01.questions;

import java.util.Scanner;

public class Q9 {
    static int sumof(int a, int b){
        int lower , bigger;
        if(a<=b){
            lower = a;
            bigger = b;
        } else {
            lower = b;
            bigger = a;
        }

        int sum = 0;
        for(int i = lower; i <= bigger; i++){
            sum += i;
        }

        return sum;
    }

    public static void main(String[] args){
        Scanner stdIn = new Scanner(System.in);

        int a,b;
        System.out.println("a 부터 b 까지 더하기");
        System.out.print("a : ");
        a = stdIn.nextInt();
        System.out.print("b : ");
        b = stdIn.nextInt();

        System.out.println("합 : " + sumof(a,b));
    }
}
