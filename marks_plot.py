# Display the marks of two students for 5 subjects using suitable graphical tools.

import matplotlib.pyplot as plt
import numpy as np

# Student names
students = ['Student 1', 'Student 2']

# Marks for each subject
subjects = ['Math', 'Science', 'English', 'History', 'Geography']
marks_student1 = [85, 90, 75, 80, 70]
marks_student2 = [78, 85, 82, 79, 88]

# Setting the positions and width for the bars
pos = np.arange(len(subjects))
print(pos)
width = 0.3

# Plotting
plt.bar(pos-width/2, marks_student1, width=width, label=students[0])
plt.bar(pos+width/2, marks_student2, width=width, label=students[1])

# Adding labels
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title('Marks of Students')
plt.xticks(pos, subjects)
plt.legend()

plt.show()
