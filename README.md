
COVID-19 Data Analysis
A simple Python data analysis project to visualize COVID-19 case trends using Pandas and Matplotlib.
This project demonstrates beginner-friendly data cleaning, plotting, and time-series analysis.

🚀 Features
Load COVID dataset from CSV

Convert date column & sort records

Plot:

Daily new cases

Total cases over time

Filter data by country

Easy to modify and extend

🛠 Tech Stack
Python

Pandas

Matplotlib

▶️ Run the Project
Install dependencies:

nginx
Copy code
pip install pandas matplotlib
Add your dataset as:

kotlin
Copy code
data.csv
Run:

nginx
Copy code
python analysis.py
Two charts will open for the selected country.

📁 Sample Dataset Format
Your CSV must include:

pgsql
Copy code
date, location, new_cases, total_cases
📁 Folder Structure
kotlin
Copy code
covid19-analysis/
  analysis.py
  data.csv   (you add this)
  README.md
