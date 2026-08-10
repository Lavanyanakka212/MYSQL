mysql> CREATE TABLE Projects (
    ->    id INT,
    ->    name VARCHAR(100),
    ->    assignedto VARCHAR(100),
    ->    start DATE,
    ->    end DATE
    -> );
Query OK, 0 rows affected (0.07 sec)

mysql>
mysql> INSERT INTO Projects VALUES
    -> (1, 'Website Revamp', 'Alice', '2024-01-15', '2024-03-01'),
    -> (2, 'Mobile App', 'Bob', '2024-02-01', NULL),
    -> (3, 'Data Migration', NULL, NULL, NULL),
    -> (4, 'SEO Optimization', 'Eve', '2024-03-10', '2024-04-20'),
    -> (5, 'Cloud Migration', NULL, '2024-03-15', NULL);
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql>
mysql>
mysql> SELECT*FROM PROJECTS;
+------+------------------+------------+------------+------------+
| id   | name             | assignedto | start      | end        |
+------+------------------+------------+------------+------------+
|    1 | Website Revamp   | Alice      | 2024-01-15 | 2024-03-01 |
|    2 | Mobile App       | Bob        | 2024-02-01 | NULL       |
|    3 | Data Migration   | NULL       | NULL       | NULL       |
|    4 | SEO Optimization | Eve        | 2024-03-10 | 2024-04-20 |
|    5 | Cloud Migration  | NULL       | 2024-03-15 | NULL       |
+------+------------------+------------+------------+------------+
5 rows in set (0.00 sec)

mysql> SELECT*FROM PROJECTS WHERE ASSIGNEDTO IS NULL;
+------+-----------------+------------+------------+------+
| id   | name            | assignedto | start      | end  |
+------+-----------------+------------+------------+------+
|    3 | Data Migration  | NULL       | NULL       | NULL |
|    5 | Cloud Migration | NULL       | 2024-03-15 | NULL |
+------+-----------------+------------+------------+------+
2 rows in set (0.01 sec)

mysql> --GET ALL PROJECTS THAT HAVE NOT STARTED YET:
    -> ^C
mysql> SELECT*FROM PROJECTS WHERE START IS NULL;
+------+----------------+------------+-------+------+
| id   | name           | assignedto | start | end  |
+------+----------------+------------+-------+------+
|    3 | Data Migration | NULL       | NULL  | NULL |
+------+----------------+------------+-------+------+
1 row in set (0.00 sec)

mysql> --GET ALL PROJECTS THAT HAVE BEEN COMPLETED:^C
mysql> SELECT*FROM PROJECTS WHERE END IS NOT NULL;
+------+------------------+------------+------------+------------+
| id   | name             | assignedto | start      | end        |
+------+------------------+------------+------------+------------+
|    1 | Website Revamp   | Alice      | 2024-01-15 | 2024-03-01 |
|    4 | SEO Optimization | Eve        | 2024-03-10 | 2024-04-20 |
+------+------------------+------------+------------+------------+
2 rows in set (0.01 sec)

mysql> --GET ALL PROJECTS WITH ASSIGNED EMPLOYEE^C
mysql> SELECT*FROM PROJECTS WHERE ASSIGNEDTO IS NOT NULL;
+------+------------------+------------+------------+------------+
| id   | name             | assignedto | start      | end        |
+------+------------------+------------+------------+------------+
|    1 | Website Revamp   | Alice      | 2024-01-15 | 2024-03-01 |
|    2 | Mobile App       | Bob        | 2024-02-01 | NULL       |
|    4 | SEO Optimization | Eve        | 2024-03-10 | 2024-04-20 |
+------+------------------+------------+------------+------------+
3 rows in set (0.00 sec)

mysql> --ASSIGN UNASSIGNED PROJECTS TO A DEFAULT PERSON(FRANK)^C
mysql> UPDATE PROJECTS SET WHERE ASSGINEDTO IS NULL TO FRANK;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'WHERE ASSGINEDTO IS NULL TO FRANK' at line 1
mysql> UPDATE PROJECTS SET FRANK WHERE ASSIGNEDTO IS NULL;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'WHERE ASSIGNEDTO IS NULL' at line 1
mysql> UPDATE PROJECTS SET ASSIGNEDTO='FRANK' WHERE ASSIGNEDTO IS NULL;
Query OK, 2 rows affected (0.01 sec)
Rows matched: 2  Changed: 2  Warnings: 0

mysql> DESC PROJECTS;
+------------+--------------+------+-----+---------+-------+
| Field      | Type         | Null | Key | Default | Extra |
+------------+--------------+------+-----+---------+-------+
| id         | int          | YES  |     | NULL    |       |
| name       | varchar(100) | YES  |     | NULL    |       |
| assignedto | varchar(100) | YES  |     | NULL    |       |
| start      | date         | YES  |     | NULL    |       |
| end        | date         | YES  |     | NULL    |       |
+------------+--------------+------+-----+---------+-------+
5 rows in set (0.02 sec)

