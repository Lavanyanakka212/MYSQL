DATE AND TIME FUNCTIONS:-
--------------------------
CURDATE():- RETURNS THE CURRENT DATE
CURTIME():- RETURNS THE CURRENT TIME
NOW():- RETURNS THE CURRENT DATE AND TIME TOGETHER
DATE():-EXTRACT THE DATE PART
TIME():- EXTRACT THE TIME PART
YEAR():-EXTRACT ON YEAR FROM DATE
MONTH():- EXTRACT MONTHE FROM DATE
DAY()/DAYOFMONTH:- EXTRACT DAY OF MONTH
WEEK():- EXTRACT WEEK NUMBER
DAYOFWEEK():- EXTRACT DAY OF THE WEEK
date_add():- add a date
date_sub:- subtract date
sysdate():-systems date and time
sec_to_time():- converts sec to time 
time_to_sec():-converts time to secs
quarter():- gives the number in which quarter the present month is in.
monthname():- give the month name 
dayname():- give the day name
last_day():- give the last day of the month
date_format():- give datein an formatted form eg:- Wednesday,July,29th,2026
datediff():- gives difference between two specified dates.
date_sub():- give the date subtracted from a specified number of days eg:-select datediff(now(),'2000-05-23') as days_diff; output:- 9563 now()=29 July,2026
date_add():- adds the dates to a specified dates and givce sthe output eg:-
dayofweek():- give the day number in the week


use newda4;
Database changed
mysql> select curdate() as current__date;
+---------------+
| current__date |
+---------------+
| 2026-07-29    |
+---------------+
1 row in set (0.00 sec)

mysql> select curtime() as current__time;
+---------------+
| current__time |
+---------------+
| 11:12:40      |
+---------------+
1 row in set (0.00 sec)

mysql> select now() as current_date_time;
+---------------------+
| current_date_time   |
+---------------------+
| 2026-07-29 11:13:06 |
+---------------------+
1 row in set (0.00 sec)

mysql> select date(now()) as extracted_date;
+----------------+
| extracted_date |
+----------------+
| 2026-07-29     |
+----------------+
1 row in set (0.01 sec)

mysql> select time(now()) as extracted_date;
+----------------+
| extracted_date |
+----------------+
| 11:15:00       |
+----------------+
1 row in set (0.00 sec)

mysql> select time(now()) as extracted_time;
+----------------+
| extracted_time |
+----------------+
| 11:15:08       |
+----------------+
1 row in set (0.00 sec)

mysql> select time('2024-04-03','14:32:10') as extracted_time;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ','14:32:10') as extracted_time' at line 1
mysql> select time('2024-04-03 14:32:10') as extracted_time;
+----------------+
| extracted_time |
+----------------+
| 14:32:10       |
+----------------+
1 row in set (0.00 sec)

mysql> select year(now()) as year_part;
+-----------+
| year_part |
+-----------+
|      2026 |
+-----------+
1 row in set (0.00 sec)

mysql> select month(now()) as month_part;
+------------+
| month_part |
+------------+
|          7 |
+------------+
1 row in set (0.01 sec)

mysql> select day(now()) as day_part;
+----------+
| day_part |
+----------+
|       29 |
+----------+
1 row in set (0.00 sec)

mysql> select week(now()) as week;
+------+
| week |
+------+
|   30 |
+------+
1 row in set (0.00 sec)

mysql> select dayofweek(now()) as day_of_week;
+-------------+
| day_of_week |
+-------------+
|           4 |
+-------------+
1 row in set (0.01 sec)

mysql> select date_add(now(),interval 20day) as new_date;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ') as new_date' at line 1
mysql> select date_add(now(),interval 20day) as new_date;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ') as new_date' at line 1
mysql> select date_add(now(),interval 20 day) as new_date;
+---------------------+
| new_date            |
+---------------------+
| 2026-08-18 11:22:56 |
+---------------------+
1 row in set (0.00 sec)

mysql> select date_add(now(),interval 100 day) as new_date;
+---------------------+
| new_date            |
+---------------------+
| 2026-11-06 11:23:04 |
+---------------------+
1 row in set (0.00 sec)

