# Syntax:-- plt.savefig('filename.png', dpi=300, bbox_inches='tight')
#                          OR
# Syntax:-- plt.savefig('folder_name/filename.(png/jpg/pdf..etc..)', dpi=300(for resolution), bbox_inches='tight')

import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[10,20,25,30]
fig, ax = plt.subplots(1, 2, figsize=(10, 5))  

ax[0].plot(x, y, color='red')  # First subplot
ax[0].set_title('Line Chart')
ax[1].bar(x, y, color='maroon')  # Second subplot
ax[1].set_title('Bar Chart')
plt.tight_layout()  # Adjust layout to prevent overlap
plt.suptitle("Comparison of bar and line charts")

plt.savefig('Revenue_distribution.png',dpi=300, bbox_inches='tight') # Save the plot as a PNG file with high resolution..

plt.show()