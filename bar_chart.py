# Syntax:---- plt.bar(x,height,color="color name",width="value",label="label name")

import matplotlib.pyplot as plt

product= ['Product A', 'Product B', 'Product C', 'Product D']
sales = [150, 200, 300, 250]
plt.bar(product, sales, color='blue', width=0.4, label='Sales Data')
plt.title('Sales of Products')
plt.xlabel('Products')
plt.ylabel('Sales Amount')
plt.legend()  
plt.show()