import pypyodbc as odbc
import pandas as pd

# I am using Microsoft SQL Server as my DBMS.
DRIVER = 'SQL Server'
SERVER_NAME = <YOUR SERVER> # replace with your server name.
DATABASE_NAME = 'ABCCompany'

# Import dataset from CSV
df = pd.read_csv('flat_data.csv')

# Specify columns to import into department table.
dept_cols = ['dept_name','salary_increment']
dept_df = df[dept_cols]
unique_dept = dept_df.drop_duplicates() # Remove duplicate data.
dept_records = unique_dept.values.tolist() # convert each row into list

# Specify columns to import into employees table.
emp_cols = ['first_name', 'last_name', 'salary', 'dept_name']
emp_df = df[emp_cols]
print(emp_df)

# Replace values in dept_name to corresponding department_id
emp_df['dept_name'] = emp_df['dept_name'].replace(
    ['Finance', 'IT', 'Sales', 'Marketing'], 
    [1, 2, 3, 4])

#rename column name dept_name to department_id. 
emp_df = emp_df.rename(columns = {'dept_name': 'department_id'})
emp_records = emp_df.values.tolist() # convert each row into a list

# sql insert data into department table
dept_insert = '''
    INSERT INTO department (name, salary_increment)
    VALUES (?, ?)
'''

# sql insert data into employees table
emp_insert = '''
    INSERT INTO employees (first_name, last_name, salary, department_id)
    VALUES (?, ?, ?, ?)
'''
# Create connection function.
def connect_str(driver, server_name, database_name):
    str = f"""
        DRIVER={{{driver}}};
        SERVER={server_name};
        DATABASE={database_name};
        Trust_Connection=yes;
        """
    return str

# Connect to SQL Server.
conn = odbc.connect(connect_str(DRIVER, SERVER_NAME, DATABASE_NAME))

# Data ingestion.
cursor = conn.cursor()
cursor.executemany(dept_insert, dept_records)
cursor.executemany(emp_insert, emp_records)
cursor.commit()

# Export tables in dbms into csv.
dept_tb = pd.read_sql_query(''' 
                              SELECT * FROM ABCCompany.dbo.department
                              '''
                              ,conn) # 'conn' is the variable that contains your database connection information
df1 = pd.DataFrame(dept_tb)
df1.to_csv (r'C:\Users\<YOUR_PATH>\department.csv', index = False) # Substitute <YOUR_PATH> with your own path.
# place 'r' before the path name to avoid any errors in the path

emp_tb = pd.read_sql_query(''' 
                              SELECT * FROM ABCCompany.dbo.employees
                              '''
                              ,conn)
df2 = pd.DataFrame(emp_tb)
df2.to_csv (r'C:\Users\<YOUR_PATH>\employees.csv', index = False)

sal_tb = pd.read_sql_query(''' 
                              SELECT * FROM ABCCompany.dbo.updated_salaries
                              '''
                              ,conn)
df2 = pd.DataFrame(sal_tb)
df2.to_csv (r'C:\Users\<YOUR_PATH>\updated_salaries.csv', index = False)

# Close cursor and conn when you're done with dbms.
cursor.close() 
conn.close()
