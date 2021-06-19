/* I am using Microsoft SQL Server as my DBMS */

/***************   Create ABC Company database   ***************/
CREATE DATABASE [ABCCompany]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'ABCCompany', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\ABCCompany.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'ABCCompany_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\ABCCompany_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO

IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [ABCCompany].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO

/***************   Create database table.   ***************/
CREATE TABLE department (
    id INT IDENTITY(1,1) NOT NULL,
    name VARCHAR(25)UNIQUE,
    salary_increment NUMERIC
    CONSTRAINT PK_department_id PRIMARY KEY CLUSTERED (id)
);

CREATE TABLE employees (
    id INT IDENTITY(1,1) NOT NULL,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25) NOT NULL,
    salary NUMERIC, 
    department_id INT FOREIGN KEY REFERENCES department (id) NOT NULL,
    CONSTRAINT PK_employees_id PRIMARY KEY CLUSTERED (id)
);

/***************   Query database.   ***************/
CREATE VIEW updated_salaries AS (
	SELECT e.id AS employee_id, e.salary*d.salary_increment*.01 + e.salary AS updated_salary
	FROM employees e
	JOIN department d ON d.id = e.department_id
);

SELECT * FROM department;
SELECT * FROM employees;
SELECT * FROM updated_salaries;
