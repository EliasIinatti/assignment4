import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    return pd.read_csv("titanic.csv")

df = load_data()

st.title("🚢 Titanic Data Dashboard")
st.write("Explore key statistics from the Titanic dataset!")

st.sidebar.header("Filters")
selected_class = st.sidebar.selectbox("Select Passenger Class", ["All"] + sorted(df['Pclass'].unique().tolist()))

filtered_df = df if selected_class == "All" else df[df['Pclass'] == selected_class]

st.subheader("Passenger Data Table")
st.dataframe(filtered_df)

st.subheader("Key Statistics")
st.write(f"Total Passengers: {len(filtered_df)}")
st.write(f"Survival Rate: {filtered_df['Survived'].mean() * 100:.2f}%")

st.subheader("Survival Rate by Class")
fig, ax = plt.subplots()
survival_rates = df.groupby('Pclass')['Survived'].mean()
survival_rates.plot(kind='bar', ax=ax, color=['blue', 'orange', 'green'])
ax.set_ylabel("Survival Rate")
st.pyplot(fig)