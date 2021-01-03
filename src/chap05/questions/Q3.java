package chap05.questions;

public class Q3 {
    static int gcd(int x, int y){
        if(y==0)
            return x;
        else
            return gcd(y,x%y);
    }

    static int gcdArray(int[] a,int firstIndex,int len) {
       if(len == 1)
           return a[firstIndex];
       else if (len == 2)
           return gcd(a[firstIndex],a[firstIndex+1]);
       else
           return gcd(a[firstIndex],gcdArray(a,firstIndex+1,len-1));
    }

    public static void main(String[] args){
        int[] a = {600,24,18,60};
        System.out.println(gcdArray(a,0,4));
    }
}
