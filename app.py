
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('fastfood_updated.csv')

# Compute ratio if not already present
if 'protein_per_cal' not in df.columns:
    df['protein_per_cal'] = df['protein'] / df['calories']

# Title
st.title("🍔 Fast Food Nutrition Explorer")

# Sidebar for chart selection
chart = st.sidebar.selectbox("Choose a chart", [
    "Calories Distribution",
    "Fat vs Carbohydrates",
    "Average Fat by Restaurant",
    "Protein per Calorie Ratio"
])

sns.set(style="whitegrid")

# Show selected chart
if chart == "Calories Distribution":
    fig, ax = plt.subplots()
    sns.histplot(df['calories'], bins=15, kde=True, color='orange', ax=ax)
    ax.set_title("Calories Distribution")
    st.pyplot(fig)

elif chart == "Fat vs Carbohydrates":
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='total_fat', y='total_carb', alpha=0.6, ax=ax)
    ax.set_title("Fat vs Carbohydrates")
    st.pyplot(fig)

elif chart == "Average Fat by Restaurant":
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df, x='restaurant', y='total_fat', ci='sd', palette='coolwarm', ax=ax)
    ax.set_title("Average Fat by Restaurant")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

elif chart == "Protein per Calorie Ratio":
    fig, ax = plt.subplots()
    sns.histplot(df['protein_per_cal'], bins=15, kde=True, color='seagreen', ax=ax)
    ax.set_title("Protein per Calorie Ratio")
    st.pyplot(fig)
