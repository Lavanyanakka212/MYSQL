Stored procedures
Queries without parameters
========================
mysql> use pfs4;
Database changed
mysql> select*from employees;
+--------+----------+------------+----------+------------+-----------+
| emp_id | emp_name | department | salary   | experience | city      |
+--------+----------+------------+----------+------------+-----------+
|    101 | Rahul    | IT         | 65000.00 |          5 | Hyderabad |
|    102 | Priya    | HR         | 45000.00 |          3 | Chennai   |
|    103 | Amit     | Finance    | 70000.00 |          6 | Bangalore |
|    104 | Sneha    | IT         | 80000.00 |          8 | Hyderabad |
|    105 | Kiran    | Sales      | 40000.00 |          2 | Pune      |
|    106 | Ravi     | HR         | 50000.00 |          4 | Mumbai    |
|    107 | Anjali   | IT         | 90000.00 |         10 | Delhi     |
|    108 | Suresh   | Finance    | 55000.00 |          5 | Chennai   |
|    109 | Divya    | Sales      | 48000.00 |          3 | Hyderabad |
|    110 | Vikram   | IT         | 75000.00 |          7 | Bangalore |
+--------+----------+------------+----------+------------+-----------+
10 rows in set (0.05 sec)

mysql> DELIMITER //
mysql> CREATE PROCEDURE DEPARTMENTWISECOUNT()
    -> BEGIN
    -> SELECT DEPARTMENT,
    -> COUNT(*)AS TOTALEMPLOYEES
    -> FROM EMPLOYEES
    -> GROUP BY DEPARTMENT;
    -> END //
Query OK, 0 rows affected (0.05 sec)

mysql> DELIMITER ;
mysql> CALL DEPARTMENTWISECOUNT();
+------------+----------------+
| DEPARTMENT | TOTALEMPLOYEES |
+------------+----------------+
| IT         |              4 |
| HR         |              2 |
| Finance    |              2 |
| Sales      |              2 |
+------------+----------------+
4 rows in set (0.02 sec)

mysql> SHOW PROCEDURE STATUS
    -> WHERE Db='pfs4';
+------+---------------------+-----------+----------------+---------------------+---------------------+---------------+---------+----------------------+----------------------+--------------------+
| Db   | Name                | Type      | Definer        | Modified            | Created             | Security_type | Comment | character_set_client | collation_connection | Database Collation |
+------+---------------------+-----------+----------------+---------------------+---------------------+---------------+---------+----------------------+----------------------+--------------------+
| pfs4 | DEPARTMENTWISECOUNT | PROCEDURE | root@localhost | 2026-08-05 09:06:42 | 2026-08-05 09:06:42 | DEFINER       |         | cp850                | cp850_general_ci     | utf8mb4_0900_ai_ci |
| pfs4 | EMPLOYEENAME        | PROCEDURE | root@localhost | 2026-08-04 11:09:10 | 2026-08-04 11:09:10 | DEFINER       |         | cp850                | cp850_general_ci     | utf8mb4_0900_ai_ci |
| pfs4 | GETALLEMPLOYEES     | PROCEDURE | root@localhost | 2026-08-04 11:00:31 | 2026-08-04 11:00:31 | DEFINER       |         | cp850                | cp850_general_ci     | utf8mb4_0900_ai_ci |
| pfs4 | GETITEMPLOYEES      | PROCEDURE | root@localhost | 2026-08-04 11:04:52 | 2026-08-04 11:04:52 | DEFINER       |         | cp850                | cp850_general_ci     | utf8mb4_0900_ai_ci |
+------+---------------------+-----------+----------------+---------------------+---------------------+---------------+---------+----------------------+----------------------+--------------------+
4 rows in set (0.07 sec)



Query OK, 0 rows affected (0.03 sec)

===============================================

using parameters

 --IN PARAMETERS
 --EMPLOYEE BY ID

 DELIMITER //
mysql> CREATE PROCEDURE getEmployeeById(IN eid INT)
    -> BEGIN
    -> SELECT*FROM EMPLOYEES
    -> WHERE EMP_ID=EID;
    -> END //
Query OK, 0 rows affected (0.10 sec)

mysql> DELIMITER ;
mysql> CALL getEmployeeById(101);
+--------+----------+------------+----------+------------+-----------+
| emp_id | emp_name | department | salary   | experience | city      |
+--------+----------+------------+----------+------------+-----------+
|    101 | Rahul    | IT         | 65000.00 |          5 | Hyderabad |
+--------+----------+------------+----------+------------+-----------+
1 row in set (0.01 sec)

Query OK, 0 rows affected (0.01 sec)

--Employee by dept

mysql> DELIMITER //
mysql> CREATE PROCEDURE getEmployeeByDepartment(IN dept VARCHAR(30))
    -> BEGIN
    -> SELECT*FROM EMPLOYEES
    -> WHERE DEPARTMENT=DEPT;
    -> END //
