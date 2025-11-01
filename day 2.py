import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(b)


print("Shape:", b.shape)
print("Dimension:", b.ndim) 
print("Data Type:", b.dtype)
print("Size:", b.size)


zeros = np.zeros((2, 3))
ones = np.ones((3, 3))
range_array = np.arange(1, 10, 2)   
random_array = np.random.randint(1, 100, (3, 3))
print(zeros)
print(ones)
print(range_array)
print(random_array)


arr = np.array([10, 20, 30, 40, 50])
print(arr[0])      
print(arr[-1])     
print(arr[1:4])    

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix[0, 2])     # Row 0, Column 2
print(matrix[:, 1])     # All rows, column 1
print(matrix[1:, :2])   # Submatrix


x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])
print(x + y)
print(x * y)
print(x ** 2)
print(np.sqrt(x))


data = np.array([5, 10, 15, 20, 25])
print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Addition:\n", A + B)
print("Matrix Multiplication:\n", np.dot(A, B))
print("Transpose:\n", A.T)


import numpy as np
students = ["Pradip", "Ravi", "Anjali"]
marks = np.array([
    [85, 78, 92, 88, 90],
    [70, 65, 80, 75, 85],
    [60, 55, 65, 70, 68]
])
average_marks = np.mean(marks, axis=1)
grades = np.where(average_marks >= 80, "A",
          np.where(average_marks >= 60, "B", "C"))
for i in range(len(students)):
    print(f"{students[i]} → Avg: {average_marks[i]:.2f}, Grade: {grades[i]}")


