joins
======
inner join :- returns matched records.
left join :-left table all, right table matched to left table, remaining as null
right join:- right table all ,left table matched to right  table ,remaining as null
full join :- matched 1st ,unmatched from left tab ,unmatched from right tab
cross join:-
self join::- action performed on single  diagram.

A join in MySQL is used to combine rows from two or more tables based on related columns,
eg:- employee table--->employee details
departments----->department details.

if you want  to see which employee belong to which department you need to join these New tables 

why do we need joins:-
--------------------
1. to fetch data from multiple tables in a single query
2. to reduce data duplication (instead of keeping on table)
3.to implement relationships like(one-to-one ,one -to-many, many-to-many ,many-to-one)
4. to generate reports and analytics combining different datasets 

inner join :- returns matched records:-
======================================
returns matching values that have matching values in bothe tables
syntax:- 
select columns
from table1
inner join table 2
on table1.common_column-table2.common_volumn;

left join :-left table all, right table matched to left table, remaining as null
========
returns all rows from the left table and the matched rows from the right table .,if no match, nullvalues appear from the right table column
syntax:- 
select columns
from table1
left join table 2
on table1.common_column-table2.common_column;

right join:- right table all ,left table matched to right  table ,remaining as null
===========
returns all rows from the right table and the matched rows from the left table .,if no match, nullvalues appear from the left table column
syntax:- 
select columns
from table1
right join table 2
on table1.common_column-table2.common_column;

full join :- matched 1st ,unmatched from left tab ,unmatched from right tab
========
to simulate use the union of left and right join 
syntax:
select columns
from table1
left join table 2
on table1.common_column-table2.common_column;
union
select columns
from table1
right join table 2
on table1.common_column-table2.common_column;

cross-join:-
===========
returns cartesian product-->every row in the from the first table with every row from the second table.
syntax:-

select columns
from table1
cross join table2;

self join:-
=========
a table joined with itself
syntax:-
select a-columns,b-columns
from table a 
inner join table b
on a.common_column-b.common_column;


mysql> CREATE TABLE Emp (
    ->  emp_id INT PRIMARY KEY,
    ->     name VARCHAR(100),
    ->     department_id INT,
    ->     salary DECIMAL(10,2)
    -> );
Query OK, 0 rows affected (0.02 sec)

mysql>
mysql> CREATE TABLE Departments (
    ->     department_id INT PRIMARY KEY,
    ->     department_name VARCHAR(100)
    -> );
Query OK, 0 rows affected (0.02 sec)

mysql>
mysql> CREATE TABLE Projects (
    ->     project_id INT PRIMARY KEY,
    ->     project_name VARCHAR(100),
    ->     emp_id INT
    -> );
Query OK, 0 rows affected (0.02 sec)

mysql>
mysql> INSERT INTO Departments (department_id, department_name) VALUES
    -> (1, 'Human Resources'),
    -> (2, 'Engineering'),
    -> (3, 'Marketing'),
    -> (4, 'Finance'),
    -> (5, 'Operations');
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql>
mysql> INSERT INTO Emp (emp_id, name, department_id, salary) VALUES
    -> (101, 'Arjun', 1, 50000),
    -> (102, 'Bhavana', 2, 65000),
    -> (103, 'Charan', 2, 72000),
    -> (104, 'Divya', 3, 45000),
    -> (105, 'Eswar', NULL, 40000),
    -> (106, 'Farhan', 4, 55000),
    -> (107, 'Gowri', 2, 62000),
    -> (108, 'Harish', 5, 48000),
    -> (109, 'Ishita', NULL, 53000),
    -> (110, 'Jagan', 3, 60000);
Query OK, 10 rows affected (0.01 sec)
Records: 10  Duplicates: 0  Warnings: 0

mysql>
mysql> INSERT INTO Projects (project_id, project_name, emp_id) VALUES
    -> (201, 'Website Redesign', 102),
    -> (202, 'Mobile Banking App', 103),
    -> (203, 'Marketing Campaign', 104),
    -> (204, 'Payroll System', 106),
    -> (205, 'Backend Optimization', 107),
    -> (206, 'Cloud Migration', 102),
    -> (207, 'Customer Analytics', 110),
    -> (208, 'Inventory System', NULL);
