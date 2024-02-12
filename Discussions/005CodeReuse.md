# What's so special about code reuse?

## Introduction

When we build software in enterprise and organization contexts it is a good idea to first design the implementation one plans on making. At the outset, a software engineer gathers requirements. These requirements then inform the general specifications of what one builds. These specifications enable selecting library components. By practicing code reuse, one has assurance that selected library components have been thoroughly tested. As a result, what is built does not have to be subject to as much testing. Code reuse is a real time saver.

## Discussion

Inspect the two linked list implementations listed in Resources below. Note the first implementation relies upon a linked list in the Java application programming interface, or API. Then comment on these implementations. Specifically address why the first implementation is an example of software engineering. What are the advantages of the second implementation? Do you see how code reuse and building from scratch differ?

## Resources

[W3Schools tutorial on Java's built in linked listLinks to an external site.](https://www.w3schools.com/java/java_linkedlist.asp)

[An implementation from scratch of a linked list in Java](./LocalLinks/LinkedList.java)

---

The first provided example, given by w3schools, is a great example of software engineering. The code is precise and to the point and offers high readability to any oncoming developer that needs to read the code.

The second provided example gives the developer more options to work with. It is built with future production in mind and provides large amounts of utility to future developers. This version of a linked list also provides more control as well as versatility, as it shows each method and allows any data type to be used. There is a clear advantage to using this well commented code over the w3schools example.

Code reuse saves a lot of time when developing new code, allowing more development to happen more quickly.
