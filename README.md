## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rationale

### 2.1 what refactoring signs (code smells) suggest this refactoring?

Answer: Middle man is the refactoring signs suggest this refactoring because the movie class no longer needs to handle price_code anymore. 
Rental class is already response for the price_code to calculate price and rental point by itself.

### 2.2 what design principle suggests this refactoring? Why?

Answer: Single Responsibility Principle is the best choice for this refactoring because movie class only focuses on the movie details while rental class focuses on price_code for price and rental_point.
They have separate responsibilities.

### 5.2 Describe where you implement this method and the reasons for your choice.

Answer: I implement this method in the pricing module.
Because
1. The pricing module is responsible for all price logic. If we keep this method in this module, then it is a Single Responsibility Principle.
2. The pricing module is focused on price strategies, making it a suitable location for methods that determine price codes. That means if we put the function in this module, then it is a High Cohesion.



