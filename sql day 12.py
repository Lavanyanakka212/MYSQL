clauses operations

--total units sold per category where total units >20
select category,sum(units_sold)as total_units
from sales
group by category
having total_units>20;

--total revenue per region where revenue >50000
select region,sum(units_sold*unit_price)as revenue
from sales 
group by region
having revenue>50000;

--count of products per category with nore than 2 products
------------------------------------------------------------
select category, count(product) as product_count
from sales
group by category
having product_count>2;

--average unit price per category <5000
-------------------------------------------
select category,
AVG(unit_price) AS avg_price
from sales
group by category
having AVG(unit_price)<5000;

---------------------------------------------------
 --categories and total units sold,orderd desending--
 select category,sum(units_sold) as total_units
    -> from sales
    -> group by category
    -> order by total_units desc;
+---------------+-------------+
| category      | total_units |
+---------------+-------------+
| Electronics   |          72 |
| Furniture     |          44 |
| HomeAppliance |          22 |
+---------------+-------------+

 --average unit price per region,ordered alphabetically
 select region,avg(unit_price) as avg_price
    -> from sales
    -> group by region
    -> order by region asc;
+--------+------------+
| region | avg_price  |
+--------+------------+
| East   |  5266.6667 |
| North  | 12100.0000 |
| South  | 12500.0000 |
| West   | 23833.3333 |
+--------+------------+

 --total revenue per category,highest first
 select category,
    -> sum(units_sold*unit_price)as revenue
    -> from sales
    -> group by category
    -> order by revenue desc;
+---------------+---------+
| category      | revenue |
+---------------+---------+
| Electronics   |  768400 |
| Furniture     |  296000 |
| HomeAppliance |  194000 |
+---------------+---------+
 --count of products in each region,desending
 select region,count(product) as product_count
    -> from sales
    -> group by region
    -> order by product_count desc;
+--------+---------------+
| region | product_count |
+--------+---------------+
| North  |             5 |
| South  |             4 |
| West   |             3 |
| East   |             3 |
+--------+---------------+
 --regions and total units sold sorted by region
 select region, count(units_sold) as total_units
    -> from sales
    -> group by region
    -> order by total_units asc;
+--------+-------------+
| region | total_units |
+--------+-------------+
| West   |           3 |
| East   |           3 |
| South  |           4 |
| North  |           5 |
+--------+-------------+

---------------------------------------------------

--Total revenue per region>20000, order by revenue descending--
select region, sum(units_sold*unit_price) as total_revenue
    -> from sales
    -> group by region
    -> having total_revenue>20000
    -> order by total_revenue desc;
+--------+---------------+
| region | total_revenue |
+--------+---------------+
| North  |        483900 |
| West   |        421500 |
| South  |        184000 |
| East   |        169000 |
+--------+---------------+
--Total units sold per category>10,order by category--
mysql> select category, sum(units_sold) as total_units
    -> from sales
    -> group by category
    -> having total_units>10
    -> order by category;
+---------------+-------------+
| category      | total_units |
+---------------+-------------+
| Electronics   |          72 |
| Furniture     |          44 |
| HomeAppliance |          22 |
+---------------+-------------+

count of products per region>1,order alphabetically
select region,count(product) as product_count
    -> from sales
    -> group by region
    -> having product_count>1
    -> order by region;
+--------+---------------+
| region | product_count |
+--------+---------------+
| East   |             3 |
| North  |             5 |
| South  |             4 |
| West   |             3 |
+--------+---------------+

--categories where avg price<6000,order by avg price
 select category,avg(unit_price) as avg_price
    -> from sales
    -> group by category
    -> having avg_price<6000
    -> order by avg_price;
Empty set (0.00 sec)

--avg units sold per category>5,order by average descending
 select category,avg(units_sold) as avg_units
    -> from sales
    -> group by category
    -> having avg_units>5
    -> order by avg_units desc;
+---------------+-----------+
| category      | avg_units |
+---------------+-----------+
| HomeAppliance |   11.0000 |
| Electronics   |   10.2857 |
| Furniture     |    7.3333 |
+---------------+-----------+
---------------------------------------------------------------------

question 1

select region, sum(units_sold) as total_units
    -> from sales
    -> where category='Electronics'
    -> group by region
    -> having total_units>15
    -> order by total_units desc;
+--------+-------------+
| region | total_units |
+--------+-------------+
| North  |          32 |
| East   |          29 |
+--------+-------------+

question 2
display the total revenue generated by each category considering only products whose unit price is greater than 2000. show only categories with revenue greater than 100000 and oder by revenue in desending order

 select category,sum(units_sold*unit_price) as revenue
    -> from sales
    -> where unit_price >2000
    -> group by category
    -> having revenue>100000
    -> order by revenue desc;
+---------------+---------+
| category      | revenue |
+---------------+---------+
| Electronics   |  726000 |
| Furniture     |  296000 |
| HomeAppliance |  194000 |
+---------------+---------+

question 3

display the average unit price of each region considering only products where units sold are greater than or equal to 5.show only regions where the average price is greater than 5000 and order the results alphabetically

