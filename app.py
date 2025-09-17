import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/metadata.csv")
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

# Title
st.title("📊 CORD-19 Data Explorer")
st.write("A simple app to explore COVID-19 research papers using the metadata.csv dataset.")

# Year filter
year_min, year_max = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select Year Range", year_min, year_max, (2020, 2021))
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Publications by Year
st.subheader("Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax)
st.pyplot(fig)

# Top Journals
st.subheader("Top Journals")
top_journals = filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax)
st.pyplot(fig)

# Sample data
st.subheader("Sample Data")
st.write(filtered[['title', 'authors', 'publish_time', 'journal']].head(10))
