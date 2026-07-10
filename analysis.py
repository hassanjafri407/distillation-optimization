import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from kneed import KneeLocator
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "data" / "reflux_sensitivity.csv"
df = pd.read_csv(csv_path)
df.columns = df.columns.str.replace(r"[\n]", " ", regex=True).str.strip()
df = df.dropna(axis=1, how="all")



df = df[
    [
        "VARY   1 B2       COL-SPEC MOLE-RR",
        "REBDUTY      CAL/SEC",
        "CONDDUTY     CAL/SEC",
        "BPURITY",
        "TPURITY"
    ]
]


df["TOTAL_ENERGY      CAL/SEC"] = (
    abs(df["REBDUTY      CAL/SEC"])
    + abs(df["CONDDUTY     CAL/SEC"])
)


plt.figure(figsize=(8,5))

plt.plot(
    df["BPURITY"],
    df["TOTAL_ENERGY      CAL/SEC"],
    marker="o"
)

plt.xlabel("Benzene Purity")
plt.ylabel("Total Energy (cal/s)")
plt.title("Energy Consumption vs Benzene Purity")

plt.grid(True)

plt.show()

df["SLOPE"] = (
    df["TOTAL_ENERGY      CAL/SEC"].diff()
    /
    df["BPURITY"].diff()
)

df


knee = KneeLocator(
    df["BPURITY"],
    df["TOTAL_ENERGY      CAL/SEC"],
    curve="convex",
    direction="increasing"
)

print("The knee point:", knee.knee)

plt.figure(figsize=(8,5))

plt.plot(
    df["BPURITY"],
    df["TOTAL_ENERGY      CAL/SEC"],
    marker="o"
)

plt.scatter(
    knee.knee,
    knee.knee_y,
    marker= "s",
    s=200,
    label="Optimal Point"
)

plt.xlabel("Benzene Purity")
plt.ylabel("Total Energy (cal/s)")
plt.legend()

plt.grid(True)

plt.show()