Query OK, 8 rows affected (0.01 sec)
Records: 8  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM EMP;
+--------+---------+---------------+----------+
| emp_id | name    | department_id | salary   |
+--------+---------+---------------+----------+
|    101 | Arjun   |             1 | 50000.00 |
|    102 | Bhavana |             2 | 65000.00 |
|    103 | Charan  |             2 | 72000.00 |
|    104 | Divya   |             3 | 45000.00 |
|    105 | Eswar   |          NULL | 40000.00 |
|    106 | Farhan  |             4 | 55000.00 |
|    107 | Gowri   |             2 | 62000.00 |
|    108 | Harish  |             5 | 48000.00 |
|    109 | Ishita  |          NULL | 53000.00 |
|    110 | Jagan   |             3 | 60000.00 |
+--------+---------+---------------+----------+
10 rows in set (0.00 sec)

mysql> SELECT * FROM PROJECTS;
+------------+----------------------+--------+
| project_id | project_name         | emp_id |
+------------+----------------------+--------+
|        201 | Website Redesign     |    102 |
|        202 | Mobile Banking App   |    103 |
|        203 | Marketing Campaign   |    104 |
|        204 | Payroll System       |    106 |
|        205 | Backend Optimization |    107 |
|        206 | Cloud Migration      |    102 |
|        207 | Customer Analytics   |    110 |
|        208 | Inventory System     |   NULL |
+------------+----------------------+--------+


mysql> -- INNER JOINT
mysql> -- GET ALL EMPLOYEES WITH THEIR DEPT NAMES
mysql>  SELECT E.EMP_ID,E.NAME,D.DEPARTMENT_NAME
    -> FROM EMP E
    -> INNER JOIN DEPARTMENTS D
    -> ON  E.DEPARTMENT_ID=D.DEPARTMENT_ID;
+--------+---------+-----------------+
| EMP_ID | NAME    | DEPARTMENT_NAME |
+--------+---------+-----------------+
|    101 | Arjun   | Human Resources |
|    102 | Bhavana | Engineering     |
|    103 | Charan  | Engineering     |
|    104 | Divya   | Marketing       |
|    106 | Farhan  | Finance         |
|    107 | Gowri   | Engineering     |
|    108 | Harish  | Operations      |
|    110 | Jagan   | Marketing       |
+--------+---------+-----------------+
8 rows in set (0.00 sec)

mysql> -- LIST ALL EMPLOYEES WHO ARE ASSIGNED TO A PROJECT
mysql> SELECT E.EMP_ID,E.NAME,P.PROJECT_NAME
    -> FROM EMP E
    -> INNER JOIN  PROJECTS P
    -> ON E.EMP_ID=P.EMP_ID;
+--------+---------+----------------------+
| EMP_ID | NAME    | PROJECT_NAME         |
+--------+---------+----------------------+
|    102 | Bhavana | Website Redesign     |
|    103 | Charan  | Mobile Banking App   |
|    104 | Divya   | Marketing Campaign   |
|    106 | Farhan  | Payroll System       |
|    107 | Gowri   | Backend Optimization |
|    102 | Bhavana | Cloud Migration      |
|    110 | Jagan   | Customer Analytics   |
+--------+---------+----------------------+
7 rows in set (0.00 sec)

mysql> SELECT E.EMP_ID,E.NAME
    -> FROM EMP E
    -> INNER JOIN  PROJECTS P
    -> ON E.EMP_ID=P.EMP_ID;
+--------+---------+
| EMP_ID | NAME    |
+--------+---------+
|    102 | Bhavana |
|    103 | Charan  |
|    104 | Divya   |
|    106 | Farhan  |
|    107 | Gowri   |
|    102 | Bhavana |
|    110 | Jagan   |
+--------+---------+
7 rows in set (0.00 sec)

mysql> SELECT E.EMP_ID,E.NAME,P.PROJECT_NAME
    -> FROM EMP E
    -> INNER JOIN  PROJECTS P
    -> ON E.EMP_ID=P.EMP_ID;
+--------+---------+----------------------+
| EMP_ID | NAME    | PROJECT_NAME         |
+--------+---------+----------------------+
|    102 | Bhavana | Website Redesign     |
|    103 | Charan  | Mobile Banking App   |
|    104 | Divya   | Marketing Campaign   |
|    106 | Farhan  | Payroll System       |
|    107 | Gowri   | Backend Optimization |
|    102 | Bhavana | Cloud Migration      |
|    110 | Jagan   | Customer Analytics   |
+--------+---------+----------------------+
7 rows in set (0.00 sec)

