package DoItAlgorithmTutorial.chap01.questions;

import java.util.Scanner;

public class Q15 {
    static void triangleRU(int n){
        for(int line = 1; line<=n; line++){
            for(int i = 1; i <=line-1; i++){
                System.out.print(" ");
            }
            for(int i = 1; i<=n-line+1; i++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public static void main(String[] args){
        Scanner stdIn = new Scanner(System.in);
        System.out.print("숫자 입력 : ");

        int n = stdIn.nextInt();
        triangleRU(n);
    }
}
