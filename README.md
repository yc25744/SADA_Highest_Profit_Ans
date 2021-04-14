# Approach to problem

1. Read the problem and find which programing language to choose

2. Decided to use **Python**

3. Use **Jupyternotebook** to start the code and convert to .py after

4. For the Part 3, I could use basic **ETL** skill to connect with postgresql | Bonus answer included

5. Please check my Answer.ipynb jupyter notebook. It shows all of the explnations and steps

6. Made **requirements.txt** for python library that I have on my computer. Please use virtualenv and install my python libraries

7. **data2.json** file will be located at resources folder

* PS. Sometimes jupyternote book does not display on github page due to github bug...
* Then please use https://nbviewer.jupyter.org/
* My .ipynb link: https://nbviewer.jupyter.org/github/yc25744/SADA_Highest_Profit_Ans/blob/main/Highest_Profit_Ans/Answer.ipynb


## Challenge: highest-profit

* First read the `Basic rules for challenges` (https://github.com/bobbae/gcp/blob/main/challenges/README.md).

* Summary: Read a CSV file containing corporate profits over the years and create JSON format data and look for highest profit values in the data.

## Part 1

* Download the data file at https://gist.github.com/bobbae/b4eec5b5cb0263e7e3e63a6806d045f2 as "raw" and read the file into a program memory.  

* The data file is in CSV format, the
comma separated values format.  

* Once the data is read into memory in your program, print out how many rows of the data is in the CSV data. This is your first printed answer.

* For each row, there are columns.  One of the columns is the "profit".  The data in this profit column
are not always valid.  Sometimes the data is non-numeric.  Remove all rows with 'profit' that is not numerical value. Then
print out how many rows of data are left, after removing all the rows with invalid non-numeric profit column data.  This is your second printed answer.

## Part 1 Solution

1. First bring the URL CSV into python dataframe by using pandas

2. Find the total rows of this df by using the "len" and print the result

```python
Total_row_profit = len(df)
```

3. Drop non-numeric value by using erros= "coerce" 

```python
df['profit'] = pd.to_numeric(df['profit'],errors='coerce')
cleaned_df=df.dropna(subset=['profit'])
```
4. Print the second answer

## Part 2

* You can now convert the content your read into memory in your program in Part 1 into JSON format and write it out to another file called `data2.json` which should only contain rows of data that have the valid numeric profit values. Each row in the Array should contain data columns like year, rank, company, revenue, and profit.

* Order the data based on the profit value.  Print the top 20 rows with the highest profit values. This is your third printed answer.

## Part 2 Solution

1. Convert df to json file and save into local directory

```python
cleaned_df.to_json("data2.json")"
```

2. Bring the Json file and convert into pandas df

```python
json_df = pd.DataFrame.from_dict(json, orient="columns")
```

3. Find the Top 20 profit values by using nlargest

```python
json_df = print(json_df.nlargest(20,['profit']))
```

## Part 3

* Check and make sure your solution produces three answers as printed output. And a file called `data2.json` is produced.

* Think about how you may do this using SQL.  We may discuss other ways to solve this problem.  You don't need to write anything down, just think about different ways.

## Part 3 Solution

1. Use sqlalchemy and connect python with local postgres server

```python
from sqlalchemy import create_engine
rds_connection_string = "postgres:password@localhost:5432/SADA"
engine = create_engine(f'postgresql://{rds_connection_string}')
```

2. I didn't connect postgres to server such as AWS RDS or GCP Cloud SQL

3. Login to pgadmin4 to create table first

```python
CREATE TABLE highest_profit (
	Year int,
	Rank int,
	Company TEXT,
	revenue float,
	profit float
)
```
4. Insert the df into database by using to_sql

```python
json_df.to_sql(name='highest_profit', con=engine, if_exists='append', index=False)
```

5. Write and run sql query that can find the TOP 20 profit

```python
pd.read_sql_query('SELECT DISTINCT * from highest_profit ORDER by profit DESC LIMIT 20', con=engine)
```
