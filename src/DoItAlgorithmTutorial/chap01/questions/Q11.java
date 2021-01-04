package DoItAlgorithmTutorial.chap01.questions;

import java.util.Scanner;

public class Q11 {
    static int getN(int number){
        int N = 0;
        int num = number;

        do{
            num /= 10;
            N++;
        } while(num!=0);

        return N;
    }

    public static void main(String[] args){
        Scanner stdIn = new Scanner(System.in);

        System.out.print("N을 입력하세요 : ");
        int number = stdIn.nextInt();

        System.out.println("입력한 수는 " + getN(number) + "자리수입니다");
    }
}