mysql> SELECT*FROM PROJECTS;
+------+------------------+------------+------------+------------+
| id   | name             | assignedto | start      | end        |
+------+------------------+------------+------------+------------+
|    1 | Website Revamp   | Alice      | 2024-01-15 | 2024-03-01 |
|    2 | Mobile App       | Bob        | 2024-02-01 | NULL       |
|    3 | Data Migration   | FRANK      | NULL       | NULL       |
|    4 | SEO Optimization | Eve        | 2024-03-10 | 2024-04-20 |
|    5 | Cloud Migration  | FRANK      | 2024-03-15 | NULL       |
+------+------------------+------------+------------+------------+
5 rows in set (0.00 sec)

mysql> --UPDATE START DATE TO TODAY FOR PROJECTS THAT HAVENT STARTED^C
mysql> UPDATE PROJECTS SET START='2026-07-23' WHERE START IS NULL;
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT*FROM PROJECTS;
+------+------------------+------------+------------+------------+
| id   | name             | assignedto | start      | end        |
+------+------------------+------------+------------+------------+
|    1 | Website Revamp   | Alice      | 2024-01-15 | 2024-03-01 |
|    2 | Mobile App       | Bob        | 2024-02-01 | NULL       |
|    3 | Data Migration   | FRANK      | 2026-07-23 | NULL       |
|    4 | SEO Optimization | Eve        | 2024-03-10 | 2024-04-20 |
|    5 | Cloud Migration  | FRANK      | 2024-03-15 | NULL       |
+------+------------------+------------+------------+------------+
5 rows in set (0.00 sec)

mysql> --UPDATE COMPLETED TO ASSIGNMENTS THAT ARE COMPLETED^C
mysql> UPDATE PROJECTS SET NAME='COMPLETED' WHERE END IS NOT NULL;
Query OK, 2 rows affected (0.01 sec)
Rows matched: 2  Changed: 2  Warnings: 0

mysql> SELECT*FROM PROJECTS;
+------+-----------------+------------+------------+------------+
| id   | name            | assignedto | start      | end        |
+------+-----------------+------------+------------+------------+
|    1 | COMPLETED       | Alice      | 2024-01-15 | 2024-03-01 |
|    2 | Mobile App      | Bob        | 2024-02-01 | NULL       |
|    3 | Data Migration  | FRANK      | 2026-07-23 | NULL       |
|    4 | COMPLETED       | Eve        | 2024-03-10 | 2024-04-20 |
|    5 | Cloud Migration | FRANK      | 2024-03-15 | NULL       |
+------+-----------------+------------+------------+------------+
5 rows in set (0.00 sec)

mysql> DELETE FROM PROJECTS WHERE ASSIGNEDTO IS NULL;
Query OK, 0 rows affected (0.00 sec)

mysql> DELETE FROM PROJECTS WHERE START IS NULL;
Query OK, 0 rows affected (0.00 sec)

mysql> DELETE FROM PROJECTS WHERE END IS NOT NULL;
Query OK, 2 rows affected (0.01 sec)

mysql> SELECT*FROM PROJECTS;
+------+-----------------+------------+------------+------+
| id   | name            | assignedto | start      | end  |
+------+-----------------+------------+------------+------+
|    2 | Mobile App      | Bob        | 2024-02-01 | NULL |
|    3 | Data Migration  | FRANK      | 2026-07-23 | NULL |
|    5 | Cloud Migration | FRANK      | 2024-03-15 | NULL |
+------+-----------------+------------+------------+------+
3 rows in set (0.00 sec)

mysql> CREATE TABLE Orders (
    ->  id INT,
    ->  customer_name VARCHAR(100),
    ->  order_date DATE,
    ->  total_amount DECIMAL(10,2)
    ->  );
Query OK, 0 rows affected (0.03 sec)

mysql>
mysql> -- STEP 2: Insert Records
mysql> INSERT INTO Orders VALUES
    ->  (1, 'Alice', '2024-03-01', 1500.00),
    ->  (2, 'Bob', '2024-03-05', 450.00),
    ->  (3, 'Charlie', '2024-03-10', 2500.00),
    ->  (4, 'Diana', '2024-03-15', 800.00),
    ->  (5, 'Eve', '2024-03-20', 1200.00),
    ->  (6, 'Frank', '2024-03-25', 3000.00),
    ->  (7, 'Grace', '2024-04-02', 1800.00),
    ->  (8, 'Henry', '2024-04-08', 950.00),
    ->  (9, 'Ivy', '2024-04-12', 2750.00),
    ->  (10, 'Jack', '2024-04-18', 650.00),
    ->  (11, 'Kevin', '2024-04-22', 4200.00),
    ->  (12, 'Lily', '2024-05-01', 1350.00),
    ->  (13, 'Michael', '2024-05-08', 5000.00),
    ->  (14, 'Nancy', '2024-05-15', 2250.00),
    ->  (15, 'Oliver', '2024-05-25', 900.00);
