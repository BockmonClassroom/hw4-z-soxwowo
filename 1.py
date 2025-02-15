# Jitong Zou
# DS5110
# February 15, 2025

import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load the dataset
file_path = "./data/Iris.csv"
data = pd.read_csv(file_path)

# Identify numerical columns (excluding categorical column "Species")
numerical_columns = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]

# Apply Min-Max Scaling (Normalization)
scaler_normalize = MinMaxScaler()
normalize = data.copy()
normalize[numerical_columns] = pd.DataFrame(
    scaler_normalize.fit_transform(normalize[numerical_columns]),
    columns=numerical_columns
)

# Apply StandardScaler (Standardization: mean=0, std=1)
scaler_standard = StandardScaler()
standardize = data.copy()
standardize[numerical_columns] = pd.DataFrame(
    scaler_standard.fit_transform(standardize[numerical_columns]),
    columns=numerical_columns
)

# Ensure the output directory exists
output_folder = "data"
os.makedirs(output_folder, exist_ok=True)

# Save the transformed datasets as CSV files
normalize.to_csv(os.path.join(output_folder, 'normalized_iris_data.csv'), index=False)
standardize.to_csv(os.path.join(output_folder, 'standardized_iris_data.csv'), index=False)

print("Normalization and standardization completed. Files saved in the 'data' folder.")
