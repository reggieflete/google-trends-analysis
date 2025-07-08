
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

st.set_page_config(page_title="Google Trends Dashboard", layout="wide")
st.title("📊 Google Trends Analysis")

# All code below was generated from notebooks
# --- From 1.nb_5years_search.ipynb ---

#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import plotly.express as px
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
    st.line_chart(df_yearly["Year"], df_yearly[col], marker="o", label=col, color=palette[idx])


plt.xticks(fontsize=10, fontweight="bold")
plt.yticks(fontsize=10)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(title="Models", fontsize=9, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3)
plt.tight_layout()
plt.savefig("charts/nb_yearly_trends.png", dpi=300)




# --- From 2.on_5years_search.ipynb ---

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
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
    st.line_chart(df_yearly["Year"], df_yearly[col], marker="o", label=col, color=palette[idx])


plt.xticks(fontsize=10, fontweight="bold")
plt.yticks(fontsize=10)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(title="Models", fontsize=9, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3)
plt.tight_layout()
plt.savefig("charts/on_yearly_trends.png", dpi=300)




# --- From 3.nb_18months_search.ipynb ---

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
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
    st.line_chart(df_last_18["Month"], df_last_18[col], marker="o", label=col, color=palette[idx])




plt.xticks(rotation=45, fontsize=10, fontweight="bold")
plt.yticks(fontsize=10)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(title="Models", fontsize=9, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3)
plt.tight_layout()
plt.savefig("charts/nb_18_months.png", dpi=300)




# --- From 4.on_18months_search.ipynb ---

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
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
    st.line_chart(df_last_18["Month"], df_last_18[col], marker="o", label=col, color=palette[idx])




plt.xticks(rotation=45, fontsize=10, fontweight="bold")
plt.yticks(fontsize=10)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(title="Models", fontsize=9, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3)
plt.tight_layout()
plt.savefig("charts/on_18_months.png", dpi=300)