Query OK, 15 rows affected (0.01 sec)
Records: 15  Duplicates: 0  Warnings: 0

mysql> SELECT*FROM ORDERS;
+------+---------------+------------+--------------+
| id   | customer_name | order_date | total_amount |
+------+---------------+------------+--------------+
|    1 | Alice         | 2024-03-01 |      1500.00 |
|    2 | Bob           | 2024-03-05 |       450.00 |
|    3 | Charlie       | 2024-03-10 |      2500.00 |
|    4 | Diana         | 2024-03-15 |       800.00 |
|    5 | Eve           | 2024-03-20 |      1200.00 |
|    6 | Frank         | 2024-03-25 |      3000.00 |
|    7 | Grace         | 2024-04-02 |      1800.00 |
|    8 | Henry         | 2024-04-08 |       950.00 |
|    9 | Ivy           | 2024-04-12 |      2750.00 |
|   10 | Jack          | 2024-04-18 |       650.00 |
|   11 | Kevin         | 2024-04-22 |      4200.00 |
|   12 | Lily          | 2024-05-01 |      1350.00 |
|   13 | Michael       | 2024-05-08 |      5000.00 |
|   14 | Nancy         | 2024-05-15 |      2250.00 |
|   15 | Oliver        | 2024-05-25 |       900.00 |
+------+---------------+------------+--------------+
15 rows in set (0.00 sec)

mysql> SELECT*FROM ORDERS WHERE ORDER_DATE BETWEEN '2024-03-03' AND '2024-03-10';
+------+---------------+------------+--------------+
| id   | customer_name | order_date | total_amount |
+------+---------------+------------+--------------+
|    2 | Bob           | 2024-03-05 |       450.00 |
|    3 | Charlie       | 2024-03-10 |      2500.00 |
+------+---------------+------------+--------------+
2 rows in set (0.00 sec)

mysql> SELECT*FROM ORDERS WHERE ORDER_DATE BETWEEN '2024-03-05' AND '2024-03-10';
+------+---------------+------------+--------------+
| id   | customer_name | order_date | total_amount |
+------+---------------+------------+--------------+
|    2 | Bob           | 2024-03-05 |       450.00 |
|    3 | Charlie       | 2024-03-10 |      2500.00 |
+------+---------------+------------+--------------+
2 rows in set (0.00 sec)

mysql> --DISPLAY ORDER PLACED BETWEEN '2024-04-01' AND '2024-04-30'^C
mysql> SELECT*FROM ORDERS WHERE ORDER_DATE BETWEEN '2024-04-01' AND '2024-04-30';
+------+---------------+------------+--------------+
| id   | customer_name | order_date | total_amount |
+------+---------------+------------+--------------+
|    7 | Grace         | 2024-04-02 |      1800.00 |
|    8 | Henry         | 2024-04-08 |       950.00 |
|    9 | Ivy           | 2024-04-12 |      2750.00 |
|   10 | Jack          | 2024-04-18 |       650.00 |
|   11 | Kevin         | 2024-04-22 |      4200.00 |
+------+---------------+------------+--------------+
5 rows in set (0.00 sec)

mysql> --DISPLAY ORDERS WHOSE TOTAL AMOUNGT IS BETWEEN 500 TO 1000^C
mysql> SELECT*FROM ORDERS WHERE TOTAL_AMOUNT BETWEEN 500 AND 1000;
+------+---------------+------------+--------------+
| id   | customer_name | order_date | total_amount |
+------+---------------+------------+--------------+
|    4 | Diana         | 2024-03-15 |       800.00 |
|    8 | Henry         | 2024-04-08 |       950.00 |
|   10 | Jack          | 2024-04-18 |       650.00 |
|   15 | Oliver        | 2024-05-25 |       900.00 |
+------+---------------+------------+--------------+
4 rows in set (0.00 sec)

mysql> SELECT*FROM ORDERS WHERE TOTAL_AMOUNT BETWEEN 500 AND 1500;
+------+---------------+------------+--------------+
| id   | customer_name | order_date | total_amount |
+------+---------------+------------+--------------+
|    1 | Alice         | 2024-03-01 |      1500.00 |
|    4 | Diana         | 2024-03-15 |       800.00 |
|    5 | Eve           | 2024-03-20 |      1200.00 |
|    8 | Henry         | 2024-04-08 |       950.00 |
|   10 | Jack          | 2024-04-18 |       650.00 |
|   12 | Lily          | 2024-05-01 |      1350.00 |
|   15 | Oliver        | 2024-05-25 |       900.00 |
+------+---------------+------------+--------------+
7 rows in set (0.00 sec)

mysql> --INCREASE PRICE TO 1000^C
mysql> UPDATE ORDERS SET TOTAL_AMOUNT=TOTAL_AMOUNT+1000 WHERE ORDER_DATE BETWEEN '2024-03-04' AND '2024-03-10';
Query OK, 2 rows affected (0.01 sec)
Rows matched: 2  Changed: 2  Warnings: 0

