package chap04.questions;

import chap04.IntStack;

public class Q3 {
    private int max;
    private int ptrOne,ptrTwo;
    private int[] array;

    public class EmptyIntStackException extends RuntimeException{
        public EmptyIntStackException() {}
    }

    public class OverflowIntStackException extends RuntimeException{
        public OverflowIntStackException() {}
    }

    public Q3(int arrayLength){
        ptrOne = 0;
        ptrTwo = arrayLength - 1;
        max = arrayLength;
        try{
            array = new int[arrayLength];
        } catch (OutOfMemoryError e){
            max = 0;
        }
    }

    public int pushFirstStack(int x) throws OverflowIntStackException{
        if(ptrOne >= ptrTwo)
            throw new OverflowIntStackException();
        return array[ptrOne++] = x;
    }

    public int pushSecondStack(int x) throws OverflowIntStackException{
        if(ptrOne >= ptrTwo)
            throw new OverflowIntStackException();
        return array[ptrTwo--] = x;
    }

    public int popFirstStack() throws EmptyIntStackException {
        if(ptrOne <= 0)
            throw new EmptyIntStackException();
        return array[--ptrOne];
    }

    public int popSecondStack() throws EmptyIntStackException {
        if(ptrTwo >= max - 1)
            throw new EmptyIntStackException();
        return array[++ptrTwo];
    }
}
