Title: Implement Sorting algorithms

Objectives:
To understand and implement selection Sort
To understand and implement Bubble Sort

Problem Statement:
Write a python program to store first year percentage of students in array. Write function for
sorting array of floating point numbers in ascending order using
a) Selection Sort
b) Bubble sort and display top five scores.

Theory:
Selection Sort
Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. 

Bubble Sort
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

# How does Selection Sort Algorithm work?
Lets consider the following array as an example: arr[] = {64, 25, 12, 22, 11}

First pass:
For the first position in the sorted array, the whole array is traversed from index 0 to 4 sequentially. The first position where 64 is stored presently, after traversing whole array it is clear that 11 is the lowest value.
Thus, replace 64 with 11. After one iteration 11, which happens to be the least value in the array, tends to appear in the first position of the sorted list.