mysql> SELECT*FROM ORDERS;
+------+---------------+------------+--------------+
| id   | customer_name | order_date | total_amount |
+------+---------------+------------+--------------+
|    1 | Alice         | 2024-03-01 |      1500.00 |
|    2 | Bob           | 2024-03-05 |      1450.00 |
|    3 | Charlie       | 2024-03-10 |      3500.00 |
|    4 | Diana         | 2024-03-15 |       800.00 |
|    5 | Eve           | 2024-03-20 |      1200.00 |
|    6 | Frank         | 2024-03-25 |      3000.00 |
|    7 | Grace         | 2024-04-02 |      1800.00 |
|    8 | Henry         | 2024-04-08 |       950.00 |
|    9 | Ivy           | 2024-04-12 |      2750.00 |
|   10 | Jack          | 2024-04-18 |       650.00 |
|   11 | Kevin         | 2024-04-22 |      4200.00 |
|   12 | Lily          | 2024-05-01 |      1350.00 |
|   13 | Michael       | 2024-05-08 |      5000.00 |
|   14 | Nancy         | 2024-05-15 |      2250.00 |
|   15 | Oliver        | 2024-05-25 |       900.00 |
+------+---------------+------------+--------------+
15 rows in set (0.00 sec)

mysql> --AMOUNT REDUCE BY 200 FOR ORDERS BETWEEN 1000 TO 2000^C
mysql> SELECT*FROM ORDERS SET TOTAL_AMOUNT=TOTAL_AMOUNT-200 WHERE TOTAL_AMOUNT BETWEEN 1000 AND 2000;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'SET TOTAL_AMOUNT=TOTAL_AMOUNT-200 WHERE TOTAL_AMOUNT BETWEEN 1000 AND 2000' at line 1
mysql> UPDATE ORDERS SET TOTAL_AMOUNT=TOTAL_AMOUNT-200 WHERE TOTAL_AMOUNT BETWEEN 1000 AND 2000;
Query OK, 5 rows affected (0.01 sec)
Rows matched: 5  Changed: 5  Warnings: 0

mysql> SELECT*FROM ORDERS;
+------+---------------+------------+--------------+
| id   | customer_name | order_date | total_amount |
+------+---------------+------------+--------------+
|    1 | Alice         | 2024-03-01 |      1300.00 |
|    2 | Bob           | 2024-03-05 |      1250.00 |
|    3 | Charlie       | 2024-03-10 |      3500.00 |
|    4 | Diana         | 2024-03-15 |       800.00 |
|    5 | Eve           | 2024-03-20 |      1000.00 |
|    6 | Frank         | 2024-03-25 |      3000.00 |
|    7 | Grace         | 2024-04-02 |      1600.00 |
|    8 | Henry         | 2024-04-08 |       950.00 |
|    9 | Ivy           | 2024-04-12 |      2750.00 |
|   10 | Jack          | 2024-04-18 |       650.00 |
|   11 | Kevin         | 2024-04-22 |      4200.00 |
|   12 | Lily          | 2024-05-01 |      1150.00 |
|   13 | Michael       | 2024-05-08 |      5000.00 |
|   14 | Nancy         | 2024-05-15 |      2250.00 |
|   15 | Oliver        | 2024-05-25 |       900.00 |
+------+---------------+------------+--------------+
15 rows in set (0.00 sec)

mysql> --INCREASE 10%^C
mysql> UPDATE ORDERS SET TOTAL_AMOUNT=TOTAL_AMOUNT+(TOTAL_AMOUNT*0.10) WHERE TOTAL_AMOUNT BETWEEN 2500 AND 5000;
Query OK, 5 rows affected (0.01 sec)
Rows matched: 5  Changed: 5  Warnings: 0

mysql> SELECT*FROM ORDERS;
+------+---------------+------------+--------------+
| id   | customer_name | order_date | total_amount |
+------+---------------+------------+--------------+
|    1 | Alice         | 2024-03-01 |      1300.00 |
|    2 | Bob           | 2024-03-05 |      1250.00 |
|    3 | Charlie       | 2024-03-10 |      3850.00 |
|    4 | Diana         | 2024-03-15 |       800.00 |
|    5 | Eve           | 2024-03-20 |      1000.00 |
|    6 | Frank         | 2024-03-25 |      3300.00 |
|    7 | Grace         | 2024-04-02 |      1600.00 |
|    8 | Henry         | 2024-04-08 |       950.00 |
|    9 | Ivy           | 2024-04-12 |      3025.00 |
|   10 | Jack          | 2024-04-18 |       650.00 |
|   11 | Kevin         | 2024-04-22 |      4620.00 |
|   12 | Lily          | 2024-05-01 |      1150.00 |
|   13 | Michael       | 2024-05-08 |      5500.00 |
|   14 | Nancy         | 2024-05-15 |      2250.00 |
|   15 | Oliver        | 2024-05-25 |       900.00 |
+------+---------------+------------+--------------+
15 rows in set (0.00 sec)