mysql> SELECT E.NAME,P.PROJECT_NAME
    -> FROM EMP E
    -> INNER JOIN  PROJECTS P
    -> ON E.EMP_ID=P.EMP_ID;
+---------+----------------------+
| NAME    | PROJECT_NAME         |
+---------+----------------------+
| Bhavana | Website Redesign     |
| Charan  | Mobile Banking App   |
| Divya   | Marketing Campaign   |
| Farhan  | Payroll System       |
| Gowri   | Backend Optimization |
| Bhavana | Cloud Migration      |
| Jagan   | Customer Analytics   |
+---------+----------------------+
7 rows in set (0.00 sec)

mysql> -- LEFT JOIN
mysql> -- LIST ALL EMPLOYEESS AND THEIR DEPARTMENTS(EVEN IF NO DEPT)
mysql> SELECT E.EMP_ID,E.NAME,D.DEPARTMENT_NAME
    -> FROM EMP E
    -> LEFT JOIN DEPARTMENTS D
    -> ON E.DEPARTMENT_ID=D.DEPARTMENT_ID;
+--------+---------+-----------------+
| EMP_ID | NAME    | DEPARTMENT_NAME |
+--------+---------+-----------------+
|    101 | Arjun   | Human Resources |
|    102 | Bhavana | Engineering     |
|    103 | Charan  | Engineering     |
|    104 | Divya   | Marketing       |
|    105 | Eswar   | NULL            |
|    106 | Farhan  | Finance         |
|    107 | Gowri   | Engineering     |
|    108 | Harish  | Operations      |
|    109 | Ishita  | NULL            |
|    110 | Jagan   | Marketing       |
+--------+---------+-----------------+
10 rows in set (0.00 sec)

mysql> -- SHOW ALL EMPLOYEES  AND THEIR PROJECTS
mysql> SELECT E.EMP_ID,E.NAME,P.PROJECT_NAME
    -> FROM EMP E
    -> LEFT JOIN PROJECTS P
    -> ON E.EMP_ID=P.EMP_ID;
+--------+---------+----------------------+
| EMP_ID | NAME    | PROJECT_NAME         |
+--------+---------+----------------------+
|    101 | Arjun   | NULL                 |
|    102 | Bhavana | Cloud Migration      |
|    102 | Bhavana | Website Redesign     |
|    103 | Charan  | Mobile Banking App   |
|    104 | Divya   | Marketing Campaign   |
|    105 | Eswar   | NULL                 |
|    106 | Farhan  | Payroll System       |
|    107 | Gowri   | Backend Optimization |
|    108 | Harish  | NULL                 |
|    109 | Ishita  | NULL                 |
|    110 | Jagan   | Customer Analytics   |
+--------+---------+----------------------+
11 rows in set (0.05 sec)

mysql> -- GET ALL DEPARTMENTS AND EMPLOYEES WORKING IN THEM
mysql> SELECT D.DEPARTMENT_NAME,E.NAME
    -> FROM DEPARTMENTS D
    -> LEFT JOIN EMP E
    -> ON D.DEPARTMENT_ID=E.DEPARTMENT_ID;
+-----------------+---------+
| DEPARTMENT_NAME | NAME    |
+-----------------+---------+
| Human Resources | Arjun   |
| Engineering     | Gowri   |
| Engineering     | Charan  |
| Engineering     | Bhavana |
| Marketing       | Jagan   |
| Marketing       | Divya   |
| Finance         | Farhan  |
| Operations      | Harish  |
+-----------------+---------+
8 rows in set (0.00 sec)

mysql> SELECT E.EMP_ID,E.NAME,D.DEPARTMENT_NAME
    -> FROM EMP E
    -> LEFT JOIN DEPARTMENTS D
    -> ON E.DEPARTMENT_ID=NULL;
+--------+---------+-----------------+
| EMP_ID | NAME    | DEPARTMENT_NAME |
+--------+---------+-----------------+
|    101 | Arjun   | NULL            |
|    102 | Bhavana | NULL            |
|    103 | Charan  | NULL            |
|    104 | Divya   | NULL            |
|    105 | Eswar   | NULL            |
|    106 | Farhan  | NULL            |
|    107 | Gowri   | NULL            |
|    108 | Harish  | NULL            |
|    109 | Ishita  | NULL            |
|    110 | Jagan   | NULL            |
+--------+---------+-----------------+
10 rows in set (0.00 sec)

