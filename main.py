#!/usr/bin/env python3

import random
import statistics as stats

comparisons = 0

def partition(A,left_index,right_index):
    global comparisons
    pivot = A[left_index]
    i = left_index + 1
    for j in range(left_index + 1,right_index+1):
        if(A[j] < pivot):
            comparisons += 1
            A[j],A[i] = A[i],A[j]
            i+=1
            
    A[left_index],A[i-1] = A[i-1],A[left_index]
    return i-2,i

def quicksort_first(A,begining,end):
    if(begining < end):
        pivot_index = begining
        left,right = partition(A,pivot_index,end)
        quicksort_first(A,begining,left)
        quicksort_first(A,right,end)
        
def quicksort_random(A,begining,end):
    if(begining < end):
        pivot_index = random.randint(0,len(A)-1)
        A[0],A[pivot_index] = A[pivot_index],A[0]
        left,right = partition(A,begining,end)
        quicksort_first(A,begining,left)
        quicksort_first(A,right,end)
def quicksort_median(A,begining,end):
    if(begining < end):
        median_array = []
        median_array.append(A[begining])
        median_array.append(A[end])
        median_array.append(A[round(end/2)])
        median = int(stats.median(median_array))
        median_index = 0
        for i in range(0,len(A)):
            if median == A[i]:
                median_index = i
        A[0],A[median_index] = A[median_index],A[0]
        
        left,right = partition(A,begining,end)
        quicksort_first(A,begining,left)
        quicksort_first(A,right,end)
  
filename = input("Please enter a filename:\n")
variant = input("Please enter a Quicksort variant:\n").lower()
file = open(filename,"r")
numberStrings = file.readlines()
numbers = []
for number in numberStrings:
    numbers.append(int(number))
    if(variant == "first"):      
        quicksort_first(numbers,0,len(numbers) - 1)
    elif(variant == "median3"):
        quicksort_median(numbers,0,len(numbers) - 1)
    elif(variant == "random"):
        quicksort_random(numbers,0,len(numbers) - 1)
    else:
         print("That's not an option.")

print(comparisons)
