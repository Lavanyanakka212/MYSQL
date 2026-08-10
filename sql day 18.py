**Queries**

**-------**

1. **FIND THE CITIES IN THE COUNTRY HAVE THE SAME CONTINENT HAS THE COUNTRY WITH LARGEST POPULATION.**



**mysql> SELECT C.NAME,C.POPULATION,CO.NAME AS COUNTRYNAME**

&#x20;   **-> FROM CITY C**

&#x20;   **-> JOIN COUNTRY CO ON**

&#x20;   **-> C.COUNTRYCODE=CO.CODE**

&#x20;   **-> WHERE CO.CONTINENT=**

&#x20;   **-> (SELECT CONTINENT FROM COUNTRY WHERE POPULATION=(SELECT MAX(POPULATION)FROM COUNTRY));**

**+------------------+------------+--------------+**

**| NAME             | POPULATION | COUNTRYNAME  |**

**+------------------+------------+--------------+**

**| Dhaka            |   22400000 | Bangladesh   |**

**| Chittagong       |    5200000 | Bangladesh   |**

**| Beijing          |   21890000 | China        |**

**| Shanghai         |   24870000 | China        |**

**| Shenzhen         |   17560000 | China        |**

**| Jakarta          |   10900000 | Indonesia    |**

**| Surabaya         |    2870000 | Indonesia    |**

**| New Delhi        |   34700000 | India        |**

**| Mumbai           |   21300000 | India        |**

**| Bengaluru        |   13600000 | India        |**

**| Tokyo            |   37400000 | Japan        |**

**| Osaka            |   19100000 | Japan        |**

**| Seoul            |    9500000 | South Korea  |**

**| Busan            |    3400000 | South Korea  |**

**| Islamabad        |    1140000 | Pakistan     |**

**| Karachi          |   16800000 | Pakistan     |**

**| Lahore           |   13000000 | Pakistan     |**

**| Riyadh           |    7680000 | Saudi Arabia |**

**| Jeddah           |    4780000 | Saudi Arabia |**

**| Bangkok          |   10700000 | Thailand     |**

**| Chiang Mai       |    1200000 | Thailand     |**

**| Hanoi            |    8400000 | Vietnam      |**

**| Ho Chi Minh City |    9300000 | Vietnam      |**

**+------------------+------------+--------------+**

**23 rows in set (0.01 sec)**



**2.FIND THE COUNTRIES WHERE THE CAPITAL CITY HAS ABOVE AVERAGE-POPULATION FOR THAT COUNTRY.**



**mysql> SELECT CO.NAME AS COUNTRYNAME,CAP.NAME AS CAPITALNAME,CAP.POPULATION**

&#x20;   **-> FROM COUNTRY CO**

&#x20;   **-> JOIN CITY CAP**

&#x20;   **-> ON CO.CAPITAL=CAP.ID**

&#x20;   **-> WHERE CAP.POPULATION>(SELECT AVG(C.POPULATION)**

&#x20;   **->                            FROM CITY C**

&#x20;   **->                              WHERE COUNTRYCODE=CO.CODE);**

**+----------------+--------------+------------+**

**| COUNTRYNAME    | CAPITALNAME  | POPULATION |**

**+----------------+--------------+------------+**

**| Argentina      | Buenos Aires |    3080000 |**

**| Belgium        | Brussels     |    1220000 |**

**| Bangladesh     | Dhaka        |   22400000 |**

**| Chile          | Santiago     |    6270000 |**

**| China          | Beijing      |   21890000 |**

**| Colombia       | Bogota       |    7970000 |**

**| Germany        | Berlin       |    3677000 |**

**| Algeria        | Algiers      |    2760000 |**

**| Egypt          | Cairo        |   10100000 |**

**| Spain          | Madrid       |    3280000 |**

**| France         | Paris        |    2140000 |**

**| United Kingdom | London       |    8980000 |**

**| Greece         | Athens       |     660000 |**

**| Indonesia      | Jakarta      |   10900000 |**

**| India          | New Delhi    |   34700000 |**

**| Italy          | Rome         |    2870000 |**

**| Japan          | Tokyo        |   37400000 |**

**| Kenya          | Nairobi      |    4400000 |**

**| South Korea    | Seoul        |    9500000 |**

**| Mexico         | Mexico City  |    9200000 |**

**| Netherlands    | Amsterdam    |     905000 |**

**| Peru           | Lima         |    9700000 |**

**| Poland         | Warsaw       |    1860000 |**

