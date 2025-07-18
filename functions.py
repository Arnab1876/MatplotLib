# Syntax----py.plot(months,sales,color="purple",linestyle="--",linewidth= "2.5",marker="o",label= "Monthly Sales Data")

import matplotlib.pyplot as plt
months=[1,2,3,4,5]   #--x-axis
sales=[1000,1500,2500,3500,5000]   #--y-axis
plt.plot(months,sales,color="purple",linestyle="--",linewidth= "2.5",marker="o",label= "Monthly Sales Data")
plt.title("<<Monthly Sales Data>>")
plt.xlabel("----Months of the Year----") # Add label for x-axis.
plt.ylabel("----Sales per Month----") # Add label for y-axis.
plt.grid(color='black',linewidth='0.5',linestyle=':') # Add grid for better readability.
plt.legend() # Add legend to the plot.
plt.xlim(1,5) # Set limits for x-axis.
plt.ylim(1000,5000) # Set limits for y-axis.
plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May']) # Set x-ticks to month names.
plt.yticks(sales, ['1K', '2K', '3K', '4K', '5K']) # Set y-ticks to sales values.
plt.show() # Display the plot.
