### Lambdas ###

"""
Lambda function is a small anonymous function without a name.
It can take any number of arguments, but can only have one expression.
Lambda function is similar to anonymous functions in JavaScript.
We need it when we want to write an anonymous function inside another function.
"""

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2, 4))

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4))

#* Exercises

#* Write a lambda function which can solve a slope or y-intercept of linear functions.

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else "Error: Division by zero"

y_intercept = lambda m, x, y: y - m * x

# Calculate the slope of a line passing through points (1, 2) and (3, 4)
m = slope(1, 2, 3, 4)
print(m)  # Output: 1.0

# Calculate the slope of a line passing through points (1, 2) and (1, 3)
m = slope(1, 2, 1, 3)
print(m)  # Output: Error: Division by zero

# Calculate the y-intercept of a line with slope 1 and passing through point (2, 3)
b = y_intercept(1, 2, 3)
print(b)  # Output: 1.0