mysql> --REMOVE PRODUCTS^C
mysql> REMOVE FROM ORDERS WHERE ORDER_DATE BETWEEN '2024-03-10' AND '2024-03-20';
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'REMOVE FROM ORDERS WHERE ORDER_DATE BETWEEN '2024-03-10' AND '2024-03-20'' at line 1
mysql> DELETE FROM ORDERS WHERE ORDER_DATE BETWEEN '2024-03-10' AND '2024-03-20';
Query OK, 3 rows affected (0.01 sec)

mysql> SELECT*FROM ORDERS;
+------+---------------+------------+--------------+
| id   | customer_name | order_date | total_amount |
+------+---------------+------------+--------------+
|    1 | Alice         | 2024-03-01 |      1300.00 |
|    2 | Bob           | 2024-03-05 |      1250.00 |
|    6 | Frank         | 2024-03-25 |      3300.00 |
|    7 | Grace         | 2024-04-02 |      1600.00 |
|    8 | Henry         | 2024-04-08 |       950.00 |
|    9 | Ivy           | 2024-04-12 |      3025.00 |
|   10 | Jack          | 2024-04-18 |       650.00 |
|   11 | Kevin         | 2024-04-22 |      4620.00 |
|   12 | Lily          | 2024-05-01 |      1150.00 |
|   13 | Michael       | 2024-05-08 |      5500.00 |
|   14 | Nancy         | 2024-05-15 |      2250.00 |
|   15 | Oliver        | 2024-05-25 |       900.00 |
+------+---------------+------------+--------------+
12 rows in set (0.00 sec)

mysql> CREATE TABLE Emp (
    ->  id INT,
    ->  name VARCHAR(100),
    ->  dept VARCHAR(20),
    ->  salary INT
    ->  );
Query OK, 0 rows affected (0.03 sec)

mysql>
mysql> -- STEP 2: Insert Records
mysql> INSERT INTO Emp VALUES
    ->  (1, 'Alice', 'HR', 35000),
    ->  (2, 'Bob', 'IT', 50000),
    ->  (3, 'Charlie', 'Finance', 45000),
    ->  (4, 'Diana', 'Marketing', 40000),
    ->  (5, 'Eve', 'IT', 55000),
    ->  (6, 'Frank', 'Finance', 48000),
    ->  (7, 'Grace', 'Sales', 37000),
    ->  (8, 'Henry', 'Admin', 42000),
    ->  (9, 'Ivy', 'HR', 39000),
    ->  (10, 'Jack', 'Sales', 46000),
    ->  (11, 'Kevin', 'IT', 60000),
    ->  (12, 'Lily', 'Marketing', 41000),
    ->  (13, 'Michael', 'Admin', 38000),
    ->  (14, 'Nancy', 'Finance', 52000),
    ->  (15, 'Oliver', 'HR', 43000);
Query OK, 15 rows affected (0.01 sec)
Records: 15  Duplicates: 0  Warnings: 0

mysql> SELECT*FROM EMP;
+------+---------+-----------+--------+
| id   | name    | dept      | salary |
+------+---------+-----------+--------+
|    1 | Alice   | HR        |  35000 |
|    2 | Bob     | IT        |  50000 |
|    3 | Charlie | Finance   |  45000 |
|    4 | Diana   | Marketing |  40000 |
|    5 | Eve     | IT        |  55000 |
|    6 | Frank   | Finance   |  48000 |
|    7 | Grace   | Sales     |  37000 |
|    8 | Henry   | Admin     |  42000 |
|    9 | Ivy     | HR        |  39000 |
|   10 | Jack    | Sales     |  46000 |
|   11 | Kevin   | IT        |  60000 |
|   12 | Lily    | Marketing |  41000 |
|   13 | Michael | Admin     |  38000 |
|   14 | Nancy   | Finance   |  52000 |
|   15 | Oliver  | HR        |  43000 |
+------+---------+-----------+--------+
15 rows in set (0.00 sec)

mysql> --GET EMPLOYESS FROM IT AND FINANCE DEPARTMENT^C
mysql> SELECT*FROM EMP WHERE DEPT IN('IT','FINANCE');
+------+---------+---------+--------+
| id   | name    | dept    | salary |
+------+---------+---------+--------+
|    2 | Bob     | IT      |  50000 |
|    3 | Charlie | Finance |  45000 |
|    5 | Eve     | IT      |  55000 |
|    6 | Frank   | Finance |  48000 |
|   11 | Kevin   | IT      |  60000 |
|   14 | Nancy   | Finance |  52000 |
+------+---------+---------+--------+
6 rows in set (0.00 sec)

mysql> --INCRESE SALARY FOR HR AND MARKETING FOR 2000^C
mysql> UPDATE EMP SET SALARY=SALARY+2000 WHERE DEPT IN('HR','MARKETING');
Query OK, 5 rows affected (0.01 sec)
Rows matched: 5  Changed: 5  Warnings: 0

