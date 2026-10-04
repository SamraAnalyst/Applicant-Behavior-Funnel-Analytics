import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("---- Step 1: Ingesting Raw Application Flow Logs ---")

funnel_data = {
    "Web_Page_Storage": ["1. Website Visit", "2. Account Created", "3. Form Filled", "4. Tasks Submitted"],
    "User_Count": [500, 350, 150, 80]
}
df = pd.DataFrame(funnel_data)

print("\nIntial User Conversion Funnel Matrix:")
print(df)

print("\n---- Step 2: Running Conversion Pipeline Analytics ---")

intial_visitors = df.loc[0, "User_Count"]
df["Conversion_Rata (%)"] = np.round((df["User_Count"] / intial_visitors) * 100, 1)

print("\nUpdated Conversion Funnel Reporting Matrix:")
print(df)

print("\n--- Step 3: Generating Visual Funnel Bottleneck Charts ---")

plt.figure(figsize=(9, 4.5))
plt.barh(df["Web_Page_Storage"], df["User_Count"], color=["#4A4644", "#8B8589", "#D2B48C", "#F5F5DC"], edgecolor="black")

plt.gca().invert_yaxis()

plt.title("Applicant Operational Conversion Funnel & Bottlenecks Audit", fontsize=11, fontweight="bold")
plt.xlabel("Total Live Active Users Count")
plt.grid(axis= 'x', linestyle='--', alpha=0.6)
plt.tight_layout()

print("desplaying final user funnel tracking visualization dashboards...")
plt.show()
