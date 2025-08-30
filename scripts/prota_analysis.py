import pandas as pd
import matplotlib.pyplot as plt

# Fake sample dataset
data = {
    "Building": ["A", "B", "C"],
    "Baseline_Reinf_t": [120, 150, 180],
    "Optimized_Reinf_t": [105, 135, 160]
}

df = pd.DataFrame(data)

# Calculate waste reduction
df["Waste_Reduction_%"] = ((df["Baseline_Reinf_t"] - df["Optimized_Reinf_t"]) / df["Baseline_Reinf_t"]) * 100

print(df)

# Plot reinforcement comparison
df.plot(x="Building", y=["Baseline_Reinf_t", "Optimized_Reinf_t"], kind="bar")
plt.title("Baseline vs Optimized Reinforcement (tonnes)")
plt.ylabel("Tonnes")
plt.show()