mysql> SELECT*FROM EMP;
+------+---------+-----------+--------+
| id   | name    | dept      | salary |
+------+---------+-----------+--------+
|    1 | Alice   | HR        |  37000 |
|    2 | Bob     | IT        |  50000 |
|    3 | Charlie | Finance   |  45000 |
|    4 | Diana   | Marketing |  42000 |
|    5 | Eve     | IT        |  55000 |
|    6 | Frank   | Finance   |  48000 |
|    7 | Grace   | Sales     |  37000 |
|    8 | Henry   | Admin     |  42000 |
|    9 | Ivy     | HR        |  41000 |
|   10 | Jack    | Sales     |  46000 |
|   11 | Kevin   | IT        |  60000 |
|   12 | Lily    | Marketing |  43000 |
|   13 | Michael | Admin     |  38000 |
|   14 | Nancy   | Finance   |  52000 |
|   15 | Oliver  | HR        |  45000 |
+------+---------+-----------+--------+
15 rows in set (0.00 sec)

mysql> --DELETE FINANACE AND MARKETING EMPLOYEES^C
mysql> DELETE FROM EMP WHERE DEPT IN('FINANCE','MARKETING');
Query OK, 5 rows affected (0.01 sec)

mysql> DELETE FROM EMP WHERE DEPT IN('SALES','IT');
Query OK, 5 rows affected (0.01 sec)

mysql> DELETE FROM EMP WHERE DEPT IN('ADMIN','HR');
Query OK, 5 rows affected (0.01 sec)

mysql> SELECT*FROM EMP;
Empty set (0.00 sec)

mysql> INSERT INTO Emp VALUES
    ->  (1, 'Rahul', 'IT', 50000),
    ->  (2, 'Ramesh', 'HR', 35000),
    ->  (3, 'Karan', 'Finance', 45000),
    ->  (4, 'Mahesh', 'Marketing', 40000),
    ->  (5, 'Suresh', 'IT', 55000),
    ->  (6, 'Arjun', 'Sales', 38000),
    ->  (7, 'Manish', 'Admin', 42000),
    ->  (8, 'Ganesh', 'Finance', 47000),
    ->  (9, 'Naresh', 'HR', 39000),
    ->  (10, 'Rohan', 'IT', 52000),
    ->  (11, 'Mohan', 'Sales', 41000),
    ->  (12, 'Kishan', 'Marketing', 43000),
    ->  (13, 'Dinesh', 'Admin', 46000),
    ->  (14, 'Rajesh', 'Finance', 51000),
    ->  (15, 'Kiran', 'IT', 48000);
Query OK, 15 rows affected (0.01 sec)
Records: 15  Duplicates: 0  Warnings: 0

mysql> SELECT*FROM EMP;
+------+--------+-----------+--------+
| id   | name   | dept      | salary |
+------+--------+-----------+--------+
|    1 | Rahul  | IT        |  50000 |
|    2 | Ramesh | HR        |  35000 |
|    3 | Karan  | Finance   |  45000 |
|    4 | Mahesh | Marketing |  40000 |
|    5 | Suresh | IT        |  55000 |
|    6 | Arjun  | Sales     |  38000 |
|    7 | Manish | Admin     |  42000 |
|    8 | Ganesh | Finance   |  47000 |
|    9 | Naresh | HR        |  39000 |
|   10 | Rohan  | IT        |  52000 |
|   11 | Mohan  | Sales     |  41000 |
|   12 | Kishan | Marketing |  43000 |
|   13 | Dinesh | Admin     |  46000 |
|   14 | Rajesh | Finance   |  51000 |
|   15 | Kiran  | IT        |  48000 |
+------+--------+-----------+--------+
15 rows in set (0.00 sec)

mysql> --DISPLAY EMPLOYEES WHOSE NAMES START WITH 'R'^C
mysql> SELECT*FROM EMP
    -> WHERE NAME LIKE 'R%';
+------+--------+---------+--------+
| id   | name   | dept    | salary |
+------+--------+---------+--------+
|    1 | Rahul  | IT      |  50000 |
|    2 | Ramesh | HR      |  35000 |
|   10 | Rohan  | IT      |  52000 |
|   14 | Rajesh | Finance |  51000 |
+------+--------+---------+--------+
4 rows in set (0.00 sec)

mysql> SELECT*FROM EMP
    -> WHERE NAME LIKE '%SH';
+------+--------+-----------+--------+
| id   | name   | dept      | salary |
+------+--------+-----------+--------+
|    2 | Ramesh | HR        |  35000 |
|    4 | Mahesh | Marketing |  40000 |
|    5 | Suresh | IT        |  55000 |
|    7 | Manish | Admin     |  42000 |
|    8 | Ganesh | Finance   |  47000 |
|    9 | Naresh | HR        |  39000 |
|   13 | Dinesh | Admin     |  46000 |
|   14 | Rajesh | Finance   |  51000 |
+------+--------+-----------+--------+
8 rows in set (0.00 sec)

