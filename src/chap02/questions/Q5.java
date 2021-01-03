package chap02.questions;

public class Q5 {
    static void rcopy(int[] a,int[] b){
        int len = b.length;

        for(int i = len-1; i>=0; i--){
            a[len-1-i] = b[i];
        }
    }

    public static void main(String[] args){
        int a[] = new int[5];
        int b[] = new int[] {1,2,3,4,5};

        rcopy(a,b);

        for(int i = 0; i<a.length; i++)
            System.out.println(a[i]);
    }
}