**| Portugal       | Lisbon       |     545000 |**

**| Saudi Arabia   | Riyadh       |    7680000 |**

**| Sweden         | Stockholm    |     980000 |**

**| Thailand       | Bangkok      |   10700000 |**

**| Venezuela      | Caracas      |    2900000 |**

**+----------------+--------------+------------+**

**28 rows in set (0.02 sec)**



**3.FIND CITIES THAT ARE LARGEST IN THEIR COUNTRY**



**mysql> SELECT C1.NAME,C1.POPULATION,C1.COUNTRYCODE**

&#x20;   **-> FROM CITY C1**

&#x20;   **-> WHERE C1.POPULATION=(SELECT MAX(C2.POPULATION)**

&#x20;   **->                           FROM CITY C2**

&#x20;   **->                            WHERE C2.COUNTRYCODE=C1.COUNTRYCODE);**

**+------------------+------------+-------------+**

**| NAME             | POPULATION | COUNTRYCODE |**

**+------------------+------------+-------------+**

**| Berlin           |    3677000 | DEU         |**

**| Paris            |    2140000 | FRA         |**

**| London           |    8980000 | GBR         |**

**| Rome             |    2870000 | ITA         |**

**| Madrid           |    3280000 | ESP         |**

**| Warsaw           |    1860000 | POL         |**

**| Amsterdam        |     905000 | NLD         |**

**| Brussels         |    1220000 | BEL         |**

**| Stockholm        |     980000 | SWE         |**

**| Lisbon           |     545000 | PRT         |**

**| Athens           |     660000 | GRC         |**

**| Monaco-Ville     |       1300 | MCO         |**

**| Lagos            |   15400000 | NGA         |**

**| Cairo            |   10100000 | EGY         |**

**| Johannesburg     |    5780000 | ZAF         |**

**| Nairobi          |    4400000 | KEN         |**

**| Addis Ababa      |    5230000 | ETH         |**

**| Kumasi           |    3350000 | GHA         |**

**| Casablanca       |    3750000 | MAR         |**

**| Algiers          |    2760000 | DZA         |**

**| Shanghai         |   24870000 | CHN         |**

**| New Delhi        |   34700000 | IND         |**

**| Tokyo            |   37400000 | JPN         |**

**| Jakarta          |   10900000 | IDN         |**

**| Karachi          |   16800000 | PAK         |**

**| Dhaka            |   22400000 | BGD         |**

**| Ho Chi Minh City |    9300000 | VNM         |**

**| Bangkok          |   10700000 | THA         |**

**| Seoul            |    9500000 | KOR         |**

**| Riyadh           |    7680000 | SAU         |**

**| New York         |    8800000 | USA         |**

**| Toronto          |    2930000 | CAN         |**

**| Mexico City      |    9200000 | MEX         |**

**| Sao Paulo        |   12300000 | BRA         |**

**| Buenos Aires     |    3080000 | ARG         |**

**| Bogota           |    7970000 | COL         |**

**| Lima             |    9700000 | PER         |**

**| Santiago         |    6270000 | CHL         |**

**| Caracas          |    2900000 | VEN         |**

**| Sydney           |    5310000 | AUS         |**

**| Auckland         |    1700000 | NZL         |**

**+------------------+------------+-------------+**

**41 rows in set (0.04 sec)**



**4.FIND COUNTRIES THAT HAVE CITIES WITH POPULATION OVER 5 MILLION.**



**mysql> SELECT C.NAME,C.CONTINENT**

&#x20;   **->     FROM COUNTRY C**

&#x20;   **->     WHERE EXISTS(SELECT 1**

&#x20;   **->     FROM CITY CI**

&#x20;   **->     WHERE CI.COUNTRYCODE=C.CODE**

&#x20;   **->     AND CI.POPULATION>5000000);**

**+----------------+---------------+**

**| NAME           | CONTINENT     |**

**+----------------+---------------+**

**| Australia      | Oceania       |**

**| Bangladesh     | Asia          |**

**| Brazil         | South America |**

**| Chile          | South America |**

**| China          | Asia          |**

**| Colombia       | South America |**

**| Egypt          | Africa        |**

**| Ethiopia       | Africa        |**

**| United Kingdom | Europe        |**

**| Indonesia      | Asia          |**

**| India          | Asia          |**

**| Japan          | Asia          |**

**| South Korea    | Asia          |**

**| Mexico         | North America |**

**| Nigeria        | Africa        |**

**| Pakistan       | Asia          |**

**| Peru           | South America |**

