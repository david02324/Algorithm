package chap04.questions;

public class Q4 {
    private int max;
    private int num;
    private int[] que;

    public class EmptyIntQueueException extends RuntimeException{
        public EmptyIntQueueException() {}
    }

    public class OverflowIntQueueException extends RuntimeException{
        public OverflowIntQueueException() {}
    }

    public Q4 (int capacity) {
        max = capacity;
        num = 0;
        try {
            que = new int[max];
        }catch(OutOfMemoryError e){
            max = 0;
        }
    }

    public int enque(int x) throws OverflowIntQueueException{
        if(num >= max)
            throw new OverflowIntQueueException();
        return que[num++] = x;
    }

    public int deque(int x) throws EmptyIntQueueException{
        if(num <= 0)
            throw new EmptyIntQueueException();
        int value = que[0];
        for(int i = 1; i < num; i++)
            que[i-1] = que[i];
        return value;
    }

    public int peek() throws EmptyIntQueueException{
        if(num <= 0)
            throw new EmptyIntQueueException();
        return que[0];
    }

    public int indexOf(int x) {
        for(int i=0; i<num; i++)
            if(que[i]==x)
                return i;
        return -1;
    }

    public void dump(){
        for(int i = 0; i<num; i++)
            System.out.println("i : " + que[i]);
    }

}
