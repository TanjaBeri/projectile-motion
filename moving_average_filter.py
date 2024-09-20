import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os import path

MARKERI = 6
ALPHA=0.2

# Ucitavanje usrednjenih vrednosti, i koriscenje Exponential Moving Average

    # ucitavanje file path-a
file_path = 'normalizovani podaci' #input("Enter the file path: ") 
file_name =  'usr_Cet_1_08.csv'#input("Enter the file name with extension (.csv)(normalizovani podaci): ")
full_path = path.join(file_path,file_name)

print(f"Full file address is: {full_path}")
# csv file name
filename = full_path

# initialzing the titles and rows list
fields = []
rows = []
with open(filename, 'r') as csvfile:
# creating a csv reader object
    csvreader = csv.reader(csvfile)

# extracting field names through first row
    fields = next(csvreader)

# extracting each data row one by one
    for row in csvreader:
        rows.append(row)

# get total number of rows
    total_num_rows = csvreader.line_num
    print("Total no. of rows: ",total_num_rows)


# Ucitavanje zasebnih kolona iz fajla
X_kol = []
Y_kol = []
Z_kol = []
for niz in rows[0:]:
    X_kol.append(niz[0])
    Y_kol.append(niz[1])
    Z_kol.append(niz[2])

print("x kol iz csv",X_kol)

X_kol1 = pd.DataFrame(X_kol)
print("X kolona",X_kol1)
X_list = [float(item) for item in X_kol]


'''X_kol_list = []

for df in X_kol:
    temp = X_kol[df].tolist()
    X_kol_list.append(temp)




print("X kol lista!!!!",X_kol_list)'''

Y_kol1 = pd.DataFrame(Y_kol)
print("Y kolona",Y_kol1)
Y_list = [float(item) for item in Y_kol]
'''Y_kol_list = []

for df in Y_kol:
    temp = Y_kol[df].tolist()
    Y_kol_list.append(temp)'''


Z_kol1 = pd.DataFrame(Z_kol)
print("Z kolona",Z_kol1)
Z_list = [float(item) for item in Z_kol]
'''Z_kol_list = []

for df in Z_kol:
    temp = Z_kol[df].tolist()
    Z_kol_list.append(temp)'''

za_ema = pd.DataFrame(rows)
#print(za_ema)

ema = za_ema.ewm(alpha=ALPHA).mean()

#print("ema",ema)

ema_X = ema.iloc[:, 0]
ema_Y = ema.iloc[:,1]
ema_z = ema.iloc[:,2]

print("ema x",ema_X)

''' ema_X_list = []

for df in ema_X:
    temp = ema_X[df].tolist()
    ema_X_list.append(temp)

ema_Y_list = []

for df in ema_Y:
    temp = ema_Y[df].tolist()
    ema_Y_list.append(temp)

ema_Z_list = []

for df in ema_z:
    temp = ema_z[df].tolist()
    ema_Z_list.append(temp)'''




# data plotting
plt.axes(projection='3d')
plt.plot(X_list,Y_list,Z_list,'r',label='Usrednjene vredn.')
plt.plot(ema_X,ema_Y,ema_z,'b',label='EMA vrednosti')

plt.title(file_name)
plt.legend()
plt.show()

print("X_list[1] = ",X_list[1])

t = abs((X_list[-1] - X_list[0])) / len(X_list)
print("t=",t)

    








