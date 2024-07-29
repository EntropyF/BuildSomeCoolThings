import numpy as np
from scipy import stats

# Generate two random distributions
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(0, 1.5, 1000)

# Perform the Kolmogorov-Smirnov test
ks_statistic, p_value = stats.ks_2samp(data1, data2)

print(f"KS Statistic: {ks_statistic}")
print(f"P-value: {p_value}")

if p_value < 0.05:
    print("The distributions are significantly different.")
else:
    print("The distributions are not significantly different.")
