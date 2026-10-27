# nCr Table

**Platform:** HackerRank  
**Problem:** [nCr Table](https://www.hackerrank.com/challenges/ncr-table/problem)  
**Topic:** Mathematics, Combinatorics, Dynamic Programming  
**Difficulty:** As listed on HackerRank

## Problem Statement

Jim is doing his discrete mathematics homework, which requires him to repeatedly calculate binomial coefficients, \( \binom{n}{r} \) (read as “n choose r”), for different values of \(n\).

Knowing that this is time-consuming, he asks his sister June for help. June, a computer science student, realizes that the calculations can be automated. By storing previously calculated values, she can use a simple formula to calculate higher values efficiently.

Given an integer \(n\), calculate all the binomial coefficients from \( \binom{n}{0} \) to \( \binom{n}{n} \).

Since the values can be large, output each coefficient modulo \(10^9\), keeping only the last nine digits.

## Mathematical Definition

The binomial coefficient is defined as:

$$
\binom{n}{r} = \frac{n!}{r!(n-r)!}
$$

It can also be calculated using the recurrence relation:

$$
\binom{n}{r}
=
\binom{n-1}{r-1}
+
\binom{n-1}{r}
$$

The boundary conditions are:

$$
\binom{n}{0} = \binom{n}{n} = 1
$$

## Input Format

- The first line contains an integer \(T\), representing the number of test cases.
- The next \(T\) lines each contain an integer \(n\).

## Output Format

For each test case, print the values

$$
\binom{n}{0}, \binom{n}{1}, \ldots, \binom{n}{n}
$$

on a single line, separated by a single space.

Each value must be calculated modulo \(10^9\).

## Constraints

- \(1 \leq T \leq 200\)
- \(1 \leq n < 1000\)

## Sample Input

```text
3
2
4
5
```

## Sample Output

```text
1 2 1
1 4 6 4 1
1 5 10 10 5 1
```

## Explanation

For \(n = 2\), the binomial coefficients are:

$$
\binom{2}{0}=1,\quad
\binom{2}{1}=2,\quad
\binom{2}{2}=1
$$

Therefore, the output is:

```text
1 2 1
```

The other test cases follow the same pattern.

## Solution

*To be added.*

## Complexity Analysis

*To be added after documenting the chosen approach.*