mysql> SELECT E.EMP_ID,E.NAME,D.DEPARTMENT_NAME
    -> FROM EMP E
    -> LEFT JOIN DEPARTMENTS D
    -> ON E.DEPARTMENT_ID=D.DEPARTMENT_ID
    -> WHERE D.DEPARTMENT_NAME IS NULL;
+--------+--------+-----------------+
| EMP_ID | NAME   | DEPARTMENT_NAME |
+--------+--------+-----------------+
|    105 | Eswar  | NULL            |
|    109 | Ishita | NULL            |
+--------+--------+-----------------+
2 rows in set (0.00 sec)

mysql> -- RIGHT JOIN
mysql> -- LIST ALL DEPARTEMENTS AND THE EMPLOYEES IN THEM (EVEN IF NO EMPLOYEE)
mysql> SELECT D.DEPARTMENT_NAME,E.NAME
    -> FROM DEPARTMENTS D
    -> RIGHT JOIN EMP E
    -> ON D.DEPARTMENT_ID=E.DEPARTMENT_ID;
+-----------------+---------+
| DEPARTMENT_NAME | NAME    |
+-----------------+---------+
| Human Resources | Arjun   |
| Engineering     | Bhavana |
| Engineering     | Charan  |
| Marketing       | Divya   |
| NULL            | Eswar   |
| Finance         | Farhan  |
| Engineering     | Gowri   |
| Operations      | Harish  |
| NULL            | Ishita  |
| Marketing       | Jagan   |
+-----------------+---------+
10 rows in set (0.00 sec)

mysql> -- SHOW ALL PROJECTS AND THIER ASSIGNED EMPLOYEES(EVEN NO PROJECTS)
mysql> SELECT P.PROJECT_NAME,E.NAME
    -> FROM PROJECTS P
    -> RIGHT JOIN EMP E
    -> ON P.EMP_ID=E.EMP_ID;
+----------------------+---------+
| PROJECT_NAME         | NAME    |
+----------------------+---------+
| NULL                 | Arjun   |
| Cloud Migration      | Bhavana |
| Website Redesign     | Bhavana |
| Mobile Banking App   | Charan  |
| Marketing Campaign   | Divya   |
| NULL                 | Eswar   |
| Payroll System       | Farhan  |
| Backend Optimization | Gowri   |
| NULL                 | Harish  |
| NULL                 | Ishita  |
| Customer Analytics   | Jagan   |
+----------------------+---------+
11 rows in set (0.00 sec)

mysql> -- LIST ALL EMPLOYEES
mysql> -- LIST ALL EMPLOYEES  AND THE DEPARTMENTS THEY BELONG USING RIGHT JOIN
mysql> SELECT E.NAME,D.DEPARTMENT_NAME
    -> FROM EMP E
    -> LEFT JOIN DEPARTMENTS D
    -> ON E.DEPARTMENT_ID=D.DEPARTMENT_ID
    -> UNION
    -> SELECT D.DEPARTMENT_NAME,E.NAME
    -> FROM DEPARTMENTS D
    -> RIGHT JOIN EMP E
    -> ON D.DEPARTMENT_ID=E.DEPARTMENT_ID;
+-----------------+-----------------+
| NAME            | DEPARTMENT_NAME |
+-----------------+-----------------+
| Arjun           | Human Resources |
| Bhavana         | Engineering     |
| Charan          | Engineering     |
| Divya           | Marketing       |
| Eswar           | NULL            |
| Farhan          | Finance         |
| Gowri           | Engineering     |
| Harish          | Operations      |
| Ishita          | NULL            |
| Jagan           | Marketing       |
| Human Resources | Arjun           |
| Engineering     | Bhavana         |
| Engineering     | Charan          |
| Marketing       | Divya           |
| NULL            | Eswar           |
| Finance         | Farhan          |
| Engineering     | Gowri           |
| Operations      | Harish          |
| NULL            | Ishita          |
| Marketing       | Jagan           |
+-----------------+-----------------+
20 rows in set (0.05 sec)

