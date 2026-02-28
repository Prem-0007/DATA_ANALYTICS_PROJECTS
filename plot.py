import streamlit as stl
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

stl.title("Student Performance Analysis")

connection = sqlite3.connect("students.db")

query = "SELECT * FROM students"
data = pd.read_sql(query, connection)

data["Total"] = data[["DBMS", "PYTHON", "JAVA", "WEB"]].sum(axis=1)
data["Average"] = data["Total"] / 4

stl.subheader("Student Data")
stl.dataframe(data)

stl.subheader("Average Scores")

figure, axes = plt.subplots()
axes.bar(data["Name"], data["Average"]) 
axes.set_xlabel("Student Name")
axes.set_ylabel("Average Score")
axes.set_title("Average Scores of Students")

stl.pyplot(figure)

connection.close()