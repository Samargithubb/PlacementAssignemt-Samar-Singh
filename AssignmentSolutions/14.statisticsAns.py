import pandas as pd
from scipy.stats import wilcoxon

# Create a dictionary with the data
data = {
    'Participant': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Before therapy': [10, 8, 12, 15, 6, 9, 11, 7, 14, 10],
    'After therapy': [7, 6, 10, 12, 5, 8, 9, 6, 12, 8]
}

# Create a DataFrame from the dictionary
df1 = pd.DataFrame(data)
df1['Difference'] = df1['After therapy'] - df1['Before therapy']
print(df1)

statistic, p_value = wilcoxon(df1['Before therapy'], df1['After therapy'])

# Print the test statistic and p-value
print("Wilcoxon signed-rank test statistic:", statistic)
print("p-value:", p_value)


""" Output
Wilcoxon signed-rank test statistic: 0.0
p-value: 0.001953125
Since the p-value (0.0019) is less than the typical significance level of 0.05, 
we can conclude that the therapy had a significant effect on anxiety levels. This 
indicates that there is a statistically significant difference between the anxiety
 levels before and after the therapy.
"""
