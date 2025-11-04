'''🏠 Homework (Practice for Day 3)
Add a new column Result — value should be:
"Pass" if grade ≠ Fail, else "Fail".
Find average marks per grade using groupby("Grade")["Average"].mean().
Sort the DataFrame by "Average" descending and print top 2 students.'''

import pandas as pd
student_data = {
    "name" : [ "pradip","sandip","ankit","amit","anil","sunil","ayush","arbind"],
    "hindi" : [ 90,60,70,80,90,67,87,90],
    "english" : [ 90,89,78,68,97,78,68,58],
    "math" : [ 94,78,49,98,68,78,57,78],
    "science" : [ 89,67,50,89,78,67,90,98]
}
show_table = pd.DataFrame(student_data)
show_table["average"] = show_table[["hindi","english","math","science"]].mean(axis=1)
show_table
def grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"
show_table["grade"] = show_table["average"].apply(grade)
show_table["Result"] = show_table["grade"].apply(lambda x: "Pass" if x != "Fail" else "Fail")
average_marks_per_grade = show_table.groupby("grade")["average"].mean()
sorted_show_table = show_table.sort_values(by="average", ascending=False)
top_2_students = sorted_show_table.head(2)
print("--- 1. Complete DataFrame with 'Result' ---")
print(show_table)
print("\n--- 2. Average Marks per Grade ---")
print(average_marks_per_grade)
print("\n--- 3. Top 2 Students ---")
print(top_2_students)

