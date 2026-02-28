# Student Performance Analysis

A simple **Python & Streamlit project** to analyze and visualize student performance data using SQLite and interactive plots.

---

## Project Structure



├─ db.py # Script to create and populate the SQLite database
├─ plot.py # Streamlit app for visualizing student performance
├─ requirements.txt # List of Python dependencies
└─ students.db # SQLite database file (optional for sharing)


---

## Features

- Creates a SQLite database for storing student data (`students.db`)
- Interactive visualization of student performance using Streamlit
- Easy to install and run locally

---

## Setup Instructions

1. **Clone the repository**


git clone <your-github-repo-url>

Create a virtual environment (optional but recommended)

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

##Install dependencies

pip install -r requirements.txt

Create the database

python db.py

Run the Streamlit app

python -m streamlit run plot.py

Visit http://localhost:8501 in your browser to see the app.