mysql> select date_sub(now(),interval 100 day) as new_date;
+---------------------+
| new_date            |
+---------------------+
| 2026-04-20 11:23:18 |
+---------------------+
1 row in set (0.00 sec)

mysql> select datediff(now(),'2000-05-23') as days_diff;
+-----------+
| days_diff |
+-----------+
|      9563 |
+-----------+
1 row in set (0.00 sec)

mysql> select date_format(now(),'%W,%M,%D,%Y') as formated__date;
+--------------------------+
| formated__date           |
+--------------------------+
| Wednesday,July,29th,2026 |
+--------------------------+
1 row in set (0.00 sec)

mysql> select last_day(now()) as last_day_of_month;
+-------------------+
| last_day_of_month |
+-------------------+
| 2026-07-31        |
+-------------------+
1 row in set (0.00 sec)

mysql> select month_name(now()) as month_name;
ERROR 1305 (42000): FUNCTION newda4.month_name does not exist
mysql> select month_name(now()) as month__name;
ERROR 1305 (42000): FUNCTION newda4.month_name does not exist
mysql> select monthname(now()) as month__name;
+-------------+
| month__name |
+-------------+
| July        |
+-------------+
1 row in set (0.00 sec)

mysql> select dayname(now()) as day__name;
+-----------+
| day__name |
+-----------+
| Wednesday |
+-----------+
1 row in set (0.00 sec)

mysql> select quarter(now()) as month_quarter;
+---------------+
| month_quarter |
+---------------+
|             3 |
+---------------+
1 row in set (0.00 sec)

mysql> --seconds to time^C
mysql> select time_to_seconds('01:01:01') as total_seconds;
ERROR 1305 (42000): FUNCTION newda4.time_to_seconds does not exist
mysql> select time_to_sec('01:01:01') as total_seconds;
+---------------+
| total_seconds |
+---------------+
|          3661 |
+---------------+
1 row in set (0.00 sec)

mysql> select sec_to_time('3663') as time;
+-----------------+
| time            |
+-----------------+
| 01:01:03.000000 |
+-----------------+
1 row in set (0.00 sec)

mysql> select sysdate() as sytem_date_time;
+---------------------+
| sytem_date_time     |
+---------------------+
| 2026-07-29 11:34:43 |
+---------------------+

 CREATE TABLE employee_attendance
    -> (
    ->  emp_id INT PRIMARY KEY AUTO_INCREMENT,
    ->  emp_name VARCHAR(100),
    ->  department VARCHAR(50),
    ->  joining_date DATE,
    ->  birth_date DATE,
    ->  login_time DATETIME,
    ->  logout_time DATETIME,
    ->  salary DECIMAL(10,2)
    -> );
Query OK, 0 rows affected (0.07 sec)

mysql>
mysql> INSERT INTO employee_attendance
    -> (emp_name, department, joining_date, birth_date, login_time, logout_time, salary)
    -> VALUES
    -> ('Rahul','IT','2021-06-15','1998-05-10','2024-11-20 09:05:10','2024-11-20 18:15:30',55000),
    -> ('Sneha','HR','2020-03-21','1996-11-18','2024-11-21 08:55:20','2024-11-21 17:45:50',48000),
    -> ('Arjun','Finance','2019-08-10','1994-07-30','2024-11-22 09:15:45','2024-11-22 18:35:20',62000),
    -> ('Priya','IT','2022-01-05','2000-01-25','2024-11-23 09:00:00','2024-11-23 17:55:40',51000),
    -> ('Kiran','Admin','2018-12-11','1992-09-15','2024-11-24 08:40:30','2024-11-24 17:30:00',45000),
    -> ('Anjali','Testing','2023-04-17','1999-12-20','2024-11-25 09:12:10','2024-11-25 18:05:00',47000),
    -> ('Vijay','IT','2021-09-14','1997-04-08','2024-11-26 09:08:15','2024-11-26 18:20:40',59000),
    -> ('Divya','HR','2019-10-19','1995-06-11','2024-11-27 08:50:30','2024-11-27 17:42:15',50000),
    -> ('Ramesh','Finance','2017-07-01','1991-08-14','2024-11-28 09:03:00','2024-11-28 18:12:00',70000),
    -> ('Pooja','Testing','2022-05-09','2001-03-19','2024-11-29 09:18:50','2024-11-29 18:25:10',53000);
