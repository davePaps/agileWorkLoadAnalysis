
import pandas as pd
import streamlit as st
print("Hello World");

df = pd.read_csv("20260609_Data.csv");
print(df.describe());
print(df.head());

# manipulate dataframe
# Group by county hub, return RA

df.groupby("Your County Hub")["RA"].sum();

st.title("Agile Data")
st.write(df.head());
st.dataframe(df);


