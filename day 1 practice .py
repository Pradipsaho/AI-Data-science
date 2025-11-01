'''
✅ Your Homework / Practice:
Modify the Student Marks Analyzer to handle 5 subjects instead of 3.
Store the results in a dictionary → {"name": "Pradip", "average": 87.6, "grade": "A"}.
Print it neatly using f-string.
'''

student_name = input("Enter student name: ")
NUM_SUBJECTS = 5 

total_marks = 0 
subject_details = {} 

for i in range(NUM_SUBJECTS):
  subject_name = input(f"Enter name for subject {i+1}: ")
  while True:
    try:
      marks = int(input(f"Enter marks for {subject_name} (out of 100): "))
      if 0 <= marks <= 100:
        break
      else:
        print("Marks must be between 0 and 100.")
    except ValueError:
      print("Invalid input. Please enter a whole number.")
      
  total_marks += marks
  subject_details[subject_name] = marks

average_score = total_marks / NUM_SUBJECTS

if average_score >= 80:
  grade = "A"
elif average_score >= 60:
  grade = "B"
elif average_score >= 40:
  grade = "C"
else: 
  grade = "Fail"

result_store = {
    "name": student_name,
    "average": round(average_score, 2),
    "grade": grade
}

print("\n--- Final Results Dictionary ---")
print(result_store)

print("\n--- Student Performance Report ---")
print(f"Student: {result_store['name']}")
print(f"Average Score: {result_store['average']}%")
print(f"Grade Achieved: {result_store['grade']}")
print("----------------------------------")