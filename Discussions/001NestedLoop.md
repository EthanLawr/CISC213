
# How do nested loops perform from a "Big O" standpoint?

## Introduction

As we have seen, [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation) enables us to get a feel for how well a given algorithm performs. Knowledge of algorithm performance in a particular context enables us to gauge whether or not what we have implemented meets the performance requirements. Gathering such requirements is part of the initial stages of the [systems development life cycle or SDLC](https://en.wikipedia.org/wiki/Systems_development_life_cycle). When we practice [top-down design](https://en.wikipedia.org/wiki/Top-down_and_bottom-up_design), initially we are not concerned about the details of the implementation being made.

## Discussion

Given the following pseudocode, how might one estimate worst-case time-complexity performance? Simply gauge approximately how many steps it takes to sort an array of key values arranged in descending order.

INSERTION-SORT(A)

    for j = 2 to A.length

        key = A[ j ]

        // Insert A[ j ] into the sorted sequence A[1 .. j -1].

        i = j - 1

        while i > 0 and A[ i ] > key

            A[ i + 1 ] = A[ i ]

            i = i - 1

        A[ i + 1 ] = key

---

# Student Answer

The loop runs for `A.length - 1` iterations. There is also a **potential** shift operation in each loop. This means that the runtime increases in proportion to the length of A, making the worst case complexity O(n^2)