mysql> --DIAPLAY EMPLOYESS WHOSE NAMES CONTAIN 'AR'.
    -> ^C
mysql> SELECT*FROM EMP
    -> WHERE NAME LIKE '%AR';
Empty set (0.00 sec)

mysql> SELECT*FROM EMP
    -> ^C
mysql> WHERE NAME LIKE '%AR';
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'WHERE NAME LIKE '%AR'' at line 1
mysql> SELECT*FROM EMP
    -> SELECT*FROM E^C
mysql> ^C
mysql> SELECT*FROM EMP
    -> WHERE NAME LIKE'_____';
+------+-------+---------+--------+
| id   | name  | dept    | salary |
+------+-------+---------+--------+
|    1 | Rahul | IT      |  50000 |
|    3 | Karan | Finance |  45000 |
|    6 | Arjun | Sales   |  38000 |
|   10 | Rohan | IT      |  52000 |
|   11 | Mohan | Sales   |  41000 |
|   15 | Kiran | IT      |  48000 |
+------+-------+---------+--------+
6 rows in set (0.00 sec)

mysql> SELECT*FROM EMP
    -> WHERE NAME LIKE 'M%N';
+------+-------+-------+--------+
| id   | name  | dept  | salary |
+------+-------+-------+--------+
|   11 | Mohan | Sales |  41000 |
+------+-------+-------+--------+
1 row in set (0.00 sec)

mysql> --DISPLAY EMPLOYEES WHOSES NAME STARTS WITH M AND CONTAIN E
    -> ^C
mysql> SELECT*FROM EMP
    -> WHERE NAME LIKE 'M%E%';
+------+--------+-----------+--------+
| id   | name   | dept      | salary |
+------+--------+-----------+--------+
|    4 | Mahesh | Marketing |  40000 |
+------+--------+-----------+--------+
1 row in set (0.00 sec)

mysql> SELECT*FROM EMP
    -> WHERE NAME LIKE '_____H\';
    '> SELECT*FROM EMP^C
mysql> SELECT*FROM EMP
    -> WHERE NAME LIKE '_____H';
+------+--------+-----------+--------+
| id   | name   | dept      | salary |
+------+--------+-----------+--------+
|    2 | Ramesh | HR        |  35000 |
|    4 | Mahesh | Marketing |  40000 |
|    5 | Suresh | IT        |  55000 |
|    7 | Manish | Admin     |  42000 |
|    8 | Ganesh | Finance   |  47000 |
|    9 | Naresh | HR        |  39000 |
|   13 | Dinesh | Admin     |  46000 |
|   14 | Rajesh | Finance   |  51000 |
+------+--------+-----------+--------+
8 rows in set (0.00 sec)

mysql> SELECT*FROM EMP
    -> WHERE NAME LIKE 'AEIOU';
Empty set (0.00 sec)

mysql> SELECT*FROM EMP
    -> WHERE NAME LIKE 'A'
    -> OR NAME LIKE ^C
mysql> SELECT*FROM EMP
    -> WHERE NAME LIKE 'A%'
    -> OR NAME LIKE 'E%'
    -> OR NAME LIKE 'I%'
    -> OR NAME LIKE 'O%'
    -> OR NAME LIKE 'U%';
+------+-------+-------+--------+
| id   | name  | dept  | salary |
+------+-------+-------+--------+
|    6 | Arjun | Sales |  38000 |
+------+-------+-------+--------+
1 row in set (0.00 sec)

mysql> CREATE DATABASE NEWDA4;
Query OK, 1 row affected (0.01 sec)

mysql> USE NEWDA4;
Database changed
mysql> CREATE TABLE employees (
    ->     emp_id INT PRIMARY KEY,
    ->     emp_name VARCHAR(50),
    ->     department VARCHAR(30),
    ->     salary DECIMAL(10,2),
    ->     experience INT,
    ->     age INT
    -> );
Query OK, 0 rows affected (0.02 sec)

mysql>
mysql> INSERT INTO employees VALUES
    -> (101,'Ravi','IT',65000,5,28),
    -> (102,'Priya','HR',45000,2,24),
    -> (103,'Amit','Finance',75000,8,35),
    -> (104,'Sneha','IT',55000,3,27),
    -> (105,'Rahul','Sales',40000,1,22),
    -> (106,'Kiran','Finance',90000,12,40),
    -> (107,'Anjali','HR',52000,4,29),
    -> (108,'Suresh','Sales',68000,7,33);
Query OK, 8 rows affected (0.00 sec)
Records: 8  Duplicates: 0  Warnings: 0

