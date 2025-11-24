import matplotlib.pyplot as plt

students_names = ["Nikhil", "Jathin", "Sharan", "Hridyansh", "Ayansh", "Ashwath", "Pranit", "Eshaan"]
students_marks = [98, 37, 86, 93, 60, 70, 59, 67]
marks_percent = []

for x in students_marks:
    res = (x/100)*100
    marks_percent.append(res)

print(marks_percent)

def line_chart_of_students_and_marks():
    plt.plot(students_names, students_marks)
    plt.title("Student Marks Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Student Marks")
    plt.show()

line_chart_of_students_and_marks()

def percent_bar_start():
    plt.bar(students_names,marks_percent)
    plt.title("Students Percentage Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Student Percentage")
    plt.show()

percent_bar_start()