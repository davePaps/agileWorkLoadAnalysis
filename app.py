
import pandas as pd
import streamlit as st

# from module import function

from src.generateData import generate_agile_data

print("Hello World");

# df = pd.read_csv("20260609_Data.csv");

df = generate_agile_data();

print(df.describe());
print(df.head());

# manipulate dataframe add
# Group by county hub, return RA

df.groupby("Your County Hub")["RA"].sum();

st.title("Agile Data")
st.write(df.head());
st.dataframe(df);


