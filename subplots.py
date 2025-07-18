# Syntax:-- plt.subplots(nrows, ncols, index,)

import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[10,20,25,30]
plt.subplot(1,2,1) #---- 1 row, 2nd column, 1st subplot
plt.plot(x,y,color='red')
plt.title('Line Chart')

plt.subplot(1,2,2) #---- 1 row, 2nd column, 2nd subplot
plt.bar(x,y,color='maroon')
plt.title('Bar Chart')
#plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()  # Display the plots

# ------------------------------------------

# Multiple Plots-- subplots()

# Syntax:-- fig,ax=plt.subplots(nrows,ncols,figsize=(width,height))


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
plt.show()