mysql> -- CROSS JOIN
mysql> SELECT * FROM EMP
    -> CROSS JOIN DEPARTMENTS;
+--------+---------+---------------+----------+---------------+-----------------+
| emp_id | name    | department_id | salary   | department_id | department_name |
+--------+---------+---------------+----------+---------------+-----------------+
|    101 | Arjun   |             1 | 50000.00 |             5 | Operations      |
|    101 | Arjun   |             1 | 50000.00 |             4 | Finance         |
|    101 | Arjun   |             1 | 50000.00 |             3 | Marketing       |
|    101 | Arjun   |             1 | 50000.00 |             2 | Engineering     |
|    101 | Arjun   |             1 | 50000.00 |             1 | Human Resources |
|    102 | Bhavana |             2 | 65000.00 |             5 | Operations      |
|    102 | Bhavana |             2 | 65000.00 |             4 | Finance         |
|    102 | Bhavana |             2 | 65000.00 |             3 | Marketing       |
|    102 | Bhavana |             2 | 65000.00 |             2 | Engineering     |
|    102 | Bhavana |             2 | 65000.00 |             1 | Human Resources |
|    103 | Charan  |             2 | 72000.00 |             5 | Operations      |
|    103 | Charan  |             2 | 72000.00 |             4 | Finance         |
|    103 | Charan  |             2 | 72000.00 |             3 | Marketing       |
|    103 | Charan  |             2 | 72000.00 |             2 | Engineering     |
|    103 | Charan  |             2 | 72000.00 |             1 | Human Resources |
|    104 | Divya   |             3 | 45000.00 |             5 | Operations      |
|    104 | Divya   |             3 | 45000.00 |             4 | Finance         |
|    104 | Divya   |             3 | 45000.00 |             3 | Marketing       |
|    104 | Divya   |             3 | 45000.00 |             2 | Engineering     |
|    104 | Divya   |             3 | 45000.00 |             1 | Human Resources |
|    105 | Eswar   |          NULL | 40000.00 |             5 | Operations      |
|    105 | Eswar   |          NULL | 40000.00 |             4 | Finance         |
|    105 | Eswar   |          NULL | 40000.00 |             3 | Marketing       |
|    105 | Eswar   |          NULL | 40000.00 |             2 | Engineering     |
|    105 | Eswar   |          NULL | 40000.00 |             1 | Human Resources |
|    106 | Farhan  |             4 | 55000.00 |             5 | Operations      |
|    106 | Farhan  |             4 | 55000.00 |             4 | Finance         |
|    106 | Farhan  |             4 | 55000.00 |             3 | Marketing       |
|    106 | Farhan  |             4 | 55000.00 |             2 | Engineering     |
|    106 | Farhan  |             4 | 55000.00 |             1 | Human Resources |
|    107 | Gowri   |             2 | 62000.00 |             5 | Operations      |
|    107 | Gowri   |             2 | 62000.00 |             4 | Finance         |
|    107 | Gowri   |             2 | 62000.00 |             3 | Marketing       |
|    107 | Gowri   |             2 | 62000.00 |             2 | Engineering     |
|    107 | Gowri   |             2 | 62000.00 |             1 | Human Resources |
|    108 | Harish  |             5 | 48000.00 |             5 | Operations      |
|    108 | Harish  |             5 | 48000.00 |             4 | Finance         |
|    108 | Harish  |             5 | 48000.00 |             3 | Marketing       |
|    108 | Harish  |             5 | 48000.00 |             2 | Engineering     |
|    108 | Harish  |             5 | 48000.00 |             1 | Human Resources |
|    109 | Ishita  |          NULL | 53000.00 |             5 | Operations      |
|    109 | Ishita  |          NULL | 53000.00 |             4 | Finance         |
|    109 | Ishita  |          NULL | 53000.00 |             3 | Marketing       |
|    109 | Ishita  |          NULL | 53000.00 |             2 | Engineering     |
|    109 | Ishita  |          NULL | 53000.00 |             1 | Human Resources |
|    110 | Jagan   |             3 | 60000.00 |             5 | Operations      |
|    110 | Jagan   |             3 | 60000.00 |             4 | Finance         |
|    110 | Jagan   |             3 | 60000.00 |             3 | Marketing       |
|    110 | Jagan   |             3 | 60000.00 |             2 | Engineering     |
|    110 | Jagan   |             3 | 60000.00 |             1 | Human Resources |
+--------+---------+---------------+----------+---------------+-----------------+
50 rows in set (0.00 sec)

