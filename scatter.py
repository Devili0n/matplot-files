import matplotlib.pyplot as plt
import pandas as pd

data={'name':['ram','sahil','kishor','arbaaz'],'age':[45,78,12,25],'ranks':[3,4,1,2]}
plt.scatter(data['name'],data['age'], c=data['ranks'],s=20)
plt.bar( data['name'],data['age']) 
# Adding Title to the Plot
plt.title("Scatter Plot")
 
# Setting the X and Y labels
plt.xlabel('Name')
plt.ylabel('Age')
 
plt.colorbar()
plt.show()
