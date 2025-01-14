import csv
import numpy as np
import matplotlib.pyplot as plt

with open("tips.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  data_list = list(data)
  data_numpy = np.array(data_list)

#select every row (:), and then grabbing index position 6, which is the 7th column of the dataset
size = data_numpy[:,6]

#tips will have calculations performed on it, so turn it into a numpy array
#pass data_numpy, select every row (:), and grabbing index position 1
#You’re setting the dtype, or data type, to float because the data in the CSV file is a string
tips = np.array(data_numpy[:,1],dtype=float)

#print(tips)
#print(size)

bills = np.array(data_numpy[:,0],dtype=float)

#print(bills)

tips_percentage = tips/bills*100

print(f"The average bill amount is: ${round(np.mean(bills), 2)}")
print(f"The median bill amount is: ${round(np.median(bills), 2)}")
print(f"The smallest bill amount is: ${round(np.min(bills), 2)}")
print(f"The largest bill is ${round(np.max(bills), 2)}")

plt.scatter(size, tips_percentage, color="#8A2BE2")

plt.xlabel("Dinner Party Size")
plt.ylabel("Tip Percentage")

plt.title("Tips per party size and bill")

plt.savefig("tips_per_party.png")

