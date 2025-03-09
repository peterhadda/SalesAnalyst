USE DataAnalyst;
DROP TABLE IF EXISTS MobileSales;

CREATE TABLE MobileSales (
    Company_Name VARCHAR(100),
    Model_Name VARCHAR(255),
    Mobile_Weight VARCHAR(50),
    RAM VARCHAR(50),
    Front_Camera VARCHAR(50),
    Back_Camera VARCHAR(50),
    Processor VARCHAR(100),
    Battery_Capacity VARCHAR(50),
    Screen_Size VARCHAR(50),
    Launched_Price_Pakistan VARCHAR(50),
    Launched_Price_India VARCHAR(50),
    Launched_Price_China VARCHAR(50),
    Launched_Price_USA VARCHAR(50),
    Launched_Price_Dubai VARCHAR(50),
    Launched_Year INT
);


--Changer de USD a Numerique--
UPDATE MobileSales
SET Launched_Price_USA=REPLACE(Launched_Price_USA,'USD','')

SELECT TOP 5 Model_Name, Company_Name, Launched_Price_USA
FROM MobileSales
ORDER BY CAST(REPLACE(LTRIM(RTRIM(Launched_Price_USA)), ',', '') AS DECIMAL(10,2)) DESC;








