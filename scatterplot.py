# Syntax:-- plt.scatter(x, y, color="color name", marker="marker_style" label="label name")
# x--independent variable, y--dependent variable

import matplotlib.pyplot as plt

hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]  # Independent variable
exam_scores = [50, 60, 70, 80, 90, 95, 100, 110]  # Dependent variable
plt.scatter(hours_studied, exam_scores, color='red', marker='^', label='Student Report')
plt.title('Exam Scores vs Hours Studied')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.legend()
plt.grid(True)  # Add grid for better readability
plt.show()  # Display the plot

# ------------------------------------------

# Grouping::Two plots at a time--

import matplotlib.pyplot as plt

plt.scatter([1, 2, 3], [50,55,60], color='black', marker='o', label='Class A')  #Group-1
plt.scatter([1, 2, 3], [45,50,57], color='red', marker='x', label='Class B')    #Group-2
plt.title('Comaprison of Two Classes: A & B')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.legend()
plt.grid(True)  # Add grid for better readability
plt.show()  # Display the plot
