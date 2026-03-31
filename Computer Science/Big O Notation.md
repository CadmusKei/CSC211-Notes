
We can describe Big O as:

> How code slows as data grows

- Describes the performance of an algorithm as the amount of data increases.
- Machine independent (# steps to completetion).
- Ignore smaller operations [eg: O(n + 1) → O(n) ].

### Examples of Big O Notation:

- O(1)
- O(n)
- O(log n)
- O(n²)

n = amount of data (A variable like $x$)

<aside> 📐

> Big O is an estimation

</aside>

When finding the performance, try considering different inputs at varied values and elements. eg how big a number is or the size of an array.

---

## Simple Example Algorithm

Consider this algorithm which adds up the values as it counts up to n. Here is an example of O(n) → Linear Time. As the amount of data increases, the number of steps increases lineay.

```java
int addUp(int n) {
	int sum = 0;
		for (int i = 0; i <= n; i++){
			sum += i; 
		}	
	return sum;
}
```

Think about how many steps we have for n = 1000 compared to n = 10.

<aside> 📏

> The number of steps grows linearly with the size of n

</aside>

If it helps we can also visualise these as functions or graphs. The steps are directly proportional to the steps so we can say its like $y = x$.

Now consider:

```java
	int addUp(int n){
		int sum = n * (n + 1) / 2;
		return sum; 
```

This is O(1) → Constant time, since regardless of the size of the data we do three simple steps. We can say this is like $y=1$ since its constant.

---

### Mental Model

With this metal model we can use common functions to describe efficiency over size. For instance a program which gets more efficient as size increases can be described as 0(log n) as it logarithmically gets more efficient (This is known as logarithmic time). An example of a logarithmic algorithm would be a binary search, since we half the search scope with each iteration.

Conversely a algorithm that slows exponentially as the data size increases can be described as O(n²). This is known as quadratic time. Some familiar examples are:

- Insertion sort.
- Selection sort.
- Bubblesort.

An interesting thing to note is that, despite the quick inefficiency, these algorithms are still highly useful for small data.

O(n1) describes a highly inefficient algorithm as its rate in steps increases drastically.

---

![image.png](attachment:c5dd07a0-e2d3-4132-9bb3-6a9dbf0f84e3:image.png)

---