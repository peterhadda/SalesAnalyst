import pandas as pd
import seaborn as sns
import matplotlib
from matplotlib import pyplot as plt
from sqlalchemy import create_engine, text


matplotlib.use('Agg')


file_path = "Mobiles Dataset (2025).csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")


df.columns = [
    "Company_Name",
    "Model_Name",
    "Mobile_Weight",
    "RAM",
    "Front_Camera",
    "Back_Camera",
    "Processor",
    "Battery_Capacity",
    "Screen_Size",
    "Launched_Price_Pakistan",
    "Launched_Price_India",
    "Launched_Price_China",
    "Launched_Price_USA",
    "Launched_Price_Dubai",
    "Launched_Year"
]


df["Launched_Price_USA"] = df["Launched_Price_USA"].str.replace("USD ", "", regex=False)
df["Launched_Price_USA"] = df["Launched_Price_USA"].str.replace(",", "", regex=False)
df["Launched_Price_USA"] = pd.to_numeric(df["Launched_Price_USA"], errors="coerce")  # Convert to float

try:

    server = 'localhost'
    database = 'DataAnalyst'
    username = 'SA'
    password = 'Password123'
    driver = 'ODBC Driver 17 for SQL Server'

    engine = create_engine(f"mssql+pyodbc://{username}:{password}@{server}:1433/{database}?driver={driver}")


    with engine.connect() as conn:
        conn.execute(text("DROP TABLE IF EXISTS MobileSales"))
        conn.commit()  # ✅ Ensure the command is committed


    df.to_sql("MobileSales", con=engine, if_exists="append", index=False)

    print("Data imported successfully!")


    query = """
    SELECT TOP 5 Model_Name, Company_Name, 
           CAST(REPLACE(LTRIM(RTRIM(Launched_Price_USA)), ',', '') AS DECIMAL(10,2)) AS Price_USD
    FROM MobileSales
    ORDER BY Price_USD DESC;
    """


    df = pd.read_sql(query, engine)


    print(df)


    plt.figure(figsize=(10, 6))
    sns.barplot(x="Price_USD", y="Model_Name", hue="Company_Name", data=df, palette="coolwarm")


    plt.title("Top 5 Most Expensive Phones", fontsize=14)
    plt.xlabel("Price in USD", fontsize=12)
    plt.ylabel("Phone Model", fontsize=12)
    plt.legend(title="Company")


    plt.savefig("top_phones.png")

    print("Plot saved successfully!")

except Exception as e:
    print("Erreur lors de l'exécution de la requête:", e)





