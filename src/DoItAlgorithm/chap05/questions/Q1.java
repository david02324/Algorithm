package DoItAlgorithm.chap05.questions;

public class Q1 {
    static int Factorial(int n){
        int answer = 1;
        for(; n > 0; n--)
            answer *= n;
        return answer;
    }

    public static void main(String[] args){
        for(int i = 0; i < 10; i++)
            System.out.println(i+"! = "+Factorial(i));
    }
}
