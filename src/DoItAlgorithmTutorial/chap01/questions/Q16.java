package DoItAlgorithmTutorial.chap01.questions;

import java.util.Scanner;

public class Q16 {
    static void spira(int n){
        for(int line = 1; line<=n;line++){
            for(int blank = n-line;blank>=0;blank--){
                System.out.print(" ");
            }
            for(int star = 1; star <= line*2 -1; star++){
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public static void main(String[] args){
        Scanner stdIn = new Scanner(System.in);

        System.out.print("몇 단의 피라미드를 출력? : ");
        int n = stdIn.nextInt();

        spira(n);
    }
}
