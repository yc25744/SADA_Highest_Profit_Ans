import pandas as pd
import io
import requests
import numpy as np

#URL CSV to dataframe
url="https://gist.githubusercontent.com/bobbae/b4eec5b5cb0263e7e3e63a6806d045f2/raw/279b794a834a62dc108fc843a72c94c49361b501/data.csv"
response=requests.get(url).content
data_file=pd.read_csv(io.StringIO(response.decode('utf-8')))

df=data_file.dropna(how='any')
df.count()

# Found the total rows of this df
Total_row_profit = len(df)
print(f"First Answer: There are total number of {Total_row_profit} rows")
print("---------------------------------------------------------------------")

#rename Profit(in millions) to profit
df=df.rename(columns={'Profit (in millions)' : 'profit', 'Revenue (in millions)' : 'revenue'})

# Drop non-numeric value by using coerce 
df['profit'] = pd.to_numeric(df['profit'],errors='coerce')
cleaned_df=df.dropna(subset=['profit'])

#Print total number of cleaned rows
Cleaned_Total_row_profit = len(cleaned_df)
print(f"Second Answer: There are total number of cleaned {Cleaned_Total_row_profit} rows")

#Save DF as Json file named "data2.json"
cleaned_df.to_json("resources/data2.json")

import json
import os
from pandas.io.json import json_normalize 

# Read Jsonfile
filepath = os.path.join("resources/data2.json")
with open(filepath) as jsonfile:
    json = json.load(jsonfile)

#Json to dataframe
json_df = pd.DataFrame.from_dict(json, orient="columns")

# In order to remove index column json_df.set_index('Year', inplace=True)
print("---------------------------------------------------------------------")
print("Third Answer")
print(json_df.nlargest(20,['profit']))

#writing sql
from sqlalchemy import create_engine

#Log into pgadmin and make table by using SQL quiry
rds_connection_string = "postgres:chldudwnd818@localhost:5432/SADA"
engine = create_engine(f'postgresql://{rds_connection_string}')

#Check the table
engine.table_names()

#Use pandas to load dataframe into database
json_df.to_sql(name='highest_profit', con=engine, if_exists='append', index=False)

# Run the squiry quiry and find the TOP 20 profit 
bonus = pd.read_sql_query('SELECT DISTINCT * from highest_profit ORDER by profit DESC LIMIT 20', con=engine)
print("---------------------------------------------------------------------")
print("BONUS Answers by using SQL")
print(bonus)