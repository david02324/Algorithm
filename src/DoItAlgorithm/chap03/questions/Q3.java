package DoItAlgorithm.chap03.questions;

public class Q3 {
    static int searchIdx(int[] a,int n,int key,int[] idx){
        int num = 0;

        for(int i = 0; i<n;i++)
            if(a[i] == key)
                idx[num++] = i;

        return num;
    }

    public static void main(String[] args) {
        int[] test = {1, 3, 6, 3, 7, 3, 5, 3};
        int[] idx = new int[test.length];
        System.out.println(searchIdx(test,test.length,3,idx));
        for(int i = 0;idx[i]!=0;i++)
            System.out.print(" " + idx[i]);
    }
}
