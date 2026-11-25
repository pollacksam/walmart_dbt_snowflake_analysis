import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
# import botocore
# import boto3
from snowflake_connector import conn

# .venv needs to be created in your folder before running this Python script

# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Execute a SQL query to retrieve data from the DATE_DIM table
sql = """SELECT F.STORE_ID, D.IS_HOLIDAY, SUM(F.STORE_WEEKLY_SALES) AS TOTAL_SALES
    FROM WALMART_DB.SNAPSHOTS.FACT_SNAPSHOT F
    JOIN WALMART_DB.GOLD.DATE_DIM D ON F.DATE_ID = D.DATE_ID
    GROUP BY F.STORE_ID, D.IS_HOLIDAY
    ORDER BY F.STORE_ID, D.IS_HOLIDAY LIMIT 4;"""

cur.execute(sql)

# Fetch the results set from the cursor and deliver it as a pandas DataFrame
df = cur.fetch_pandas_all()

# Use seaborn to create a histogram of the data, with STORE_DATE on the x-axis, STORE_WEEKLY_SALES on the y-axis, and DEPT_ID as the hue.
sns.set_theme(style="whitegrid")
fig, axs = plt.subplots(5, 5, figsize=(7, 5))
sns.despine(fig)

# The histogram will be stacked and use a pastel color palette. 
sns.histplot(df, x="STORE_ID",
             y="TOTAL_SALES",
             hue="IS_HOLIDAY",
             binwidth=3,
            #  multiple="stack",
             palette="pastel",
             edgecolor=".3",
             linewidth=.5)

# The x-axis will be formatted to display dates in the "YYYY-MM-DD" format. 
# ax.xaxis.set_major_formatter(mpl.dates.DateFormatter("%Y-%m-%d"))

# Finally, the plot will be displayed using plt.show().
plt.show()

# SQL Select specific columns and print the first values from each (i.e., first row).
# col1, col2 = conn.cursor().execute("SELECT DATE_ID, IS_HOLIDAY FROM WALMART_DB.GOLD.DATE_DIM").fetchone()
# print('{0}, {1}'.format(col1, col2))

# SQL Select specific columns and print the first 100 values from each (i.e., first 100 rows) using for loop.
# for (col1, col2) in conn.cursor().execute("SELECT DATE_ID, IS_HOLIDAY FROM WALMART_DB.GOLD.DATE_DIM LIMIT 100"):
#     print('{0}, {1}'.format(col1, col2))

# conn.close()