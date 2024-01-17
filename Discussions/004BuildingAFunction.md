# Building a function in Java on a top-down basis

### Introduction

What is so special about beginning the implementation of a function in Java at the outside? When working with numeric data, often we know in advance the details of a specific calculation we would like to perform. The formula (function or equation) representing our calculation is best described by utilizing conventional algebraic notation (which is symbolic). We can also think of a formula as being comprised of a series of sub calculations. Breaking a formula down like this is the essence of top-down design. To develop a more intimate understanding of top-down design, it is helpful to also understand bottom-up design. See the first hyperlink in the Resources section below to learn about both top-down and bottom-up design.

### Discussion

Here's an example that elucidates the way to convert a formula in mathematical notation to a method written in Java. Notice we start with the computation we would like to perform in symbolic form. It may be helpful to think about the series of key presses one would make with a simple scientific calculator. Once you have reviewed this example, pick a formula that operates on a numeric basis and comment on how you would approach building a method in Java to perform the computation. Specifically address how building the method header informs the way the method is implemented. See the second hyperlink in Resources below for a list of common equations.

##### Mathematical Notation

<h2 style="color:blue;">f(x,y,z) = xy + yz</h2>

##### Method Header in Java (we are starting on the outside)

<h4 style="color:blue;">private static double functionExample(double x, double y, double z)</h4>
<h4>Method Body in Java</h4>

<h4 style="color:blue;">return Math.pow(x,y) + Math.pow(y,z);</h4>

### References

[Link to Wikipedia entry on top-down and bottom-up design](https://en.wikipedia.org/wiki/Top-down_and_bottom-up_design)

[Link to Wikipedia entry on common formulas](https://en.wikipedia.org/wiki/List_of_equations)

---

# Student Answer

We can create a midpoint riemann sum, approximating the following integral

$\sum_{-5}^{12} (x^2 - x + 3)dx \: where \: n = 40$

We must first find what values are important. From this we get the following:

Function: x2 - x + 3

Lower limit: -5

Upper Limit: 12

Subintervals: 40

We can then move on to creating our code by starting with this:

````java
class Riemann
{      
    public static void main(String args[])
    {
        System.out.println(riemannSum(-5.0, 12.0, 40.0));
    }
}
````

We can now start solving, having our inputs ready. To start, we can calculate the width of each subinterval. We will do this in a new method called riemannSum.

Math Formula: $\frac{b-a}{n}$

````java
public static double riemannSum(double a, double b, double n){
    double width = (b - a) / n;
}
````

Then we can setup the formula of:

$riemannSum (a,b,n) = \sum_{i=0}^{n-1} ((a + \frac{width}{2} + i \cdot width)^2 - (a + \frac{width}{2} + i \cdot width) + 3) \cdot width$

We need to iterate it over each subinterval to create a sum of function values at the midpoint of each subinterval multiplied by the width. This will come out to look like the following:

````java
public static double riemannSum(double a, double b, double n){
    double width = (b - a) / n;
    double sum = 0.0;

    for (int i = 0; i < n; i++) {
        double first_mid_p=a + (width / 2.0) + i * width;
        sum = sum + (first_mid_p*first_mid_p-first_mid_p+3);
    }

}
````

Finally we must multiply the sum by the width to get the estimated area under the curve

````java
public static double riemannSum(double a, double b, double n){
    double width = (b - a) / n;
    double sum = 0.0;

    for (int i = 0; i < n; i++) {
        double first_mid_p=a + (width / 2.0) + i * width;
        sum = sum + (first_mid_p*first_mid_p-first_mid_p+3);
    }

    return sum * width

}
````

This leaves us with the following code:

````java
class Riemann
{     
    public static double riemannSum(double a, double b, double n){
        double width = (b - a) / n;
        double sum = 0.0;
        for (int i = 0; i < n; i++) {
            double first_mid_p=a + (width / 2.0) + i * width;
            sum = sum + (first_mid_p*first_mid_p-first_mid_p+3);
        }
    return sum * width
    }
    public static void main(String args[]) {
        System.out.println(riemannSum(-5.0, 12.0, 40.0));
    }
}
````
