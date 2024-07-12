import csv
import matplotlib.pyplot as plt

def srednja_vr_x(rows):
    # Tacka x usrednjene, da se nadje centar loptice
    srednje_x = []
    samo_x = []
    suma = 0
    for row in rows:
        samo_x.append(row[0:6])
        #print(samo_x)
    for i in samo_x:
        #print(i)
        suma = 0
        for j in i:
            #print(j)
            suma = suma + float(j)
        rez = suma/6
        srednje_x.append(rez)
    return srednje_x

def srednja_vr_y(rows):
    # Tacka y usrednjene, da se nadje centar loptice
    srednje_y = []
    samo_y = []
    suma = 0
    for row in rows:
        samo_y.append(row[6:12])
    #print("Samo y:",samo_y)
    for i in samo_y:
        #print(i)
        suma = 0
        for j in i:
            #print(j)
            suma = suma + float(j)
        rez = suma/6
        srednje_y.append(rez)
    return srednje_y

def srednja_vr_z(rows):
    # Tacka z usrednjene, da se nadje centar loptice
    srednje_z = []
    samo_z = []
    suma = 0
    for row in rows:
        samo_z.append(row[12:18])
    #print("Samo z:",samo_z)
    for i in samo_z:
        #print(i)
        suma = 0
        for j in i:
            #print(j)
            suma = suma + float(j)
        rez = suma/6
        srednje_z.append(rez)
    return srednje_z

# csv file name
filename = "normalizovani podaci/norm_po_osama_cet_1_07.csv"

# initialzing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

srednje_x= srednja_vr_x(rows)
print("Srednja vrednost za x osu: ",srednje_x)
srednje_y= srednja_vr_y(rows)
print("Srednja vrednost za y osu: ",srednje_y)
srednje_z= srednja_vr_z(rows)
print("Srednja vrednost za z osu: ",srednje_z)

# data plotting
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(srednje_x,srednje_y,srednje_z,'green')
ax.set_xlabel('x osa')
ax.set_ylabel('y osa')
ax.set_zlabel('z osa')
ax.set_title('3D projectile motion')
plt.show()


