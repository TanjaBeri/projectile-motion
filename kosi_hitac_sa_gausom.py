import numpy as np
import matplotlib.pyplot as plt
from moving_average_filter import X_kol1,Y_kol1,Z_kol1
from moving_average_filter import X_list,Y_list,Z_list


g = 9810
dt= 0.01

n_samples = len(X_list)
# time of flight
T = n_samples/100

def racunanje_svih_traj(g,dt,T,samples):

    i = 0
    trajectories = []
    for i in range(1,samples):
        # ubacivanje svih prethodnih koord.
        x = X_list[:i]
        y = Y_list[:i]
        z = Z_list[:i]
        t = i*dt
        # ubacivanje tacka u trenutnu i prethodnu koord.
        x0, y0, z0 = X_list[i-1], Y_list[i-1],Z_list[i-1]       
        x1, y1, z1 = X_list[i],Y_list[i],Z_list[i]

        # izracunavanje pocetnih brzina
        v0x = (x1 - x0) / dt
        v0y = (y1 - y0) / dt
        v0z = (z1 - z0) / dt

        while t < T:
            x_novo = x0 + v0x * (t+dt)
            x.append(x_novo)
            y_novo = y0 + v0y * (t+dt)
            y.append(y_novo)
            z_novo = z0 + v0z * (t+dt) - 0.5 * g * (t+dt)**2
            z.append(z_novo)

            t += dt

        trajectories.append([x,y,z])

    trajectories = np.array(trajectories)
    return trajectories

def jedna_Traj(trajectories,window):
    trenutna_traj = trajectories[0,:,:] # pristupam samo prvoj trajektoriji, u x,y,z osi i svim tackama prve trajektorije
    return trenutna_traj

def druga_Traj(trajectories,window):
    trenutna_traj = trajectories[1,:,:] # pristupam samo prvoj trajektoriji, u x,y,z osi i svim tackama prve trajektorije
    return trenutna_traj

def covariance_matrix(trajektorija):
    # Finding means of x, y and z
    suma_x = 0
    for i in trajektorija[0,:]:
        # print(i)
        suma_x = suma_x + int(i)
    mean_x = suma_x/ len(trajektorija)
    print("Mean_x:",mean_x)

    suma_y = 0
    for j in trajektorija[1,:]:
        # print(i)
        suma_y = suma_y + int(j)
    mean_y = suma_y/ len(trajektorija)
    print("Mean_y:",mean_y)

    suma_z = 0
    for k in trajektorija[2,:]:
        # print(i)
        suma_z = suma_z + int(k)
    mean_z = suma_z/ len(trajektorija)
    print("Mean_x:",mean_z)


    # Finding variance of x, y and z
    suma_kv_x = 0
    raz_x = []
    for i in trajektorija[0,:]:
        razlika_x = i - mean_x
        raz_x.append(razlika_x)
        kv_raz_x = pow(razlika_x,2)
        suma_kv_x = suma_kv_x + kv_raz_x
    var_x = suma_kv_x / (len(trajektorija)-1)
    print("Var x: ",var_x)

    suma_kv_y = 0
    raz_y = []
    for j in trajektorija[1,:]:
            razlika_y = j - mean_y
            raz_y.append(razlika_y)
            kv_raz_y = pow(razlika_y,2)
            suma_kv_y = suma_kv_y + kv_raz_y
    var_y = suma_kv_y / (len(trajektorija)-1)
    print("Var y: ",var_y)

    suma_kv_z = 0
    raz_z =[]
    for k in trajektorija[2,:]:
            razlika_z = k - mean_z
            raz_z.append(razlika_z)
            kv_raz_z = pow(razlika_z,2)
            suma_kv_z = suma_kv_z + kv_raz_z
    var_z = suma_kv_z / (len(trajektorija)-1)
    print("Var z: ",var_z)

    # Covariance cov(x,y)
    suma_xy = 0
    for i,j in zip(raz_x,raz_y):
        proizv_xy = i * j
        suma_xy = suma_xy + proizv_xy
    cov_xy = suma_xy/(len(trajektorija)-1)
    print("Cov(x,y):",cov_xy)

    # Covariance cov(x,z)
    suma_xz = 0
    for i,j in zip(raz_x,raz_z):
        proizv_xz = i * j
        suma_xz = suma_xz + proizv_xz
    cov_xz = suma_xz/(len(trajektorija)-1)
    print("Cov(x,z):",cov_xz)

    # Covariance cov(y,z)
    suma_yz = 0
    for i,j in zip(raz_y,raz_z):
        proizv_yz = i * j
        suma_yz = suma_yz + proizv_yz
    cov_yz = suma_yz/(len(trajektorija)-1)
    print("Cov(y,z):",cov_yz)

    mean_vector = [mean_x,mean_y,mean_z]

    cov_matrix = ([var_x,cov_xy,cov_xz],
                [cov_xy,var_y,cov_yz],
                [cov_xz,cov_yz,var_z])

    cov_matrix = np.array(cov_matrix)

    return cov_matrix,mean_vector

def multivariate_Gauss(trajektorija,mean_vector,covariance):
    cov_det = np.linalg.det(covariance)  # Determinant of covariance matrix
    cov_inv = np.linalg.inv(covariance)
    k = 3
    n = 0
    pdf_values = []
    while n < trajektorija.size/len(trajektorija):
        pojedinacno_xyz = trajektorija[:,n]
        # print(trenutna[:,n])

        x_minus_mean = pojedinacno_xyz - mean_vector

        # Calculate the exponent term: -0.5 * (x - mean).T @ cov_inv @ (x - mean)
        exponent_term = -0.5 * np.dot(np.dot(x_minus_mean.T, cov_inv), x_minus_mean)

        # Calculate the normalization constant: 1 / sqrt((2*pi)^k * |cov_matrix|)
        norm_constant = 1 / np.sqrt((2 * np.pi) ** k * cov_det)

        # Calculate the PDF value
        pdf_value = norm_constant * np.exp(exponent_term)

        pdf_values.append(pdf_value)
        n = n + 1

    return pdf_values


trajectories = racunanje_svih_traj(g,dt,T,n_samples)
trenutna = jedna_Traj(trajectories,15)
cov_matrix1, mean_vector1 = covariance_matrix(trenutna)
multivar_gaus1 = multivariate_Gauss(trenutna,mean_vector1,cov_matrix1)

print(trenutna)
print(multivar_gaus1)
# print(trajectories)
# print(len(x),len(y),len(z))
print("'Kraj")
