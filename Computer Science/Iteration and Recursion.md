# **Iteration**

Iterative algorithms are algorithms that have a **loop** within them (Since there are multiple iterations) eg: _while_ and _for._

With iteration we consider:

- What is changed each time we go through the loop?
- How do i keep track of the number of times through the loop?
- When can I stop?
- Where is the result when I stop?

**Simple example**: Imagine we don't have the `*` operator for multiplication and we must write our own function for it.

```python
def mult(a, b):
	total = 0
	for n in range(b):
		total += a
	return total
```

Or with a while:

```python
	def mult_iter(a,b):
		result = 0
		while (b > 0):
			result += a
			b -= 1
		return result
```

# **Converting Iterative to recursive**

<aside> ✨

Recursion = Repeat

</aside>

- Recognise that we have a problem that we are solving many times.
- Decompose the problem into:
    - Something you know.
    - And then the same problem again.
- A simple example:
    - (5*4)
    - = 5+(5*3)
    - = 5+(5+(5*2))
    - = 5+(5+(5+(5*1))

Recognise that we are dividing the part we dont know into something similar until we get a very simple problem like 5_1. and once we understand what 5_1 is, we can build our way back till we have a final answer.

<aside> ✨

This is the structure of recursion. Divide your work down until a simple condition or problem is met, and work our way up from there.

</aside>

The manner in which we recursively (repeatedly) divide our problem into smaller, easier problems, is by calling the same function in itself. This is recursion.

- = 5+(5+(5+(5))
- = 5+(5+(10))
- = 5 + (15)
- = 20

## Steps of recursion

- Recursive Step (repeating step):
    - Decide how to reduce problem into a smaller/simpler version of the same problem.
- Base case
    - Keep reducing problem until reach a simple case that can be solved directly.
    - When b = 1, a*b = a.

**Multiplication via Recursion:**

```python
def mult_recurs(a, b):
	if b == 1: 
		return a
	else:
		 return a + mult_recurs(a, b - 1)
```

Note how we are calling the function within itself to reduce the problem to a simple one, and then solving upwards in steps (these steps are known as scope).

> Notice these patterns:

**Base Case**

A conditional, followed by a return of the simplest form.

```python
if b == 1: 
		return a
```

**Recursive Step**

The function calls itself with a modification to arguments.

```python
	else:
		 return a + mult_recurs(a, b - 1)
```

## The Grasping Idea!

The final important idea to keep in mind when writing recursive code is that the recursive step must move one step closer to the base case!

## **NB: Visualise It!**

[https://pythontutor.com/visualize.html#mode=edit](https://pythontutor.com/visualize.html#mode=edit)

<aside> ✨

Paste this code in python tutor! A tool that visualises the steps in your code!

</aside>

```python
def mult_recurs(a, b):
    if b == 1: 
        return a
    else:
         return a + mult_recurs(a, b - 1)
         
print(mult_recurs(5, 4))
```

> You can use python tutor for Java too!

<aside> ✨

Try writing the Java version and visualising it on python tutor.

</aside>

```java
public class MergeSort{
    public static void main(String[] args){

        System.out.println(mult(6,4));
    }

    static int mult(int a, int b) {
        if (b == 1) return a;
        else return a + mult(a, b - 1);
    }
}
```

# Another example

**Iterative Algorithm:**

```java
static int power(int a, int b) {
        int result = 1;
        for (int i = 0; i < b; i++) {
            result *= a;
        }
        return result;
    }
```

**Recursive Algorithm:**

```java
static int power_rec(int a, int b)
    {
        if (b == 0) return 1;
        else return a*power_rec(a, b-1);
    }
```

<aside> ✨

Just because recursion can reduce time complexity doesn't mean it is always more efficient, due to scope levels it can take more space than a single variable inerrable algorithm.

</aside>