**| Saudi Arabia   | Asia          |**

**| Thailand       | Asia          |**

**| United States  | North America |**

**| Vietnam        | Asia          |**

**| South Africa   | Africa        |**

**+----------------+---------------+**

**22 rows in set (0.01 sec)**



**5.FIND COUNTRIES THAT HAVE ATLEAST ONE CITY.**



&#x20;**mysql> SELECT NAME,CONTINENT,POPULATION FROM COUNTRY C**

&#x20;   **->      WHERE EXISTS(SELECT 1**

&#x20;   **->      FROM CITY CI**

&#x20;   **->      WHERE CI.COUNTRYCODE=C.CODE);**

**+----------------+---------------+------------+**

**| NAME           | CONTINENT     | POPULATION |**

**+----------------+---------------+------------+**

**| Argentina      | South America |   45800000 |**

**| Australia      | Oceania       |   26600000 |**

**| Belgium        | Europe        |   11600000 |**

**| Bangladesh     | Asia          |  172000000 |**

**| Brazil         | South America |  216400000 |**

**| Canada         | North America |   38900000 |**

**| Chile          | South America |   19600000 |**

**| China          | Asia          | 1412000000 |**

**| Colombia       | South America |   52200000 |**

**| Germany        | Europe        |   83200000 |**

**| Algeria        | Africa        |   45400000 |**

**| Egypt          | Africa        |  112700000 |**

**| Spain          | Europe        |   47400000 |**

**| Ethiopia       | Africa        |  126500000 |**

**| France         | Europe        |   68000000 |**

**| United Kingdom | Europe        |   67300000 |**

**| Ghana          | Africa        |   33500000 |**

**| Greece         | Europe        |   10400000 |**

**| Indonesia      | Asia          |  277500000 |**

**| India          | Asia          | 1428000000 |**

**| Italy          | Europe        |   59000000 |**

**| Japan          | Asia          |  123300000 |**

**| Kenya          | Africa        |   55100000 |**

**| South Korea    | Asia          |   51700000 |**

**| Morocco        | Africa        |   37800000 |**

**| Monaco         | Europe        |      39000 |**

**| Mexico         | North America |  128900000 |**

**| Nigeria        | Africa        |  223800000 |**

**| Netherlands    | Europe        |   17700000 |**

**| New Zealand    | Oceania       |    5200000 |**

**| Pakistan       | Asia          |  240500000 |**

**| Peru           | South America |   34400000 |**

**| Poland         | Europe        |   37700000 |**

**| Portugal       | Europe        |   10300000 |**

**| Saudi Arabia   | Asia          |   36900000 |**

**| Sweden         | Europe        |   10500000 |**

**| Thailand       | Asia          |   71800000 |**

**| United States  | North America |  339900000 |**

**| Venezuela      | South America |   28300000 |**

**| Vietnam        | Asia          |   98900000 |**

**| South Africa   | Africa        |   60400000 |**

**+----------------+---------------+------------+**

**41 rows in set (0.01 sec)**

**=========================================================**

&#x20;**INTERVIEW QUESTIONS**



**TO GET MIN AND MAX**

**--------------------**

**MIN:**

**SELECT MIN(SALARY)AS MINIMUM\_SALARY FROM EMPLOYEES;**

**MAX:**

**SELECT MAX(SALARY)AS MAXIMUM\_SALARY FROM EMPLOYEES;**



**---------------**

**TO GET 2ND MIN AND 2ND MAX:**

**2ND MIN:**

**SELECT MIN(SALARY) AS SECOND\_MIN**

**FROM EMPLOYEES WHERE SALARY>(SELECT MIN(SALARY) FROM EMPLOYEES);**

**2ND MAX:**

**SELECT MAX(SALARY) AS SECOND\_MAX**

**FROM EMPLOYEES WHERE SALARY<(SELECT MAX(SALARY) FROM EMPLOYEES);**



**---------------------**

**TO GET 3RD MIN AND 3RD MAX:**



**3RD MIN:**

**SELECT MIN(SALARY) AS THIRD\_MIN**

**FROM EMPLOYEE**

**WHERE SALARY > (**

&#x20;   **SELECT MIN(SALARY) FROM EMPLOYEE** 

&#x20;   **WHERE SALARY > (SELECT MIN(SALARY) FROM EMPLOYEE)**

**);**



**3RD MAX:**

**SELECT MAX(SALARY) AS THIRD\_MAX**

**FROM EMPLOYEE**

