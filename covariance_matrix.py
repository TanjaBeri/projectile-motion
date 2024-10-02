import numpy as np
# from kosi_hitac_jef_copy import trajectories
from kosi_hitac_sa_gausom import trenutna

print("Trajecotries:",trenutna)
print("Shape:",np.shape(trenutna))
print("Len:",len(trenutna))

# Finding means of x, y and z
suma_x = 0
for i in trenutna[0,:]:
    # print(i)
    suma_x = suma_x + int(i)
mean_x = suma_x/ len(trenutna)
print("Mean_x:",mean_x)

suma_y = 0
for j in trenutna[1,:]:
    # print(i)
    suma_y = suma_y + int(j)
mean_y = suma_y/ len(trenutna)
print("Mean_y:",mean_y)

suma_z = 0
for k in trenutna[2,:]:
    # print(i)
    suma_z = suma_z + int(k)
mean_z = suma_z/ len(trenutna)
print("Mean_x:",mean_z)


# Finding variance of x, y and z
suma_kv_x = 0
raz_x = []
for i in trenutna[0,:]:
    razlika_x = i - mean_x
    raz_x.append(razlika_x)
    kv_raz_x = pow(razlika_x,2)
    suma_kv_x = suma_kv_x + kv_raz_x
var_x = suma_kv_x / (len(trenutna)-1)
print("Var x: ",var_x)

suma_kv_y = 0
raz_y = []
for j in trenutna[1,:]:
        razlika_y = j - mean_y
        raz_y.append(razlika_y)
        kv_raz_y = pow(razlika_y,2)
        suma_kv_y = suma_kv_y + kv_raz_y
var_y = suma_kv_y / (len(trenutna)-1)
print("Var y: ",var_y)

suma_kv_z = 0
raz_z =[]
for k in trenutna[2,:]:
        razlika_z = k - mean_z
        raz_z.append(razlika_z)
        kv_raz_z = pow(razlika_z,2)
        suma_kv_z = suma_kv_z + kv_raz_z
var_z = suma_kv_z / (len(trenutna)-1)
print("Var z: ",var_z)

# Covariance cov(x,y)
suma_xy = 0
for i,j in zip(raz_x,raz_y):
    proizv_xy = i * j
    suma_xy = suma_xy + proizv_xy
cov_xy = suma_xy/(len(trenutna)-1)
print("Cov(x,y):",cov_xy)

# Covariance cov(x,z)
suma_xz = 0
for i,j in zip(raz_x,raz_z):
    proizv_xz = i * j
    suma_xz = suma_xz + proizv_xz
cov_xz = suma_xz/(len(trenutna)-1)
print("Cov(x,z):",cov_xz)

# Covariance cov(y,z)
suma_yz = 0
for i,j in zip(raz_y,raz_z):
    proizv_yz = i * j
    suma_yz = suma_yz + proizv_yz
cov_yz = suma_yz/(len(trenutna)-1)
print("Cov(y,z):",cov_yz)

mean_vector = [mean_x,mean_y,mean_z]

cov_matrix = ([var_x,cov_xy,cov_xz],
              [cov_xy,var_y,cov_yz],
              [cov_xz,cov_yz,var_z])

cov_matrix = np.array(cov_matrix)

print("Covariance matrix:",cov_matrix)
print(np.shape(cov_matrix))
