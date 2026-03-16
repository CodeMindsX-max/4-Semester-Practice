 
import numpy as np 
import matplotlib.pyplot as plt 
 
# Data 
categories = ['A', 'B', 'C', 'D', 'E'] 
values1 = [23, 45, 56, 78, 32] 
values2 = [40, 35, 60, 55, 25] 
 
# Plot 
x = np.arange(len(categories)) 
width = 0.35 
 
fig, ax = plt.subplots() 
rects1 = ax.bar(x - width/2, values1, width, label='Group 1') 
rects2 = ax.bar(x + width/2, values2, width, label='Group 2') 
 
ax.set_xlabel('Categories') 
ax.set_ylabel('Values') 
ax.set_title('Grouped Bar Graph') 
ax.set_xticks(x) 
ax.set_xticklabels(categories) 
ax.legend() 
 
plt.show() 