**WHERE SALARY < (**

&#x20;   **SELECT MAX(SALARY) FROM EMPLOYEE**

&#x20;   **WHERE SALARY < (SELECT MAX(SALARY) FROM EMPLOYEE)**

**);**

==========================================

**TO GET** 

**1.2ND MIN SALARY DEPARTMENTWISE:**



**SELECT D.DEPT\_ID,D.DEPT\_NAME,MIN(E.SALARY)AS SECOND\_MIN\_SALARY**

**FROM EMPLOYEE E**

**JOIN DEPARTMENT D**

**ON E.DEPT\_ID=D.DEPT\_ID**

**WHERE E.SALARY>(**

**SELECT MIN(SALARY)**

**FROM EMPLOYEE E2**

**WHERE E2.DEPT\_ID=E.DEPT\_ID)**

**GROUP BY D.DEPT\_ID;**

**------------------------------**

**2.2ND MAX SALARY DEPARTMENTWISE:**



**SELECT D.DEPT\_ID,D.DEPT\_NAME,MAX(E.SALARY)AS SECOND\_MAX\_SALARY**

**FROM EMPLOYEE E**

**JOIN DEPARTMENT D**

**ON E.DEPT\_ID=D.DEPT\_ID**

**WHERE E.SALARY<(**

**SELECT MAX(SALARY)**

**FROM EMPLOYEE E2**

**WHERE E2.DEPT\_ID=E.DEPT\_ID)**

**GROUP BY D.DEPT\_ID;**

\------------------------

**3.3RD** **MIN SALARY DEPARTMENTWISE:**



**SELECT D.DEPT\_ID,D.DEPT\_NAME,MIN(E.SALARY)AS THIRD\_MIN\_SALARY**

**FROM EMPLOYEE E**

**JOIN DEPARTMENT D**

**ON E.DEPT\_ID=D.DEPT\_ID**

**WHERE E.SALARY>(**

&#x20;   **SELECT MIN(SALARY)**

&#x20;   **FROM EMPLOYEE E2**

&#x20;   **WHERE E2.DEPT\_ID=E.DEPT\_ID**

&#x20;     **AND E2.SALARY>(**

&#x20;         **SELECT MIN(SALARY)**

&#x20;         **FROM EMPLOYEE E3**

&#x20;         **WHERE E3.DEPT\_ID = E2.DEPT\_ID**

&#x20;     **)**

**)**

**GROUP BY D.DEPT\_ID;**

**------------------------**



**4.3RD MAX SALARY DEPARTMENTWISE:**



**SELECT D.DEPT\_ID,D.DEPT\_NAME,MAX(E.SALARY)AS THIRD\_MAX\_SALARY**

**FROM EMPLOYEE E**

**JOIN DEPARTMENT D**

**ON E.DEPT\_ID=D.DEPT\_ID**

**WHERE E.SALARY<(**

&#x20;   **SELECT MAX(SALARY)**

&#x20;   **FROM EMPLOYEE E2**

&#x20;   **WHERE E2.DEPT\_ID=E.DEPT\_ID**

&#x20;     **AND E2.SALARY<(**

&#x20;         **SELECT MAX(SALARY)**

&#x20;         **FROM EMPLOYEE E3**

&#x20;         **WHERE E3.DEPT\_ID = E2.DEPT\_ID**

&#x20;     **)**

**)**

**GROUP BY D.DEPT\_ID;**



**============================**

**STORED PROCEDURES**



**A STORED PROCEDURE IS A NAMED,PRECOMPILED COLLECTION OF ONE OR MORE SQL STATEMENTS THAT ARE STORED INSIDE THE DATABASE AND CAN BE EXECUTED(CALLED) WHENEVER REQUIRED.INSTEAD OF SENDING A LONG BLOCK OF SQL FROM AN APPLICATION EVERYTIME,THE APPLICATION SIMPLY CALLS THE PROCEDURE BY NAME.**



**STORED PROCEDURES BEHAVE LIKE FUNCTIONS OR SUBROUTINES IN PROGRAMMING LANGUAGE.THEY CAN ACCEPT PARAMENTERS,PERFORMS LOGIC(LOOPS,CONDITIONS,VARIABLE DECLARATIONS) AND RETURN RESULTS.**



**WHY USE STORED PROCEDURES**

**-------------------------**

**1.PERFORMANCE:- PRECOMPILED AND CATCHED BY THE DATABASE ENGINE,SO REPEATED EXECUTION IS FASTER TAHN SENDING RAW SQL EACH TIME.**