Query OK, 10 rows affected (0.01 sec)
Records: 10  Duplicates: 0  Warnings: 0

select*from employee_attendance;
+--------+----------+------------+--------------+------------+---------------------+---------------------+----------+
| emp_id | emp_name | department | joining_date | birth_date | login_time          | logout_time         | salary   |
+--------+----------+------------+--------------+------------+---------------------+---------------------+----------+
|      1 | Rahul    | IT         | 2021-06-15   | 1998-05-10 | 2024-11-20 09:05:10 | 2024-11-20 18:15:30 | 55000.00 |
|      2 | Sneha    | HR         | 2020-03-21   | 1996-11-18 | 2024-11-21 08:55:20 | 2024-11-21 17:45:50 | 48000.00 |
|      3 | Arjun    | Finance    | 2019-08-10   | 1994-07-30 | 2024-11-22 09:15:45 | 2024-11-22 18:35:20 | 62000.00 |
|      4 | Priya    | IT         | 2022-01-05   | 2000-01-25 | 2024-11-23 09:00:00 | 2024-11-23 17:55:40 | 51000.00 |
|      5 | Kiran    | Admin      | 2018-12-11   | 1992-09-15 | 2024-11-24 08:40:30 | 2024-11-24 17:30:00 | 45000.00 |
|      6 | Anjali   | Testing    | 2023-04-17   | 1999-12-20 | 2024-11-25 09:12:10 | 2024-11-25 18:05:00 | 47000.00 |
|      7 | Vijay    | IT         | 2021-09-14   | 1997-04-08 | 2024-11-26 09:08:15 | 2024-11-26 18:20:40 | 59000.00 |
|      8 | Divya    | HR         | 2019-10-19   | 1995-06-11 | 2024-11-27 08:50:30 | 2024-11-27 17:42:15 | 50000.00 |
|      9 | Ramesh   | Finance    | 2017-07-01   | 1991-08-14 | 2024-11-28 09:03:00 | 2024-11-28 18:12:00 | 70000.00 |
|     10 | Pooja    | Testing    | 2022-05-09   | 2001-03-19 | 2024-11-29 09:18:50 | 2024-11-29 18:25:10 | 53000.00 |
+--------+----------+------------+--------------+------------+---------------------+---------------------+----------+

 select date(login_time) as date_part from employee_attendance;
+------------+
| date_part  |
+------------+
| 2024-11-20 |
| 2024-11-21 |
| 2024-11-22 |
| 2024-11-23 |
| 2024-11-24 |
| 2024-11-25 |
| 2024-11-26 |
| 2024-11-27 |
| 2024-11-28 |
| 2024-11-29 |
+------------+
 --display only time part from every employees login time^C
mysql> select time(login_time) as time_part from employee_attendance;
+-----------+
| time_part |
+-----------+
| 09:05:10  |
| 08:55:20  |
| 09:15:45  |
| 09:00:00  |
| 08:40:30  |
| 09:12:10  |
| 09:08:15  |
| 08:50:30  |
| 09:03:00  |
| 09:18:50  |
+-----------+

--display employee names along with their birth monthe number
 select emp_name,joining_date
    -> from employee_attendance
    -> where year(joining_date)=year(curdate());
Empty set 

--display joining dates of employees who joined in 2022
select emp_name,joining_date
    -> from employee_attendance
    -> where year(joining_date)=2022;
+----------+--------------+
| emp_name | joining_date |
+----------+--------------+
| Priya    | 2022-01-05   |
| Pooja    | 2022-05-09   |
+----------+--------------+

--display emp birth month is 11
select emp_name,birth_date
    -> from employee_attendance
    -> where month(birth_date)=11;
+----------+------------+
| emp_name | birth_date |
+----------+------------+
| Sneha    | 1996-11-18 |
+----------+------------+