Query OK, 0 rows affected (0.01 sec)

mysql> DELIMITER ;
mysql> CALL getEmployeeByDepartment('IT');
+--------+----------+------------+----------+------------+-----------+
| emp_id | emp_name | department | salary   | experience | city      |
+--------+----------+------------+----------+------------+-----------+
|    101 | Rahul    | IT         | 65000.00 |          5 | Hyderabad |
|    104 | Sneha    | IT         | 80000.00 |          8 | Hyderabad |
|    107 | Anjali   | IT         | 90000.00 |         10 | Delhi     |
|    110 | Vikram   | IT         | 75000.00 |          7 | Bangalore |
+--------+----------+------------+----------+------------+-----------+
4 rows in set (0.01 sec)

Query OK, 0 rows affected (0.02 sec)

using 2 parameters
------------------

mysql> DELIMITER //
mysql> CREATE PROCEDURE salaryRange(IN minSal DECIMAL(10,2), IN maxSal DECIMAL(10,2))
    -> BEGIN
    -> SELECT*FROM EMPLOYEES
    -> WHERE SALARY BETWEEN minSal AND maxSal;
    -> END //
Query OK, 0 rows affected (0.02 sec)

mysql> DELIMITER ;
mysql> CALL salaryRange(40000,70000);
+--------+----------+------------+----------+------------+-----------+
| emp_id | emp_name | department | salary   | experience | city      |
+--------+----------+------------+----------+------------+-----------+
|    101 | Rahul    | IT         | 65000.00 |          5 | Hyderabad |
|    102 | Priya    | HR         | 45000.00 |          3 | Chennai   |
|    103 | Amit     | Finance    | 70000.00 |          6 | Bangalore |
|    105 | Kiran    | Sales      | 40000.00 |          2 | Pune      |
|    106 | Ravi     | HR         | 50000.00 |          4 | Mumbai    |
|    108 | Suresh   | Finance    | 55000.00 |          5 | Chennai   |
|    109 | Divya    | Sales      | 48000.00 |          3 | Hyderabad |
+--------+----------+------------+----------+------------+-----------+
7 rows in set (0.01 sec)

Query OK, 0 rows affected (0.02 sec)



mysql> DELIMITER //
mysql> CREATE PROCEDURE DeptExperience(IN dept VARCHAR(30), IN exp INT)
    -> BEGIN
    -> SELECT*FROM EMPLOYEES
    -> WHERE department=dept
    -> AND experience>=exp;
    -> END //
Query OK, 0 rows affected (0.01 sec)

mysql> DELIMITER ;
mysql> CALL DeptExperience('IT',5);
+--------+----------+------------+----------+------------+-----------+
| emp_id | emp_name | department | salary   | experience | city      |
+--------+----------+------------+----------+------------+-----------+
|    101 | Rahul    | IT         | 65000.00 |          5 | Hyderabad |
|    104 | Sneha    | IT         | 80000.00 |          8 | Hyderabad |
|    107 | Anjali   | IT         | 90000.00 |         10 | Delhi     |
|    110 | Vikram   | IT         | 75000.00 |          7 | Bangalore |
+--------+----------+------------+----------+------------+-----------+
4 rows in set (0.01 sec)

Query OK, 0 rows affected (0.02 sec)

=======================
--OUT PARAMETER
--TOTAL EMPLOYEES COUNT


mysql> DELIMITER //
mysql> CREATE PROCEDURE totalEmployees(OUT total INT)
    -> BEGIN
    -> SELECT COUNT(*)INTO TOTAL
    -> FROM EMPLOYEES;
    -> END //
Query OK, 0 rows affected (0.02 sec)

mysql> DELIMITER ;
mysql> CALL totalEMployees(@total);
Query OK, 1 row affected (0.04 sec)

mysql> select@total;
+--------+
| @total |
+--------+
|     10 |
+--------+
1 row in set (0.00 sec)

mysql> DELIMITER //
mysql>  CREATE PROCEDURE itEmployeesCount(OUT cnt INT)
    ->      BEGIN
    ->      SELECT COUNT(*)
    ->      INTO CNT
    ->      FROM EMPLOYEES
    ->      WHERE DEPARTMENT='IT';
    ->      END //
Query OK, 0 rows affected (0.03 sec)

mysql>
mysql> DELIMITER ;
mysql> CALL itEmployeesCount(@cnt);
Query OK, 1 row affected (0.01 sec)

mysql> SELECT@cnt;
+------+
| @cnt |
+------+
|    4 |
+------+
1 row in set (0.01 sec)


===========================
IN-OUT PARAMETER
----------------

