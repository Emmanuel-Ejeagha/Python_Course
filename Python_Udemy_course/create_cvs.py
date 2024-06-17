#!/usr/bin/pytho
# Generate 50 rows and five columns of data

import numpy as np
new_data = np.random.random((50, 5))
create = np.savetxt("main.csv", new_data, fmt="%.2f", delimiter=",", header="H1, H2, H3, H4, H5")

# Read CSV File
reading_csv = np.loadtxt("main.csv", delimiter=",")
read = reading_csv[:5, :]
print(read)