mysql> SELECT E.EMP_ID,D.DEPARTMENT_ID
    -> FROM EMP E
    -> CROSS JOIN DEPARTMENTS D;
+--------+---------------+
| EMP_ID | DEPARTMENT_ID |
+--------+---------------+
|    101 |             5 |
|    101 |             4 |
|    101 |             3 |
|    101 |             2 |
|    101 |             1 |
|    102 |             5 |
|    102 |             4 |
|    102 |             3 |
|    102 |             2 |
|    102 |             1 |
|    103 |             5 |
|    103 |             4 |
|    103 |             3 |
|    103 |             2 |
|    103 |             1 |
|    104 |             5 |
|    104 |             4 |
|    104 |             3 |
|    104 |             2 |
|    104 |             1 |
|    105 |             5 |
|    105 |             4 |
|    105 |             3 |
|    105 |             2 |
|    105 |             1 |
|    106 |             5 |
|    106 |             4 |
|    106 |             3 |
|    106 |             2 |
|    106 |             1 |
|    107 |             5 |
|    107 |             4 |
|    107 |             3 |
|    107 |             2 |
|    107 |             1 |
|    108 |             5 |
|    108 |             4 |
|    108 |             3 |
|    108 |             2 |
|    108 |             1 |
|    109 |             5 |
|    109 |             4 |
|    109 |             3 |
|    109 |             2 |
|    109 |             1 |
|    110 |             5 |
|    110 |             4 |
|    110 |             3 |
|    110 |             2 |
|    110 |             1 |
+--------+---------------+


=======================================================
VIEWS
=======
WHAT IS A VIEW
-----------------
A VIEW IS A VIRTUAL TABLE IN MY SQL
BULIT IT FROM THE RESULT OF STORED SELECT STATEMENTS
IT LOOKS AND BEHAVES LIKE REGULAR TABLE WHEN YOU QUERY IT
YOU CAN SELECT FROM IT,FILTER IT AND JOINED IT
BUT IT DOESN'T STORE ANY DATA ON ITS OWN
EVERY TIME VIEW IS QUERIED 
MYSQL RUNS ITS UNDERLYING SELECT STATEMENTS AGAINST IN REAL TABLES AND RETURNS THE RESULT

WHY DO WE NEED VIES
-------------------
SIMPLIFY COMPLEX QUERIES
REUSE QUERY
DATA SECURITY
LOGICAL DATA IDEPENDENCE

ADVANTAGES
------------
SECURITY
REUSABILITY
SIMPLICITY
CONSISTENCY
MAINTAINABILITY
CUSTOM DATA PRESENTATION
NO EXTRA  STORAGE COST
 
CREATING VIEW
---------------
CREATE VIEW VIEW NAME AS
SELECT COLUMNS FROM TABLE
WHERE CONDITION

ALTERING VIEWS
---------------
ALTER VIEW VIEW NAME
SELECT NEW_COLUMNS
FROM NEW_TABLES

DROPING VIEW
-------------
DROP VIEW VIEW NAME;
DROP VIEW IF EXISTS VIEW_NAME;


mysql> CREATE TABLE departments (
    ->  dept_id INT PRIMARY KEY AUTO_INCREMENT,
    ->  dept_name VARCHAR(50),
    ->  location VARCHAR(50)
    -> );
Query OK, 0 rows affected (0.08 sec)

mysql>
mysql> CREATE TABLE employees (
    ->  emp_id INT PRIMARY KEY AUTO_INCREMENT,
    ->  emp_name VARCHAR(100),
    ->  dept_id INT,
    ->  designation VARCHAR(50),
    ->  salary DECIMAL(10,2),
    ->  join_date DATE,
    ->  FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
    -> );
Query OK, 0 rows affected (0.03 sec)

mysql>
mysql> INSERT INTO departments (dept_name, location) VALUES
    -> ('IT','Hyderabad'), ('HR','Bangalore'), ('Finance','Chennai'), ('Sales','Mumbai');
