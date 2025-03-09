📱 Mobile Price Analysis & Visualization
This project analyzes mobile phone data from a CSV dataset and identifies the top 5 most expensive phones. It then generates a bar chart visualization using Python.

📂 Files Overview
Mobiles Dataset (2025).csv – Contains mobile phone specifications and launch prices in multiple countries.
admin.py – The main script that processes the data, imports it into an SQL database, and generates a visualization.
DataAnalyst.sql – SQL script related to the data analysis process.
top_phones.png – The generated bar chart of the most expensive phones.
🛠️ How It Works
Data Preprocessing:

The script reads the CSV dataset.
It renames columns for better readability.
Launch prices are cleaned and converted to numerical format.
Database Handling:

The processed data is imported into an SQL database (DataAnalyst).
The script connects using SQLAlchemy and stores data in the MobileSales table.
Query Execution:

A SQL query selects the top 5 most expensive phones based on their launch price in the USA.
Data Visualization:

The selected top 5 phones are visualized using a horizontal bar chart (top_phones.png).
The chart highlights the company names using a color-coded legend.
🔧 Setup & Execution
Requirements
Python 3.x
Required Libraries:
nginx
Copy
Edit
pandas
seaborn
matplotlib
sqlalchemy
pyodbc
Microsoft SQL Server with ODBC Driver 17 for SQL Server.
Steps to Run:
Install dependencies:
nginx
Copy
Edit
pip install pandas seaborn matplotlib sqlalchemy pyodbc
Ensure you have an SQL Server running locally with a database named DataAnalyst.
Modify database credentials in admin.py if needed.
Run the script:
nginx
Copy
Edit
python admin.py
The output will be a PNG visualization (top_phones.png) showing the most expensive phones.
📊 Sample Output
The top_phones.png file contains a bar chart ranking the top 5 most expensive phones by their price in USD.
