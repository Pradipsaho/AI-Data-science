name = "Pradip"
age = 21
marks = 88.5
is_student = True

print(name, age, marks, is_student)
print(type(name), type(age), type(marks), type(is_student))

fruits = ["apple", "banana", "mango"]
fruits.append("grapes")
print(fruits)

numbers = (10, 20, 30)
print(numbers[1])

student = {"name": "Pradip", "age": 21, "dept": "AI&DS"}
print(student["name"])
student["marks"] = 90
print(student)

score = 85
if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good")
else:
    print("Needs Improvement")

for i in range(1, 6):
    print("Iteration:", i)

i = 1
while i <= 5:
    print("Loop:", i)
    i += 1

def average(a, b, c):
    return (a + b + c) / 3

result = average(85, 90, 95)
print("Average:", result)

squares = [x**2 for x in range(1, 6)]
print(squares)