--display emp who join in june
select emp_name,joining_date
    -> from employee_attendance
    -> where monthname(joining_date)='june';
+----------+--------------+
| emp_name | joining_date |
+----------+--------------+
| Rahul    | 2021-06-15   |
+----------+--------------+

--display emp whose bron on 10th
select emp_name,birth_date
    -> from employee_attendance
    -> where day(birth_date)=10;
+----------+------------+
| emp_name | birth_date |
+----------+------------+
| Rahul    | 1998-05-10 |
+----------+------------+

--display emp joined in second quarter
 select emp_name,joining_date
    -> from employee_attendance
    -> where quarter(joining_date)=2;
+----------+--------------+
| emp_name | joining_date |
+----------+--------------+
| Rahul    | 2021-06-15   |
| Anjali   | 2023-04-17   |
| Pooja    | 2022-05-09   |
+----------+--------------+


--emp who have completed more than 3yrs in the company^C
mysql> select emp_name,joining_date
    -> from employee_attendance
    -> where timestampdiff(year,joining_date,curdate())>3;
+----------+--------------+
| emp_name | joining_date |
+----------+--------------+
| Rahul    | 2021-06-15   |
| Sneha    | 2020-03-21   |
| Arjun    | 2019-08-10   |
| Priya    | 2022-01-05   |
| Kiran    | 2018-12-11   |
| Vijay    | 2021-09-14   |
| Divya    | 2019-10-19   |
| Ramesh   | 2017-07-01   |
| Pooja    | 2022-05-09   |
+----------+--------------+
9 rows in set (0.00 sec)

mysql> select emp_name,joining_date
    -> from employee_attendance
    -> where timestampdiff(year,joining_date,curdate())>4;
+----------+--------------+
| emp_name | joining_date |
+----------+--------------+
| Rahul    | 2021-06-15   |
| Sneha    | 2020-03-21   |
| Arjun    | 2019-08-10   |
| Kiran    | 2018-12-11   |
| Divya    | 2019-10-19   |
| Ramesh   | 2017-07-01   |
+----------+--------------+
6 rows in set (0.00 sec)

mysql> --working hours of employee^C
mysql> mysql> select emp_name,
    -> timestampdiff(hour,login_time,logout_time) as working_hours
    -> from employee_attendance;
+----------+---------------+
| emp_name | working_hours |
+----------+---------------+
| Rahul    |             9 |
| Sneha    |             8 |
| Arjun    |             9 |
| Priya    |             8 |
| Kiran    |             8 |
| Anjali   |             8 |
| Vijay    |             9 |
| Divya    |             8 |
| Ramesh   |             9 |
| Pooja    |             9 |
+----------+---------------+
10 rows in set (0.00 sec)

mysql> select emp_name,
    -> timestampdiff(minute,login_time,logout_time) as working_hours
    -> from employee_attendance;
+----------+---------------+
| emp_name | working_hours |
+----------+---------------+
| Rahul    |           550 |
| Sneha    |           530 |
| Arjun    |           559 |
| Priya    |           535 |
| Kiran    |           529 |
| Anjali   |           532 |
| Vijay    |           552 |
| Divya    |           531 |
| Ramesh   |           549 |
| Pooja    |           546 |
+----------+---------------+
10 rows in set (0.00 sec)

display employees whose login time is before 9.00 AM
    -> --Display employees who loged in after 9:10 Am
    -> --display employees who joining dates falls on monday
    -> --display employees whoses birth month startes with letter j
    -> --display employees who joined in week number 25
    -> --display employee names and tha last day of their birth month
    -> --display emoployees with joining date after adding one year
    -> --display employees with their joining date after subtracting two months.
    -> DISPLAY EMPLOYEE LOGIN TIME IN 12-HOUR FORMAT (EXAMPLE: 09:15 AM).
    -> -- DISPLAY EMPLOYEE LOGOUT TIME IN THE FORMAT 28-NOV-2024 06:15 PM.
    -> -- DISPLAY EMPLOYEES WHOSE LOGIN AND LOGOUT OCCURRED ON THE SAME DATE.
=======================================================================================================================================================
