
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

### Tips for recursion

- $a^{log(b)}=b^{log(a)}$

# Big-O Examples

## Example 1: Linear Loop
```java
void example1(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
        System.out.println(arr[i]);
    }
}
```
**T(n) = n** | **O(n)**

Single loop over n elements → linear.

---

## Example 2: Loop Over Half Array
```java
void example2(int[] arr) {
    for (int i = 0; i < arr.length/2; i++) {
        System.out.println(arr[i]);
    }
}
```
**T(n) = n/2** | **O(n)**

Constants ignored in Big-O → still linear.

---

## Example 3: Logarithmic Loop
```java
void example3(int n) {
    for (int i = n; i > 0; i /= 2) {
        System.out.println(i);
    }
}
```
**T(n) = log₂(n)** | **O(log n)**

Each iteration halves input → logarithmic iterations.

---

## Example 4: Nested Loop
```java
void example4(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            System.out.println(i+j);
        }
    }
}
```
**T(n) = n²** | **O(n²)**

Two nested loops → multiply iterations → quadratic.

---

## Example 5: Single Loop
```java
void example5(int n) {
    for (int i = 0; i < n; i++) {
        System.out.println(i);
    }
}
```
**T(n) = n** | **O(n)**

Straightforward linear.

---

## Example 6: Multiple Independent Loops
```java
void example6(int n) {
    for (int i = 0; i < n; i++) {}
    for (int j = 0; j < n; j++) {}
}
```
**T(n) = 2n** | **O(n)**

Big-O drops constants → linear.

---

## Example 7: Triangular Loop
```java
void example7(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            System.out.println(i+j);
        }
    }
}
```
**T(n) = 1 + 2 + ... + (n-1) = n(n-1)/2** | **O(n²)**

Triangular sum → quadratic.

---

## Example 8: Recursive — Two Calls on n/2
```java
void example8(int n) {
    if (n <= 1) return;
    example8(n/2);
    example8(n/2);
}
```
**T(n) = 2T(n/2) + 1** | **O(n)**

Each level doubles calls, input halves → geometric sum → linear.

---

## Example 9: Recursive — Two Calls on n-1
```java
void example9(int n) {
    if (n <= 1) return;
    example9(n-1);
    example9(n-1);
}
```
**T(n) = 2T(n-1) + 1** | **O(2ⁿ)**

Input decreases by 1, two calls per node → exponential growth.

---

## Example 10: Recursive — Three Calls on n/2
```java
void example10(int n) {
    if (n <= 1) return;
    example10(n/2);
    example10(n/2);
    example10(n/2);
} 
```
**T(n) = 3T(n/2) + 1** | **O(n^log₂(3)) ≈ O(n^1.585)**

 Branching factor = 3, input halves → 3^k · T(n/2^k) + geometric sum.
---

![[Time Complexity.pdf]]