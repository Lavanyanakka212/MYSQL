day 17 STORED PROCEDURED 
----------------
It is a named, precompiled collection of one or more SQL statements that are stored inside the database and can be executed or called whenever required, instead of sending a long block of SQL from an application every time, the application simply calls the procedure by name 

they can accept parameters, perform logic(loops, conditions, variables declaration)and return results

why use of this?
---------------
performance:-precompiled catched by the database engine ,so repeated execution is faster than sending raw sql each time

reusability:- write the logic ones and call it from many applications or scripts 

security:-users can be granted execute permission on a procedure without granting direct access to the underline tables

reduced network traffic:- a single call statement replaces many line of SQL sent over the network

maintainability:- business logic is centralized in the database, so changes are made in one place 

consistency:- ensures the same validation/business rules are applied every time ,regardless of which application calls it

Advantages:-
-----------
faster execution after compilation
reduced duplicate SQL
supports transactions, loops ,conditions, variables, cursors, and execution handlers
easy maintenance

disadvantages:-
----------------
debugging can be difficult.
vender specific syntax
complex procedures may become hard to maintain

create procedure:-
syntax:-
delimiter//

create procedure procedure_name(
in|out|inout|parameter name data-type,..
)
begin
...............SQL statemenet or logic
..............declaration,condition,loops..etc
end//


**mysql> SELECT\*FROM EMPLOYEES;**

**+--------+----------+------------+----------+------------+-----------+**

**| emp\_id | emp\_name | department | salary   | experience | city      |**

**+--------+----------+------------+----------+------------+-----------+**

**|    101 | Rahul    | IT         | 65000.00 |          5 | Hyderabad |**

**|    102 | Priya    | HR         | 45000.00 |          3 | Chennai   |**

**|    103 | Amit     | Finance    | 70000.00 |          6 | Bangalore |**

**|    104 | Sneha    | IT         | 80000.00 |          8 | Hyderabad |**

**|    105 | Kiran    | Sales      | 40000.00 |          2 | Pune      |**

**|    106 | Ravi     | HR         | 50000.00 |          4 | Mumbai    |**

**|    107 | Anjali   | IT         | 90000.00 |         10 | Delhi     |**

**|    108 | Suresh   | Finance    | 55000.00 |          5 | Chennai   |**

**|    109 | Divya    | Sales      | 48000.00 |          3 | Hyderabad |**

**|    110 | Vikram   | IT         | 75000.00 |          7 | Bangalore |**

**+--------+----------+------------+----------+------------+-----------+**


mysql> SHOW PROCEDURE STATUS   # to see the procedures.**

&#x20;   **-> WHERE Db = 'pfs4';

**mysql> DELIMITER //**

**mysql> CREATE PROCEDURE GETITEMPLOYEES()**

&#x20;   **-> BEGIN**

&#x20;   **->     SELECT\*FROM EMPLOYEES**

&#x20;   **-> WHERE DEPARTMENT='IT';**

&#x20;   **-> END //**

**Query OK, 0 rows affected (0.01 sec)**



**mysql> DELIMITER ;**

**mysql> CALL GETITEMPLOYEES();**

**+--------+----------+------------+----------+------------+-----------+**

**| emp\_id | emp\_name | department | salary   | experience | city      |**

**+--------+----------+------------+----------+------------+-----------+**

**|    101 | Rahul    | IT         | 65000.00 |          5 | Hyderabad |**

**|    104 | Sneha    | IT         | 80000.00 |          8 | Hyderabad |**

**|    107 | Anjali   | IT         | 90000.00 |         10 | Delhi     |**

**|    110 | Vikram   | IT         | 75000.00 |          7 | Bangalore |**

**+--------+----------+------------+----------+------------+-----------+**

**4 rows in set (0.00 sec)**



delimeter //
create procedure salaryrange(IN minsal DECIMAL (10,2),IN maxsal DECIMAL(10,2))
begin 
select*from employees
where salary between minsal and maxsal;
end//

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

--
create procedure DeptExperience(IN dept VARCHAR(30),IN exp INT)
BEGIN
SELECT*FROM EMPLOYEES
WHERE DEPARTMENT=dept
AND EXPERIENCE>=exp
END//
~
DELIMITER;
CALL DeptExperience('IT',5);


--
OUT PARAMETER
==============
DELIMITER //
CREATE PROCEDURE TOTALEMPLOYEES(OUT TOTAL INT)
BEGIN
SELECT COUNT(*)TOTAL
FROM EMPLOYEES;
END //
~
DELIMITER;
CALL TOTALEMPLOYEES(@TOTAL);
~
SELECT@TOTAL;
+--------+
| @total |
+--------+
|     10 |
+--------+

--
DELIMITER //
CREATE PROCEDURE ITEMPLOYEESCOUNT(OUT TOTAL INT)
BEGIN
SELECT COUNT(*)
INTO TOTAL
FROM EMPLOYEES
WHERE DEPARTMENT='IT';
END //
~
DELIMITER;
CALL ITEMPLOYEESCOUNT(@TOTAL);

--
INOUT PARAMETER
================
DELIMITER //
CREATE PROCEDURE ADDBONUS(IN EMPID INT;
                          INOUT BONUS DECIMAL(10,2)
BEGIN
UPDATE EMPLOYEES
SET SALARY =SALARY+BONUS
WHERE EMP_ID = EMPID;

SELECT SALARY
INTO BONUS
FROM EMPLOYEES
WHERE EMP_ID = EMPID;
END //
~
DELIMITER;
SET @B=5000;
~
CALL ADDBONUS(101,@B)

--------------

DELIMITER //
CREATE PROCEDURE DEDUCTSALARY(IN EMPID INT;
                          INOUT BONUS DECIMAL(10,2)
BEGIN
UPDATE EMPLOYEES
SET SALARY =SALARY-AMOUNT
WHERE EMP_ID = EMPID;

SELECT SALARY
INTO AMOUNT
FROM EMPLOYEES
WHERE EMP_ID = EMPID;
END //
~
DELIMITER;
SET @DEDUCTION=5000;
~
CALL DEDUCTSALARY(103,@DEDUCTION)
SELECT @DEDUCTION;
+------------+
| @deduction |
+------------+
|       5000 |
+------------+


