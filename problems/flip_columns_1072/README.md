### Problem 472
https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

#### Description
Given a matrix consisting of 0s and 1s, we may choose any number of columns in the matrix and flip every cell in that column.  Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.

Return the maximum number of rows that have all values equal after some number of flips.

#### Exapmles
```
Input: [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.
```

```
Input: [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.
```