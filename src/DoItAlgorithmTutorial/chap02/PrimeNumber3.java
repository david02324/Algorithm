package DoItAlgorithmTutorial.chap02;

public class PrimeNumber3 {
    public static void main(String[] args){
        int[] primes = new int[500];
        primes[0] = 2;
        primes[1] = 3;
        int count = 2;
        int calculateCount = 0;

        for(int i = 5; i <= 1000; i+=2) {
            boolean squ = false;
            for(int j = 1; primes[j]*primes[j] <= i; j++){
                calculateCount+=2;
                if(i % primes[j] == 0) {
                    squ = true;
                    break;
                }
            }
            if(!squ){
                System.out.println(i);
                primes[count++] = i;
                calculateCount++;
            }
        }

        System.out.println("찾은 소수의 개수 : " + count);
        System.out.println("나눗셈 회수 : " + calculateCount);
    }
}

