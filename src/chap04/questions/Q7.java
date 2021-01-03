package chap04.questions;

public class Q7 {
    private int max;
    private int head;
    private int tail;
    private int[] deque;

    Q7(int capacity){
        max = capacity;
        head = tail = capacity/2+1;

        deque = new int[max];
    }

    public class EmptyIntDequeException extends RuntimeException{
        public EmptyIntDequeException() {}
    }

    public class OverflowIntDequeException extends RuntimeException{
        public OverflowIntDequeException() {}
    }

    int pushFront(int x){
        if(head <= 0)
            throw new OverflowIntDequeException();
        return deque[head--] = x;
    }

    int pushBack(int x){
        if(tail >= max)
            throw new OverflowIntDequeException();
        return deque[tail++] = x;
    }

    int popFront(){
        if(head+1 >= tail)
            throw new EmptyIntDequeException();
        return deque[++head];
    }

    int popBack(){
        if(head+1 >= tail)
            throw new EmptyIntDequeException();
        return deque[--tail];
    }

    int front(){
        if(head+1 >= tail)
            throw new EmptyIntDequeException();
        return deque[head + 1];
    }

    int back(){
        if(head+1 >= tail)
            throw new EmptyIntDequeException();
        return deque[tail - 1];
    }
}
