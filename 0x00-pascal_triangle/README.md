# 0x00-pascal_triangle Challenge

## Overview

This project involves generating Pascal's Triangle up to a specified number of rows using Python. Pascal's Triangle is a triangular array of the binomial coefficients. Each number is the sum of the two directly above it.

## Description

The `pascal_triangle` function takes an integer `n` as input and returns a list of lists of integers representing Pascal's Triangle up to `n` rows. This function handles edge cases where `n` is less than or equal to 0 by returning an empty list. For `n` equal to 1, it returns the first row `[1]`.

## Function Signature

```python
def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
        n (int): Number of rows of Pascal's Triangle to generate.

    Returns:
        List of lists of int: Pascal's Triangle up to n rows.
    """
```

## Algorithm

1. **Initialization**:
   - Start with an empty list `triangleElements`.
   - If `n` is 0 or less, return the empty list.
   - Initialize the first row as `[1]` and add it to `triangleElements`.

2. **Generate Rows**:
   - Loop from `1` to `n-1` to generate each subsequent row.
   - For each row, start with `[1]`.
   - Use the previous row to calculate the current row's elements:
     - Each new element is the sum of the two elements directly above it from the previous row.
   - End each row with `[1]`.
   - Append the completed row to `triangleElements`.

3. **Return Result**:
   - Return `triangleElements` which now contains all rows up to `n`.

## Example Usage

```python
print(pascal_triangle(5))
```

**Output**:

```python
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
```

## Edge Cases

- `n <= 0`: Return an empty list.
- `n == 1`: Return `[[1]]`.

## How to Run

1. Save the function in a Python file (e.g., `pascal_triangle.py`).
2. Import and call the function from another script or an interactive Python session.

## Code

To see the implementation, refer to the [0-pascal_triangle.py](0-pascal_triangle.py) file.

## Conclusion

This project demonstrates the creation of Pascal's Triangle using a simple algorithm involving nested loops. The function is efficient and handles basic edge cases, making it a reliable tool for generating Pascal's Triangle up to any specified number of rows.
