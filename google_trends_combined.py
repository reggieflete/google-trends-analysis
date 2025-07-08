# --- From 1.nb_5years_search.ipynb ---

#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("data/nb popular 5y CA.csv", skiprows=1)
df.rename(columns={df.columns[0]: "Semana"}, inplace=True)
df["Semana"] = pd.to_datetime(df["Semana"], errors='coerce')
df["Year"] = df["Semana"].dt.year
df_yearly = df.groupby("Year").mean(numeric_only=True).reset_index()

# Plot
plt.figure(figsize=(10, 5))
sns.set_style("whitegrid")
palette = sns.color_palette("tab10", len(df_yearly.columns[1:]))

for idx, col in enumerate(df_yearly.columns[1:]):
    plt.plot(df_yearly["Year"], df_yearly[col], marker="o", label=col, color=palette[idx])

plt.title("New Balance - Yearly Search Interest (5 Years)", fontsize=14, fontweight="bold", color="darkblue")
plt.xlabel("Year", fontsize=12, fontweight="bold")
plt.ylabel("Search Interest", fontsize=12, fontweight="bold")
plt.xticks(fontsize=10, fontweight="bold")
plt.yticks(fontsize=10)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(title="Models", fontsize=9, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3)
plt.tight_layout()
plt.savefig("charts/nb_yearly_trends.png", dpi=300)
plt.show()



# --- From 2.on_5years_search.ipynb ---

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("data/on popular 5y CA.csv", skiprows=1)
df.rename(columns={df.columns[0]: "Semana"}, inplace=True)
df["Semana"] = pd.to_datetime(df["Semana"], errors='coerce')
df["Year"] = df["Semana"].dt.year
df_yearly = df.groupby("Year").mean(numeric_only=True).reset_index()

# Plot
plt.figure(figsize=(10, 5))
sns.set_style("whitegrid")
palette = sns.color_palette("tab10", len(df_yearly.columns[1:]))

for idx, col in enumerate(df_yearly.columns[1:]):
    plt.plot(df_yearly["Year"], df_yearly[col], marker="o", label=col, color=palette[idx])

plt.title("On Running - Yearly Search Interest (5 Years)", fontsize=14, fontweight="bold", color="darkblue")
plt.xlabel("Year", fontsize=12, fontweight="bold")
plt.ylabel("Search Interest", fontsize=12, fontweight="bold")
plt.xticks(fontsize=10, fontweight="bold")
plt.yticks(fontsize=10)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(title="Models", fontsize=9, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3)
plt.tight_layout()
plt.savefig("charts/on_yearly_trends.png", dpi=300)
plt.show()



# --- From 3.nb_18months_search.ipynb ---

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("data/nb popular 5y CA.csv", skiprows=1)
df.rename(columns={df.columns[0]: "Semana"}, inplace=True)
df["Semana"] = pd.to_datetime(df["Semana"], errors='coerce')
df["Month"] = df["Semana"].dt.to_period("M").astype(str)
df_monthly = df.groupby("Month").mean(numeric_only=True).reset_index()
df_last_18 = df_monthly.tail(18)

# Plot
plt.figure(figsize=(10, 5))
sns.set_style("whitegrid")
palette = sns.color_palette("tab10", len(df_last_18.columns[1:]))

for idx, col in enumerate(df_last_18.columns[1:]):
    plt.plot(df_last_18["Month"], df_last_18[col], marker="o", label=col, color=palette[idx])

plt.title("New Balance - Last 18 Months", fontsize=14, fontweight="bold", color="darkblue")
plt.xlabel("Month", fontsize=12, fontweight="bold")
plt.ylabel("Search Interest", fontsize=12, fontweight="bold")
plt.xticks(rotation=45, fontsize=10, fontweight="bold")
plt.yticks(fontsize=10)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(title="Models", fontsize=9, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3)
plt.tight_layout()
plt.savefig("charts/nb_18_months.png", dpi=300)
plt.show()



# --- From 4.on_18months_search.ipynb ---

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("data/on popular 5y CA.csv", skiprows=1)
df.rename(columns={df.columns[0]: "Semana"}, inplace=True)
df["Semana"] = pd.to_datetime(df["Semana"], errors='coerce')
df["Month"] = df["Semana"].dt.to_period("M").astype(str)
df_monthly = df.groupby("Month").mean(numeric_only=True).reset_index()
df_last_18 = df_monthly.tail(18)

# Plot
plt.figure(figsize=(10, 5))
sns.set_style("whitegrid")
palette = sns.color_palette("tab10", len(df_last_18.columns[1:]))

for idx, col in enumerate(df_last_18.columns[1:]):
    plt.plot(df_last_18["Month"], df_last_18[col], marker="o", label=col, color=palette[idx])

plt.title("On Running - Last 18 Months", fontsize=14, fontweight="bold", color="darkblue")
plt.xlabel("Month", fontsize=12, fontweight="bold")
plt.ylabel("Search Interest", fontsize=12, fontweight="bold")
plt.xticks(rotation=45, fontsize=10, fontweight="bold")
plt.yticks(fontsize=10)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(title="Models", fontsize=9, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3)
plt.tight_layout()
plt.savefig("charts/on_18_months.png", dpi=300)
plt.show()



