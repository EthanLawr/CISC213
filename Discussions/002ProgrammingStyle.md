
# How does one distinguish good programming style from bad programming style?

## Introduction

The extent to which an implementation exhibits good programming style is somewhat subjective. Bad programming style results in code that is difficult to understand and as a result a nightmare to maintain.

## Discussion

Take a look at the following Java and comment how you think this example might be modified in light of good programming style.

````java
import java.util.Stack;

public class STACKAPP {

    public static void main(String[ ] args) {Stack<Integer> myStack8;

myStack8 = new Stack<Integer>( );

    myStack8.push(7); myStack8.push(3);

        System.out.println(myStack8.pop( ));

}//end main method

}//end STACKAPP class
````

Things to consider when forming your response include layout, indentation, white space, capitalization of variable and method names and comments. For more information on good programming style, see the Wikipedia entry listed in References, below.

## References

[Link to Wikipedia entry on programming style](https://en.wikipedia.org/wiki/Programming_style)

---

# Student Answer

I have opted to use Cornell Universities style guidelines for the following code:

````java
import java.util.Stack;

public class StackApp {
    /** Performs edits on a Java Stack and outputs a removed value */
    public static void main(String[] args) {
        Stack<Integer> myStack = new Stack<Integer>();
        myStack.push(7);
        myStack.push(3);
        System.out.println(myStack.pop());
    }
}
````