select region,avg(unit_price) as revenue
    -> from sales
    -> where units_sold>=5
    -> group by region
    -> having revenue>5000
    -> order by region;
+--------+------------+
| region | revenue    |
+--------+------------+
| East   |  5266.6667 |
| North  |  6375.0000 |
| West   | 23833.3333 |
+--------+------------+

Q 4
Q 5

===================================================================================

SET OPERATORS:--

Union:- combines results from two queries and remove duplicates rows. columns must have the 
same number and type.

Union all :- combines results from two queries. including duplicates columns must have the same number and type.

imtersect:- returns rows that are common to both queries.columns must have the same number and type.

note:- MySQL doest'nt support intersect directly

Minus:- returns rows from the first query that are not present in the second query columns must have the same number and type.

note:- MySQL doesn't support Minus directly.
                


mysql> CREATE TABLE Students (
    ->     student_id INT PRIMARY KEY,
    ->     student_name VARCHAR(50),
    ->     course VARCHAR(50)
    -> );
Query OK, 0 rows affected (0.03 sec)

mysql>
mysql> INSERT INTO Students VALUES
    -> (101,'Rahul','Java Full Stack'),
    -> (102,'Priya','Python Full Stack'),
    -> (103,'Kiran','Data Science'),
    -> (104,'Sneha','Java Full Stack'),
    -> (105,'Ajay','Testing');
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> CREATE TABLE Placed_Students (
    ->     student_id INT PRIMARY KEY,
    ->     student_name VARCHAR(50),
    ->     company_name VARCHAR(50)
    -> );
Query OK, 0 rows affected (0.03 sec)

mysql> INSERT INTO Placed_Students VALUES
    -> (103,'Kiran','TCS'),
    -> (104,'Sneha','Infosys'),
    -> (105,'Ajay','Wipro'),
    -> (106,'Pooja','Accenture'),
    -> (107,'Ramesh','Capgemini');


mysql> SELECT*FROM STUDENTS;
+------------+--------------+-------------------+
| student_id | student_name | course            |
+------------+--------------+-------------------+
|        101 | Rahul        | Java Full Stack   |
|        102 | Priya        | Python Full Stack |
|        103 | Kiran        | Data Science      |
|        104 | Sneha        | Java Full Stack   |
|        105 | Ajay         | Testing           |
+------------+--------------+-------------------+
5 rows in set (0.00 sec)

mysql> SELECT*FROM PLACED_STUDENTS;
+------------+--------------+--------------+
| student_id | student_name | company_name |
+------------+--------------+--------------+
|        103 | Kiran        | TCS          |
|        104 | Sneha        | Infosys      |
|        105 | Ajay         | Wipro        |
|        106 | Pooja        | Accenture    |
|        107 | Ramesh       | Capgemini    |
+------------+--------------+--------------+
5 rows in set (0.00 sec)

mysql> SELECT STUDENT_ID
    -> FROM STUDENTS
    -> UNION
    -> SELECT STUDENT_ID
    -> FROM PLACED_STUDENTS;
+------------+
| STUDENT_ID |
+------------+
|        101 |
|        102 |
|        103 |
|        104 |
|        105 |
|        106 |
|        107 |
+------------+
7 rows in set (0.01 sec)

mysql> SELECT STUDENT_ID
    -> FROM STUDENTS
    -> UNION ALL
    -> SELECT STUDENT_ID
    -> FROM PLACED_STUDENTS;
+------------+
| STUDENT_ID |
+------------+
|        101 |
|        102 |
|        103 |
|        104 |
|        105 |
|        103 |
|        104 |
|        105 |
|        106 |
|        107 |
+------------+
10 rows in set (0.00 sec)

mysql> --DISPLAY ALL STUDENT IDS AND NAMES FROM BOTH TABLES WITHOUT DUPLICATES^C
mysql> SELECT STUDENT_ID,STUDENT_NAME
    -> FROM STUDENTS
    -> UNION
    -> SELECT STUDENT_ID,STUDENT_NAME
    -> FROM PLACED_STUDENTS;
+------------+--------------+
| STUDENT_ID | STUDENT_NAME |
+------------+--------------+
|        101 | Rahul        |
|        102 | Priya        |
|        103 | Kiran        |
|        104 | Sneha        |
|        105 | Ajay         |
|        106 | Pooja        |
|        107 | Ramesh       |
+------------+--------------+
7 rows in set (0.00 sec)

mysql> SELECT STUDENT_ID,STUDENT_NAME
    -> FROM STUDENTS
    -> UNION ALL
    -> SELECT STUDENT_ID,STUDENT_NAME
    -> FROM PLACED_STUDENTS;
+------------+--------------+
| STUDENT_ID | STUDENT_NAME |
+------------+--------------+
|        101 | Rahul        |
|        102 | Priya        |
|        103 | Kiran        |
|        104 | Sneha        |
|        105 | Ajay         |
|        103 | Kiran        |
|        104 | Sneha        |
|        105 | Ajay         |
|        106 | Pooja        |
|        107 | Ramesh       |
+------------+--------------+
10 rows in set (0.00 sec)

mysql>






