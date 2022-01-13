package DoItAlgorithmTutorial.chap04.questions;

public class Q6<E> {
    private int max;
    private int front;
    private int rear;
    private int num;
    private E[] que;


    public Q6(int capacity){
        num = front = rear = 0;
        max = capacity;
        try{
            que = (E[]) new Object[max];
        } catch (OutOfMemoryError e){
            max = 0;
        }
    }

    public E enque(E x){
        if(num >= max) {
            System.out.println("큐가 가득 참");
            return null;
        }
        que[rear++] = x;
        num++;
        if(rear==max)
            rear = 0;
        return x;
    }

    public E deque(){
        if(num <= 0)
        {
            System.out.println("큐가 비었음");
            return null;
        }
        E x = que[front++];
        num--;
        if(front == max)
            front = 0;
        return x;
    }

    public E peek(){
        if(num<=0)
        {
            System.out.println("큐가 비었음");
            return null;
        };
        return que[front];
    }

    public int indexOf(E x){
        for(int i = 0; i<num; i++){
            int idx = (front+i) % max;
            if(que[idx] == x)
                return idx;
        }
        return -1;
    }

    public void clear(){
        num = front = rear = 0;
    }

    public int capacity(){
        return max;
    }

    public int size(){
        return num;
    }

    public boolean isEmpty(){
        return num <= 0;
    }

    public boolean isFull(){
        return num >= max;
    }

    public void dump(){
        if(num<=0)
            System.out.println("큐가 비어 있습니다");
        else{
            for(int i = 0; i < num; i++)
                System.out.println(que[(front + i) % max] + " ");
            System.out.println();
        }
    }
}

