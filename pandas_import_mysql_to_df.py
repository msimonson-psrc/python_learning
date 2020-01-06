#  https://pythondata.com/quick-tip-sqlalchemy-for-mysql-and-pandas/

import pandas as pd
import sqlalchemy as sql

connect_string = 'mysql://root:saluki23_saluki23MHS@localhost/2018_by_working_snoh'
sql_engine = sql.create_engine(connect_string)

query = "select * from parcels"
df = pd.read_sql_query(query, sql_engine)

print(df.head())

#Now transitioning to https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/