Query OK, 4 rows affected (0.01 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql>
mysql> INSERT INTO employees (emp_name, dept_id, designation, salary, join_date) VALUES
    -> ('Rahul',1,'Software Engineer',55000,'2021-06-15'),
    -> ('Anita',2,'HR Executive',38000,'2020-03-21'),
    -> ('Suresh',4,'Sales Manager',52000,'2019-08-10'),
    -> ('Priya',1,'Team Lead',65000,'2022-01-05'),
    -> ('Kiran',3,'Finance Analyst',48000,'2018-12-11'),
    -> ('Deepika',2,'HR Manager',60000,'2019-10-19')
    -> ;
Query OK, 6 rows affected (0.06 sec)
Records: 6  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM EMPLOYEES;
+--------+----------+---------+-------------------+----------+------------+
| emp_id | emp_name | dept_id | designation       | salary   | join_date  |
+--------+----------+---------+-------------------+----------+------------+
|      1 | Rahul    |       1 | Software Engineer | 55000.00 | 2021-06-15 |
|      2 | Anita    |       2 | HR Executive      | 38000.00 | 2020-03-21 |
|      3 | Suresh   |       4 | Sales Manager     | 52000.00 | 2019-08-10 |
|      4 | Priya    |       1 | Team Lead         | 65000.00 | 2022-01-05 |
|      5 | Kiran    |       3 | Finance Analyst   | 48000.00 | 2018-12-11 |
|      6 | Deepika  |       2 | HR Manager        | 60000.00 | 2019-10-19 |
+--------+----------+---------+-------------------+----------+------------+
6 rows in set (0.00 sec)

mysql> SELECT * FROM DEPARTMENTS;
+---------+-----------+-----------+
| dept_id | dept_name | location  |
+---------+-----------+-----------+
|       1 | IT        | Hyderabad |
|       2 | HR        | Bangalore |
|       3 | Finance   | Chennai   |
|       4 | Sales     | Mumbai    |
+---------+-----------+-----------+
4 rows in set (0.00 sec)

mysql> CREATE VIEW VW_EMP_DEPT AS
    -> SELECT E.EMP_ID,E.EMP_NAME,E.DESIGNATION,D.DEPT_NAME,D.LOCATION
    -> FROM EMPLOYEES E
    -> JOIN DEPARTMENTS D
    -> ON E.DEPT_ID=D.DEPT_ID;
Query OK, 0 rows affected (0.07 sec)

mysql> SELECT * FROM VW_EMP_DEPT;
+--------+----------+-------------------+-----------+-----------+
| EMP_ID | EMP_NAME | DESIGNATION       | DEPT_NAME | LOCATION  |
+--------+----------+-------------------+-----------+-----------+
|      1 | Rahul    | Software Engineer | IT        | Hyderabad |
|      4 | Priya    | Team Lead         | IT        | Hyderabad |
|      2 | Anita    | HR Executive      | HR        | Bangalore |
|      6 | Deepika  | HR Manager        | HR        | Bangalore |
|      5 | Kiran    | Finance Analyst   | Finance   | Chennai   |
|      3 | Suresh   | Sales Manager     | Sales     | Mumbai    |
+--------+----------+-------------------+-----------+-----------+


mysql> SELECT TABLE_NAME
    -> FROM INFORMATION_SCHEMA.VIEWS
    -> WHERE TABLE_SCHEMA='PSF4';
+-------------+
| TABLE_NAME  |
+-------------+
| vw_emp_dept |
+-------------+
1 row in set (0.05 sec)

mysql> DESC VW_EMP_DEPT;
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| EMP_ID      | int          | NO   |     | 0       |       |
| EMP_NAME    | varchar(100) | YES  |     | NULL    |       |
| DESIGNATION | varchar(50)  | YES  |     | NULL    |       |
| DEPT_NAME   | varchar(50)  | YES  |     | NULL    |       |
| LOCATION    | varchar(50)  | YES  |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+


mysql> CREATE VIEW VW_DEPT_SALARY
    -> AS
    -> SELECT D.DEPT_NAME,
    -> COUNT(E.EMP_ID) AS TOTAL_EMPLOYEES,
    -> SUM(E.SALARY)AS TOTAL_SALARY,
    -> AVG(E.SALARY) AS AVG_SALARY
    -> FROM EMPLOYEES E
    -> JOIN DEPARTMENTS D
    -> ON E.DEPT_ID=D.DEPT_ID
    -> GROUP BY D.DEPT_NAME;
Query OK, 0 rows affected (0.01 sec)

mysql> SELECT *FROM VW_DEPT_SALARY;
+-----------+-----------------+--------------+--------------+
| DEPT_NAME | TOTAL_EMPLOYEES | TOTAL_SALARY | AVG_SALARY   |
+-----------+-----------------+--------------+--------------+
| IT        |               2 |    120000.00 | 60000.000000 |
| HR        |               2 |     98000.00 | 49000.000000 |
| Finance   |               1 |     48000.00 | 48000.000000 |
| Sales     |               1 |     52000.00 | 52000.000000 |
+-----------+-----------------+--------------+--------------+
4 rows in set (0.05 sec)

 SELECT TABLE_NAME
    -> FROM INFORMATION_SCHEMA.VIEWS
    -> WHERE TABLE_SCHEMA='PSF4';
+----------------+
| TABLE_NAME     |
+----------------+
| vw_emp_dept    |
| vw_dept_salary |
+----------------+
2 rows in set (0.00 sec)

mysql> CREATE VIEW VW_SALARY
    -> AS
    -> SELECT EMP_NAME,SALARY AS MONTLY_SALARY,SALARY*12
    -> AS ANNUAL_SALARY
    -> FROM EMPLOYEES;
Query OK, 0 rows affected (0.09 sec)

mysql> SELECT * FROM VW_SALARY;
+----------+---------------+---------------+
| EMP_NAME | MONTLY_SALARY | ANNUAL_SALARY |
+----------+---------------+---------------+
| Rahul    |      55000.00 |     660000.00 |
| Anita    |      38000.00 |     456000.00 |
| Suresh   |      52000.00 |     624000.00 |
| Priya    |      65000.00 |     780000.00 |
| Kiran    |      48000.00 |     576000.00 |
| Deepika  |      60000.00 |     720000.00 |
+----------+---------------+---------------+


mysql> CREATE VIEW VW_HIGH_PAID_DEPT
    -> AS
    -> SELECT DEPT_NAME,AVG_SALARY
    -> FROM VW_DEPT_SALARY
    -> WHERE AVG_SALARY>50000;
Query OK, 0 rows affected (0.09 sec)

mysql> SELECT * FROM VW_HIGH_PAID_DEPT;
+-----------+--------------+
| DEPT_NAME | AVG_SALARY   |
+-----------+--------------+
| IT        | 60000.000000 |
| Sales     | 52000.000000 |
+-----------+--------------+


mysql> -- ALTERING VIEWS
mysql> ALTER VIEW  VW_EMP_DEPT
    -> AS
    -> SELECT E.EMP_ID,E.EMP_NAME,D.DEPT_NAME
    -> FROM EMPLOYEES E
    -> JOIN DEPARTMENTS D
    -> ON E.DEPT_ID=D.DEPT_ID;
Query OK, 0 rows affected (0.05 sec)
mysql> SELECT *  FROM VW_EMP_DEPT;
+--------+----------+-----------+
| EMP_ID | EMP_NAME | DEPT_NAME |
+--------+----------+-----------+
|      1 | Rahul    | IT        |
|      4 | Priya    | IT        |
|      2 | Anita    | HR        |
|      6 | Deepika  | HR        |
|      5 | Kiran    | Finance   |
|      3 | Suresh   | Sales     |
+--------+----------+-----------+
6 rows in set (0.00 sec)

mysql> DROP VIEW  VW_EMP_DEPT;
Query OK, 0 rows affected (0.05 sec)


==========================================================================================================================
views:-
=====
what is a view?/
a view is a virtual table in MySQL. built from th ethe result of the stored select statement.it look like the regular table when you query it.
you can select from it, filter ,and also join it. but its doesn't not store any data on its own. everytime view is queried. MySQL runs its underlying select statement against in real tables and returns the result.

why do we need views??
1.to simplify complex queries
2. to reuse query logic
3. data security
4.logicall data independence 

advantages of view:-
================
security
reusability
simplicity
consistency
maintainability
custom data presentation
no extra storage cost

creating view??
===============
syntax
create view view_name as
select columns from table
where condidtion

altering view??
================
alter view view_name as
select new_columns
from new_tables

dropping tables?
===============
drop view view-name;
drop view if exists view_name;




