**2.REUSABILITY:- WRITE THE LOGIC ONCE CALL IT FROM MANY APPLICATIONS OR SCRIPTS.**

**3.SECURITY:- USERS CAN BE GRANTED EXECUTE PERMISSION ON A PROCEDURE WITHOUT GRANTING DIRECT ACCESS TO THE UNDERLYING TABLES.**

**4.REDUCE NETWORK TRAFFIC:- A SINGLE CALL STATEMENT REPLACES MANY LINES OF SQL SENT OVER THE NETWORK.**

**5.MAINTAINBILITY:- BUSINESS LOGIC IS CENTRALIZED IN THE DATABASE, SO MANY CHANGES ARE MADE IN ONE PLACE.**

**6.CONSISTENCY:- ENSURES THE SAME VALIDATION/BUSINESS RULES ARE APPLIED EVERY TIME, REGARDLESS OF WHICH APPLILCATION CALLS IT.**



**ADAVNTAGES**

**----------**

* **FASTER EXECUTION AFTER COMPILATION**
* **REDUCE DUPILICATE SQL.**
* **SUPPORTS TRANSACTIONS,LOOPS,CONDITIONS, VARIABLES, CURSORS AND EXCEPTION HANDLERS.**
* **EASY MAINTENANCE.**



**DISADVANTAGES**

**-------------**

* **DEBUGGING CAN BE DIFFICULT.**
* **VENDOR-SPECIFIC SYNTAX.**
* **COMPLEX PROCEDURES MAY BECOME HARD YO MAINTAIN.**



**HOW TO CREATE PROCEDURE**

**SYNTAX**

**----------**

**DELIMITER//**



**CREATE PROCEDURE procedure\_name(**

**\[IN | OUT | INOUT]parameter-name data-type,.........**

**)  # parameterts are optional**

**BEGIN**

**-------SQL statements/logic**

**-----------declarations,conditions,loos..etc**

**END//**



**DELIMITER;**



**call procedure\_name;**





**EXAMPLE:**



