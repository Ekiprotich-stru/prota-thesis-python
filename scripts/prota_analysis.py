# scripts/prota_waste_study.py
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("plots", exist_ok=True)

# Sample dataset (replace with your Prota CSV later)
data = {
    "Building": ["A", "B", "C", "D"],
    "Baseline_Reinf_t": [120, 150, 180, 210],
    "Optimized_Reinf_t": [105, 135, 160, 190]
}

df = pd.DataFrame(data)
df["Waste_Reduction_%"] = ((df["Baseline_Reinf_t"] - df["Optimized_Reinf_t"]) / df["Baseline_Reinf_t"]) * 100
print("\nReinforcement and Waste Reduction Summary:\n")
print(df)

# Bar chart - baseline vs optimized
ax = df.plot(x="Building", y=["Baseline_Reinf_t", "Optimized_Reinf_t"], kind="bar", rot=0)
ax.set_title("Baseline vs Optimized Reinforcement (tonnes)")
ax.set_ylabel("Tonnes")
plt.tight_layout()
plt.savefig("plots/reinforcement_comparison2.png")
plt.close()

# Bar chart - waste reduction %
ax = df.plot(x="Building", y="Waste_Reduction_%", kind="bar", rot=0, color="green")
ax.set_title("Waste Reduction Percentage")
ax.set_ylabel("% Reduction")
plt.tight_layout()
plt.savefig("plots/waste_reduction2.png")
plt.close()

# Line plot - trend
ax = df.plot(x="Building", y=["Baseline_Reinf_t", "Optimized_Reinf_t"], marker="o")
ax.set_title("Trend of Reinforcement per Building")
ax.set_ylabel("Tonnes")
plt.tight_layout()
plt.savefig("plots/reinforcement_trend.png")
plt.close()

# Line plot - waste trend
ax = df.plot(x="Building", y="Waste_Reduction_%", marker="o", color="red")
ax.set_title("Trend of Waste Reduction per Building")
ax.set_ylabel("% Reduction")
plt.tight_layout()
plt.savefig("plots/waste_trend.png")
plt.close()