mysql> DELIMITER //
mysql> CREATE PROCEDURE AddBounus(
    -> IN empid INT,
    -> INOUT bonus DECIMAL(10,2)
    -> )
    -> BEGIN
    -> UPDATE Employees
    -> SET salary = salary + bonus
    -> WHERE emp_id = empid;
    -> SELECT  salary
    -> INTO bonus
    -> FROM Employees
    -> WHERE emp_id = empid;
    -> END //
Query OK, 0 rows affected (0.02 sec)

mysql> DELIMITER ;
mysql> SET @b=5000;
Query OK, 0 rows affected (0.01 sec)

mysql> CALL AddBounus(101,@b);
Query OK, 1 row affected (0.03 sec)

mysql> SELECT @B;
+----------+
| @B       |
+----------+
| 70000.00 |
+----------+
1 row in set (0.00 sec)


mysql> CALL AddBounus(102,@b);
Query OK, 1 row affected (0.01 sec)

mysql> SELECT @B;
+-----------+
| @B        |
+-----------+
| 115000.00 |
+-----------+
1 row in set (0.00 sec)

-- DETECT----

mysql> DELIMITER //
mysql> CREATE PROCEDURE DeductSalary(
    ->      IN empid INT,
    ->      INOUT amount DECIMAL(10,2)
    ->      )
    ->      BEGIN
    ->      UPDATE Employees
    ->      SET salary = salary - amount
    ->      WHERE emp_id = empid;
    ->      SELECT  salary
    ->      INTO amount
    ->      FROM Employees
    ->      WHERE emp_id = empid;
    ->      END //
Query OK, 0 rows affected (0.02 sec)

mysql> DELIMITER ;
mysql> SET @deduction = 5000;
Query OK, 0 rows affected (0.00 sec)

mysql> CALl DeductSalary(103,@deduction);
Query OK, 1 row affected (0.01 sec)

mysql> select @deduction;
+------------+
| @deduction |
+------------+
|   65000.00 |
+------------+
1 row in set (0.00 sec)

================================================
Introduction to Triggers 

A trigger is a special type of stored program that automatically executes in a response to a specific event INSERT,UPDATE, OR DELETE....
--> Occurring on a specific table.
unlike a stored procedure a trigger is never called directly . the database engine invokes automatically when the trigger event happens.

Syntax
------

DELIMITER //

CREATE TRIGGER trigger_name
{BEFORE | AFTER} {INSERT|UPDATE |DELETE}
ON table_name
FOR EACH ROW
BEGIN
     ---trigger logic
     ---use NEW.column_name for inserted/updated values
     ---use OLD.column_name for deleted/previous values
END //

DELIMITER ;

Keyword Meaning
BEFORE:- Trigger fires before the triggering event is applied to the table. Often used for validation.
After:-  Trigger fires 





=========================
QUERIES

CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(30),
    salary DECIMAL(10,2),
    experience INT,
    city VARCHAR(30)
);



INSERT INTO Employees VALUES
(101,'Rahul','IT',65000,5,'Hyderabad'),
(102,'Priya','HR',45000,3,'Chennai'),
(103,'Amit','Finance',70000,6,'Bangalore'),
(104,'Sneha','IT',80000,8,'Hyderabad'),
(105,'Kiran','Sales',40000,2,'Pune');




CREATE TABLE Employee_Audit(
    audit_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT,
    action_type VARCHAR(20),
    old_salary DECIMAL(10,2),
    new_salary DECIMAL(10,2),
    action_time DATETIME
);


mysql> SELECT*FROM EMPLOYEES;
+--------+----------+------------+----------+------------+-----------+
| emp_id | emp_name | department | salary   | experience | city      |
+--------+----------+------------+----------+------------+-----------+
|    101 | Rahul    | IT         | 65000.00 |          5 | Hyderabad |
|    102 | Priya    | HR         | 45000.00 |          3 | Chennai   |
|    103 | Amit     | Finance    | 70000.00 |          6 | Bangalore |
|    104 | Sneha    | IT         | 80000.00 |          8 | Hyderabad |
|    105 | Kiran    | Sales      | 40000.00 |          2 | Pune      |
+--------+----------+------------+----------+------------+-----------+
5 rows in set (0.00 sec)

BEFORE
------

mysql> DELIMITER //
mysql> CREATE TRIGGER trg_before_insert_salary
    -> BEFORE INSERT
    -> ON EMPLOYEES
    -> FOR EACH ROW
    -> BEGIN
    -> IF NEW.SALARY<20000 THEN
    -> SIGNAL SQLSTATE '45000'
    -> SET MESSAGE_TEXT ='SALARY CANNOT BE LESS THAN 20000';
    -> END IF;
    -> END //
Query OK, 0 rows affected (0.03 sec)

mysql> DELIMITER ;
mysql> INSERT INTO EMPLOYEES VALUES(106,'ARJUN','IT',15000,3,'DELHI');
ERROR 1644 (45000): SALARY CANNOT BE LESS THAN 20000
