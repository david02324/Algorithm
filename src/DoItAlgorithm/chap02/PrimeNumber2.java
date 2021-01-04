package DoItAlgorithm.chap02;

public class PrimeNumber2 {
    public static void main(String[] args){
        int[] primes = new int[500];
        primes[0] = 2;
        int count = 1;
        int divisionCount = 0;

        for(int i = 3; i <= 1000; i+=2){
            for(int j = 1; j<=count; j++){
                if(j==count){
                    System.out.println(i);
                    primes[j]=i;
                    count++;
                    break;
                }
                divisionCount++;
                if(i % primes[j] == 0) break;
            }
        }
        System.out.println("찾은 소수의 개수 : " + count);
        System.out.println("나눗셈 회수 : " + divisionCount);
    }
}
