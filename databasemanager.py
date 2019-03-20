import sqlite3
import sys
from genremapper import val_input
#remember to check dbname when connecting to database

def runsqlquery(database_name1,query):
    '''
    Docstring:
    '''
    print(f"sqlite3 query mode. Database:{database_name1} ('quit' to exit query mode)")
    try:
        check=query.find("SELECT")*query.find("Select")*query.find("select")
        if check==0:
            conn=sqlite3.connect(database_name1)
            cursor=conn.execute(query)
            for row in cursor:
                print(row)
        else:
            conn=sqlite3.connect(database_name1)
            conn.execute(query)
            conn.commit()
    except:
        print(sys.exc_info()," error.")
#1. Convert .CSV files to pandas dataframes
#2. Add respective genre code for a mapping
#3. Convert DataFrame into SQLite Database