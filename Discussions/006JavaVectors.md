# The Java Collections Framework Vector vis-à-vis a Conventional Array

## Introduction

The Java Collections Framework or JCF provides us with a Vector class which we can utilize to process a single column of data. Of course the Vector class is based upon a mathematical construct also called a *vector*. One might visualize a vector as a single column in a Microsoft Excel spreadsheet. We might be talking about thousands of entries, one after the other. A common way to store such data is in a relational database such as *Microsoft Access* or *MySQL*. When the data are stored in a relation or table in a relational database, it is relatively easy to query the data to obtain various statistical measures. It is also possible to warehouse data in a CSV or *comma-separated values file*. CSV files offer a mechanism to share data which might be processed in a variety of contexts. The JCF Vector class is applicable when one is tasked with processing large volumes of data. As it turns out, a *conventional array* is very similar to a Vector object. There is one important distinction. A Vector can *grow and shrink* as needed. A conventional array is *fixed in size* once it is declared. Keep in mind an array may be more appropriate in certain contexts *rather* than a Vector.

## Discussion

Thinking back to the [CSV file](./LocalLinks/CISC213JCFExercise.csv) and the provided [Java application](./LocalLinks/WeatherVectorApp.java) to process the CSV file, why is it advantageous to place a reliance upon the Vector class instead of a *conventional array* of doubles? Consider the fact that *Vectors* can grow and shrink as needed, while once memory is allocated for an array, its size *cannot* change. Bear in mind we do not know how many temperature readings there are in the CSV file.

## References

[Official documentation on the Vector class, published by OracleLinks to an external site.](https://docs.oracle.com/javase/8/docs/api/java/util/Vector.html)

[Official documentation on conventional arrays, published by OracleLinks to an external site.](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html)

---

## Student Answer

Incomplete.