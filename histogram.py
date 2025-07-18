# Syntax:-- plt.hist(data,bins=number_of_bins,color="color name",edgecolor="color name",label="label name")

import matplotlib.pyplot as plt

scores=[45,50,68,72,76,79,80,89,96,110,120,129,130,139,145,158,165,178,189,196,207,218,228,237,245,259,264]
plt.hist(scores,bins=10,color="Purple",edgecolor="Black")
plt.xlabel("Range of Scores")
plt.ylabel("Number of students")
plt.title("Score distribution of Students")
plt.show()