Title: Implement Sorting algorithms

Objectives:
To understand and implement Selection Sort
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

Second Pass:
For the second position, where 25 is present, again traverse the rest of the array in a sequential manner.
After traversing, we found that 12 is the second lowest value in the array and it should appear at the second place in the array, thus swap these values.

Third Pass:
Now, for third place, where 25 is present again traverse the rest of the array and find the third least value present in the array.
While traversing, 22 came out to be the third least value and it should appear at the third place in the array, thus swap 22 with element present at third position.

Fourth pass:
Similarly, for fourth position traverse the rest of the array and find the fourth least element in the array 
As 25 is the 4th lowest value hence, it will place at the fourth position.

Fifth Pass:
At last the largest value present in the array automatically get placed at the last position in the array
The resulted array is the sorted array.

# How does Bubble Sort Algorithm work?
  In Bubble Sort algorithm, 
  -- Traverse from left and compare adjacent elements and the higher one is placed at right side. 
  -- In this way, the largest element is moved to the rightmost end at first. 
  -- This process is then continued to find the second largest and place it and so on until the data is sorted.

  Total no. of passes: n-1
  Total no. of comparisons: n*(n-1)/2

Step 1: We start with an unsorted array.
[7, 12, 9, 11, 3] 

Step 2: We look at the two first values. Does the lowest value come first? Yes, so we don't need to swap them.
[7, 12, 9, 11, 3] 

Step 3: Take one step forward and look at values 12 and 9. Does the lowest value come first? No.
[7, 12, 9, 11, 3] 

Step 4: So we need to swap them so that 9 comes first.
[7, 9, 12, 11, 3] 

Step 5: Taking one step forward, looking at 12 and 11.
[7, 9, 12, 11, 3]

Step 6: We must swap so that 11 comes before 12.
[7, 9, 11, 12, 3] 

Step 7: Looking at 12 and 3, do we need to swap them? Yes.
[7, 9, 11, 12, 3]

Step 8: Swapping 12 and 3 so that 3 comes first.
[7, 9, 11, 3, 12] 

# Conclusion
Hence in this program we learnt how to implement selection Sort and Bubble Sort.