mysql>
mysql>
mysql> SELECT*FROM EMPLOYEES;
+--------+----------+------------+----------+------------+------+
| emp_id | emp_name | department | salary   | experience | age  |
+--------+----------+------------+----------+------------+------+
|    101 | Ravi     | IT         | 65000.00 |          5 |   28 |
|    102 | Priya    | HR         | 45000.00 |          2 |   24 |
|    103 | Amit     | Finance    | 75000.00 |          8 |   35 |
|    104 | Sneha    | IT         | 55000.00 |          3 |   27 |
|    105 | Rahul    | Sales      | 40000.00 |          1 |   22 |
|    106 | Kiran    | Finance    | 90000.00 |         12 |   40 |
|    107 | Anjali   | HR         | 52000.00 |          4 |   29 |
|    108 | Suresh   | Sales      | 68000.00 |          7 |   33 |
+--------+----------+------------+----------+------------+------+
8 rows in set (0.00 sec)

mysql> SELECT EMP_NAME,SALARY
    -> ^C
mysql> SELECT EMP_NAME,SALARY,
    -> CASE
    -> WHEN SALARY>=80000 THE 'HIGH_SALARY'
    -> WHEN SALARY>=60000 ^C
mysql> SELECT EMP_NAME,SALARY,
    -> CASE
    -> WHEN SALARY>=80000 THEN 'HIGH_SALARY'
    -> WHEN SALARY>=60000 THEN 'MEDIUM_SALARY'
    -> ELSE 'LOW_SALARY'
    -> END AS SALARY_CATEGORY
    -> FROM EMPLOYEES;
+----------+----------+-----------------+
| EMP_NAME | SALARY   | SALARY_CATEGORY |
+----------+----------+-----------------+
| Ravi     | 65000.00 | MEDIUM_SALARY   |
| Priya    | 45000.00 | LOW_SALARY      |
| Amit     | 75000.00 | MEDIUM_SALARY   |
| Sneha    | 55000.00 | LOW_SALARY      |
| Rahul    | 40000.00 | LOW_SALARY      |
| Kiran    | 90000.00 | HIGH_SALARY     |
| Anjali   | 52000.00 | LOW_SALARY      |
| Suresh   | 68000.00 | MEDIUM_SALARY   |
+----------+----------+-----------------+
8 rows in set (0.00 sec)

mysql> -->=10 EXPERT >=5 SENIOR >=2 JUNIOR ELSE FRESHER^C
mysql> SELECT EMP_NAME,EXPERIENCE,
    -> CASE
    -> WHEN EXPERIENCE>=80000 THEN 'HIGH_SALARY'
    -> WHEN EXPERIENCE>=80000 THEN 'HIGH_SALARY'^C
mysql> SELECT EMP_NAME,EXPERIENCE,
    -> CASE
    -> WHEN EXPERIENCE>=10 THEN 'EXPERT'
    -> WHEN EXPERIENCE>=5 THEN 'SENIOR'
    -> WHEN EXPERIENCE>=2 THEN 'JUNIOR'
    -> ELSE 'FRESHER'
    -> END AS EXPERIENCE_CATEGORY
    -> FROM EMPLOYEES;
+----------+------------+---------------------+
| EMP_NAME | EXPERIENCE | EXPERIENCE_CATEGORY |
+----------+------------+---------------------+
| Ravi     |          5 | SENIOR              |
| Priya    |          2 | JUNIOR              |
| Amit     |          8 | SENIOR              |
| Sneha    |          3 | JUNIOR              |
| Rahul    |          1 | FRESHER             |
| Kiran    |         12 | EXPERT              |
| Anjali   |          4 | JUNIOR              |
| Suresh   |          7 | SENIOR              |
+----------+------------+---------------------+
8 rows in set (0.00 sec)

mysql> SELECT EMP_NAME,AGE,
    -> CASE
    -> WHEN AGE>=18 THEN 'ELIGIBLE_TO_VOTE'
    -> ELSE 'NOT_ELIGIBLE
    '> END AS ELIGIBILITY
    '> FROM EMPLOYEES;
    '> ^C
mysql> SELECT EMP_NAME,AGE,
    -> CASE
    -> WHEN AGE>=18 THEN 'ELIGIBLE_TO_VOTE'
    -> ELSE 'NOT_ELIGIBLE'
    -> END AS ELIGIBILITY
    -> FROM EMPLOYEES;
+----------+------+------------------+
| EMP_NAME | AGE  | ELIGIBILITY      |
+----------+------+------------------+
| Ravi     |   28 | ELIGIBLE_TO_VOTE |
| Priya    |   24 | ELIGIBLE_TO_VOTE |
| Amit     |   35 | ELIGIBLE_TO_VOTE |
| Sneha    |   27 | ELIGIBLE_TO_VOTE |
| Rahul    |   22 | ELIGIBLE_TO_VOTE |
| Kiran    |   40 | ELIGIBLE_TO_VOTE |
| Anjali   |   29 | ELIGIBLE_TO_VOTE |
| Suresh   |   33 | ELIGIBLE_TO_VOTE |
+----------+------+------------------+
8 rows in set (0.00 sec)
