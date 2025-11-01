'''🏠 Homework (Practice Tasks)
Create an array of 10 random integers between 1–100 and print:
Mean, Median, Standard Deviation.
Create two 3×3 matrices and perform:
Addition, Subtraction, Matrix Multiplication.
Find top 3 marks for each student using np.sort() or slicing.'''
import numpy as np
random = np.random.randint(0,100,10)
print(random)
mean  = np.mean(random)
median = np.median(random)
s_d = np.std(random)
print(mean)
print(median)
print(s_d)

matrix1 = np.random.randint(1,50,(3,3))
matrix2 = np.random.randint(1,50,(3,3))
print(matrix1)
print(matrix2)
print("add: \n" , matrix1+matrix2)
print("sub :\n", matrix1-matrix2)
print("matrix multiple: \n " , np.dot(matrix1,matrix2))



import numpy as np

marks = np.array([
    [85, 78, 92, 88, 90],
    [70, 65, 80, 75, 85],
    [60, 55, 65, 70, 68]
])

sorted_marks = np.sort(marks, axis=1)
top3_marks = sorted_marks[:, -3:]
top3_avg = np.mean(top3_marks, axis=1)

for i in range(len(marks)):
    print(f"Student {i+1} → Top 3 Marks: {top3_marks[i]}, Average: {top3_avg[i]:.2f}")
