# demo.py----basic plotting with matplotlib..

import matplotlib.pyplot as plt
x=['Mon','Tues','Wed','Thurs','Fri']
y=[20,15,30,45,50]

plt.plot(x,y)
plt.title("Sales of this Week")
plt.xlabel("Days of the Week")
plt.ylabel("Sales per day")
plt.show()

