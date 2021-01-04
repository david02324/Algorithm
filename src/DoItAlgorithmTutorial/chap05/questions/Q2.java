package DoItAlgorithmTutorial.chap05.questions;

public class Q2 {
    static int gcd(int a,int b){
        int gcd = 1;
        int smaller;
        if(a>b)
            smaller = b;
        else
            smaller = a;
        for(int i = 2;i<=smaller;i++){
            if(a%i == 0)
                if(b%i == 0)
                    gcd = i;
        }
        return gcd;
    }

    public static void main(String[] args){
        System.out.println(gcd(12,27));
    }
}