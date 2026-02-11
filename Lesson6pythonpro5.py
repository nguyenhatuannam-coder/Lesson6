import pandas as pd
import streamlit as st

st.title("Bài 6: Các phương pháp làm sạch dữ liệu")


df = pd.read_csv("data5.6_1.csv")

st.subheader("Dữ liệu ban đầu")
st.dataframe(df)


st.subheader("Kiểu dữ liệu các cột")
st.write(df.dtypes)


st.subheader("Dữ liệu trùng lặp")
st.write("Số dòng trùng lặp:", df.duplicated().sum())


df = df.drop_duplicates()


st.subheader("Giá trị thiếu trước khi xử lý")
st.write(df.isnull().sum())


df["gender"].fillna(df["gender"].mode()[0], inplace=True)
df["lunch"].fillna(df["lunch"].mode()[0], inplace=True)

# Điền giá trị thiếu cho cột số bằng median
df["math score"].fillna(df["math score"].median(), inplace=True)
df["reading score"].fillna(df["reading score"].median(), inplace=True)
df["writing score"].fillna(df["writing score"].median(), inplace=True)

# Kiểm tra giá trị thiếu sau khi xử lý
st.subheader("Giá trị thiếu sau khi xử lý")
st.write(df.isnull().sum())

# Hiển thị dữ liệu sau khi làm sạch
st.subheader("Dữ liệu sau khi làm sạch")
st.dataframe(df)
