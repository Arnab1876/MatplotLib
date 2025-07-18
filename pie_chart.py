# Syntax:-- plt.pie(values,labels=label_list,colors=color_list,autopct="%1.1f%%")

import matplotlib.pyplot as plt

regions=['North America', 'Europe', 'Asia', 'South America']
revenue=[300, 200, 400, 100]
plt.pie(revenue, labels=regions, colors=['Magenta','Aqua','Yellow','Blue','Purple'],autopct='%1.1f%%')
plt.title('Revenue Distribution by Region')


plt.show()