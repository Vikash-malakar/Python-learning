import numpy as np

rng = np.random.default_rng(42)

data = rng.integers(10, 100, size=(6, 5))

# Boolean masking
high_values = data[data > 70]

# Multiple conditions
filtered = data[(data > 30) & (data < 70)]

# Fancy indexing
selected_rows = data[[0, 2, 4]]
selected_columns = data[:, [1, 3]]

# Replace values using condition
cleaned_data = np.where(data < 30, 0, data)

print("Original Data:\n", data)
print("\nHigh Values:", high_values)
print("\nFiltered Values:", filtered)
print("\nSelected Rows:\n", selected_rows)
print("\nSelected Columns:\n", selected_columns)
print("\nCleaned Data:\n", cleaned_data)