import numpy as np
import matplotlib.pyplot as plt
from kosi_hitac_jef_copy import trajectories
from covariance_matrix import cov_matrix,mean_x,mean_y,mean_z

# Example dataset (each row is a data point, each column is a feature)
data = np.array([
    [2.1, 3.5, 1.7],
    [1.9, 3.8, 1.4],
    [3.0, 4.2, 2.0],
    [2.7, 3.6, 1.8]
])

# Step 1: Calculate the mean vector (mean of each feature)
print("Trajectories shape:",np.shape(trajectories))
for i in trajectories:
    i = np.array(i)
    mean_vector = np.mean(i, axis=0)
# print("Mean vector",mean_vector)
mean_vector = [mean_x,mean_y,mean_z]


# Step 3: Calculate the determinant and inverse of the covariance matrix
cov_det = np.linalg.det(cov_matrix)  # Determinant of covariance matrix
cov_inv = np.linalg.inv(cov_matrix)  # Inverse of covariance matrix

# Number of dimensions (features)
k = len(mean_vector)

# Function to calculate the multivariate Gaussian PDF for a single data point
def multivariate_gaussian_pdf(x, mean, cov_inv, cov_det, k):
    # Subtract the mean vector from the data point
    x_minus_mean = x - mean
    # Calculate the exponent term: -0.5 * (x - mean).T @ cov_inv @ (x - mean)
    exponent_term = -0.5 * np.dot(np.dot(x_minus_mean.T, cov_inv), x_minus_mean)
    # Calculate the normalization constant: 1 / sqrt((2*pi)^k * |cov_matrix|)
    norm_constant = 1 / np.sqrt((2 * np.pi) ** k * cov_det)
    # Calculate the PDF value
    pdf_value = norm_constant * np.exp(exponent_term)
    return pdf_value

# Calculate PDF values for each data point in the dataset
pdf_values = [multivariate_gaussian_pdf(x, mean_vector, cov_inv, cov_det, k) for x in trajectories]

# Display the PDF values
print("PDF Values for each data point:", pdf_values)



# Step 3: Plotting the PDF values
plt.figure(figsize=(10, 6))

# Plot the PDF values with markers for visibility
plt.plot(pdf_values, marker='o', linestyle='-', color='b', label='PDF Values')

# Adding labels and titles to the plot
plt.xlabel('Data Point Index')
plt.ylabel('PDF Value')
plt.title('PDF Values of Multivariate Gaussian Distribution')
plt.grid(True)
plt.legend()

# Display the plot
plt.show()

