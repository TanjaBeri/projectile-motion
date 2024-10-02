import numpy as np
from kosi_hitac_sa_gausom import trenutna
from covariance_matrix import mean_vector,cov_matrix

# Example dataset (each row is a data point, each column is a feature)
data = np.array([
    [2.1, 3.5, 1.7],
    [1.9, 3.8, 1.4],
    [3.0, 4.2, 2.0],
    [2.7, 3.6, 1.8]
])

# Step 1: Calculate the mean vector (mean of each feature)
# mean_vector = np.mean(trenutna)

# Step 2: Calculate the covariance matrix
# cov_matrix = np.cov(trenutna, rowvar=False)  # rowvar=False treats rows as observations

# Step 3: Calculate the determinant and inverse of the covariance matrix
cov_det = np.linalg.det(cov_matrix)  # Determinant of covariance matrix
cov_inv = np.linalg.inv(cov_matrix)  # Inverse of covariance matrix

# Number of dimensions (features)
k = 3

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
# pdf_values = [multivariate_gaussian_pdf(x, mean_vector, cov_inv, cov_det, k) for x in trenutna]

# Display the PDF values
print("PDF Values for each data point:")
print("Kraj")

n = 0
pdf_values = []
while n < trenutna.size/len(trenutna):
    pojedinacno_xyz = trenutna[:,n]
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

print("Sve pdf values:",pdf_values)   