**mysql> CREATE TABLE Employees (**

&#x20;   **->     emp\_id INT PRIMARY KEY,**

&#x20;   **->     emp\_name VARCHAR(50),**

&#x20;   **->     department VARCHAR(30),**

&#x20;   **->     salary DECIMAL(10,2),**

&#x20;   **->     experience INT,**

&#x20;   **->     city VARCHAR(30)**

&#x20;   **-> );**

**Query OK, 0 rows affected (0.06 sec)**



**mysql> INSERT INTO Employees VALUES**

&#x20;   **-> (101,'Rahul','IT',65000,5,'Hyderabad'),**

&#x20;   **-> (102,'Priya','HR',45000,3,'Chennai'),**

&#x20;   **-> (103,'Amit','Finance',70000,6,'Bangalore'),**

&#x20;   **-> (104,'Sneha','IT',80000,8,'Hyderabad'),**

&#x20;   **-> (105,'Kiran','Sales',40000,2,'Pune'),**

&#x20;   **-> (106,'Ravi','HR',50000,4,'Mumbai'),**

&#x20;   **-> (107,'Anjali','IT',90000,10,'Delhi'),**

&#x20;   **-> (108,'Suresh','Finance',55000,5,'Chennai'),**

&#x20;   **-> (109,'Divya','Sales',48000,3,'Hyderabad'),**

&#x20;   **-> (110,'Vikram','IT',75000,7,'Bangalore');**

**Query OK, 10 rows affected (0.02 sec)**

**Records: 10  Duplicates: 0  Warnings: 0**



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

**10 rows in set (0.01 sec)**



**WITHOUT PARAMETERS**

**mysql> DELIMITER //**

**mysql>**

**mysql> CREATE PROCEDURE GETALLEMPLOYEES()**

&#x20;   **-> BEGIN**

&#x20;   **->     SELECT\*FROM EMPLOYEES;**

&#x20;   **-> END //**

**Query OK, 0 rows affected (0.02 sec)**



**mysql>**

**mysql> DELIMITER ;**

**mysql>  CALL GETALLEMPLOYESS();**

**ERROR 1305 (42000): PROCEDURE pfs4.GETALLEMPLOYESS does not exist**

**mysql>  CALL GETALLEMPLOYEES();**

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

**10 rows in set (0.01 sec)**



**Query OK, 0 rows affected (0.03 sec)**



**mysql> SHOW PROCEDURE STATUS   # to see the procedures.**

&#x20;   **-> WHERE Db = 'pfs4';**

**+------+-----------------+-----------+----------------+---------------------+---------------------+---------------+---------+----------------------+----------------------+--------------------+**

**| Db   | Name            | Type      | Definer        | Modified            | Created             | Security\_type | Comment | character\_set\_client | collation\_connection | Database Collation |**

**+------+-----------------+-----------+----------------+---------------------+---------------------+---------------+---------+----------------------+----------------------+--------------------+**

**| pfs4 | GETALLEMPLOYEES | PROCEDURE | root@localhost | 2026-08-04 11:00:31 | 2026-08-04 11:00:31 | DEFINER       |         | cp850                | cp850\_general\_ci     | utf8mb4\_0900\_ai\_ci |**

**+------+-----------------+-----------+----------------+---------------------+---------------------+---------------+---------+----------------------+----------------------+--------------------+**

**1 row in set (0.02 sec)**







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



**Query OK, 0 rows affected (0.01 sec)**



**mysql> SHOW PROCEDURE STATUS**

&#x20;   **-> WHERE Db='pfs4';**

**+------+-----------------+-----------+----------------+---------------------+---------------------+---------------+---------+----------------------+----------------------+--------------------+**

**| Db   | Name            | Type      | Definer        | Modified            | Created             | Security\_type | Comment | character\_set\_client | collation\_connection | Database Collation |**

**+------+-----------------+-----------+----------------+---------------------+---------------------+---------------+---------+----------------------+----------------------+--------------------+**

**| pfs4 | GETALLEMPLOYEES | PROCEDURE | root@localhost | 2026-08-04 11:00:31 | 2026-08-04 11:00:31 | DEFINER       |         | cp850                | cp850\_general\_ci     | utf8mb4\_0900\_ai\_ci |**

**| pfs4 | GETITEMPLOYEES  | PROCEDURE | root@localhost | 2026-08-04 11:04:52 | 2026-08-04 11:04:52 | DEFINER       |         | cp850                | cp850\_general\_ci     | utf8mb4\_0900\_ai\_ci |**

**+------+-----------------+-----------+----------------+---------------------+---------------------+---------------+---------+----------------------+----------------------+--------------------+**

**2 rows in set (0.00 sec)**



**mysql> DELIMITER //**

**mysql> CREATE PROCEDURE ALLEMPLOYEES()**

&#x20;   **-> BEGIN**

&#x20;   **->     SELECT EMP\_NAME**

&#x20;   **-> FROM EMPLOYEES;**

&#x20;   **-> END //**

**Query OK, 0 rows affected (0.03 sec)**



**mysql> DELIMITER ;**

**mysql> SHOW PROCEDURE STATUS**

&#x20;   **-> WHERE DB='PFS4';**

**+------+-----------------+-----------+----------------+---------------------+---------------------+---------------+---------+----------------------+----------------------+--------------------+**

**| Db   | Name            | Type      | Definer        | Modified            | Created             | Security\_type | Comment | character\_set\_client | collation\_connection | Database Collation |**

**+------+-----------------+-----------+----------------+---------------------+---------------------+---------------+---------+----------------------+----------------------+--------------------+**

**| pfs4 | ALLEMPLOYEES    | PROCEDURE | root@localhost | 2026-08-04 11:09:16 | 2026-08-04 11:09:16 | DEFINER       |         | utf8mb4              | utf8mb4\_0900\_ai\_ci   | utf8mb4\_0900\_ai\_ci |**

**| pfs4 | EMPLOYEES       | PROCEDURE | root@localhost | 2026-08-04 11:05:42 | 2026-08-04 11:05:42 | DEFINER       |         | utf8mb4              | utf8mb4\_0900\_ai\_ci   | utf8mb4\_0900\_ai\_ci |**

**| pfs4 | GETALLEMPLOYEES | PROCEDURE | root@localhost | 2026-08-04 10:55:20 | 2026-08-04 10:55:20 | DEFINER       |         | utf8mb4              | utf8mb4\_0900\_ai\_ci   | utf8mb4\_0900\_ai\_ci |**

**| pfs4 | GETITEMPLOYEES  | PROCEDURE | root@localhost | 2026-08-04 11:03:00 | 2026-08-04 11:03:00 | DEFINER       |         | utf8mb4              | utf8mb4\_0900\_ai\_ci   | utf8mb4\_0900\_ai\_ci |**

**+------+-----------------+-----------+----------------+---------------------+---------------------+---------------+---------+----------------------+----------------------+--------------------+**

**4 rows in set (0.00 sec)**



