Numeric Functions:-
===================

abs():- absolute valueos a number
ceil():- rounded up
floor():- rounded down
round():- round to a specific number of digits
mof():- modulo value
pow():- exponential value
sqrt():- square root
RADIANS() -- CONVERT DEGREES TO RADIANS
DEGREE() CONVERT RADIANS TO DEGREES
SIGN()-- RETUNRS SIGN OF A NUMBER
    -> 1 FOR POSTIVE NUMBERS
    -> -1 FOR NEGATIVE NUMBERS
    -> 0 FOR ZERO^C
RAND() GENERATE A RANDOM NUMBER
PI() RETURNS A PI VALUE
GREATEST() FIND THE MAXIMUN VALUE
LEAST() FINDS LEAST VALUE
 LOG2() CONVERTS NUMBER INTO BASE 2(RETUNRS BASE-2 LOGRITHAM)
LOG10() BASE 10
BIT_COUNT() RETURNS THE BITS VALUES(LCM REMAININGS)
 OCT() RETURNS THE REMAINING BIT value(LCM OF 62 GIVES 100 OUTPUT)
BIT() 

mysql> SELECT ABS(-100) AS ABSOLUTE_VALUE;
+----------------+
| ABSOLUTE_VALUE |
+----------------+
|            100 |
+----------------+
1 row in set (0.01 sec)

mysql> SELECT CEIL(12.34) AS ROUNDED_UI;
+------------+
| ROUNDED_UI |
+------------+
|         13 |
+------------+
1 row in set (0.02 sec)

mysql> SELECT FLOOR(12.34) AS ROUNDED_DOWN;
+--------------+
| ROUNDED_DOWN |
+--------------+
|           12 |
+--------------+
1 row in set (0.00 sec)

mysql> SELECT ROUND(12.3456,2) AS ROUNDED_VALUE;
+---------------+
| ROUNDED_VALUE |
+---------------+
|         12.35 |
+---------------+
1 row in set (0.00 sec)

mysql> SELECT MOD(17,5) AS REMINDER;
+----------+
| REMINDER |
+----------+
|        2 |
+----------+
1 row in set (0.00 sec)

mysql> SELECT POW(2,3) AS POWER_VALUE;
+-------------+
| POWER_VALUE |
+-------------+
|           8 |
+-------------+
1 row in set (0.00 sec)

mysql> SELECT SQRT(16) AS SQUARE_ROOT;
+-------------+
| SQUARE_ROOT |
+-------------+
|           4 |
+-------------+
1 row in set (0.00 sec)

mysql> SELECT LOG(10) AS LOG_VALUE;
+-------------------+
| LOG_VALUE         |
+-------------------+
| 2.302585092994046 |
+-------------------+
1 row in set (0.00 sec)

mysql> SELECT LOG(10,100) AS LOG_VALUE;
+-----------+
| LOG_VALUE |
+-----------+
|         2 |
+-----------+
1 row in set (0.00 sec)

mysql> --RADIANS -- CONVERT DEGREES TO RADIANS
    -> ^C
mysql> SELECT RADIANS(100) AS RADIANS_VALUE;
+--------------------+
| RADIANS_VALUE      |
+--------------------+
| 1.7453292519943295 |
+--------------------+
1 row in set (0.00 sec)

mysql> --DEGREE() CONVERT RADIANS TO DEGREES^C
mysql> SELECT DEGREES(PI()) AS DEGREES_VALUE;
+---------------+
| DEGREES_VALUE |
+---------------+
|           180 |
+---------------+
1 row in set (0.00 sec)

mysql> --SIGN()-- RETUNRS SIGN OF A NUMBER
    -> 1 FOR POSTIVE NUMBERS
    -> -1 FOR NEGATIVE NUMBERS
    -> 0 FOR ZERO^C
mysql> SELECT SIGN(-100) AS SIGN_VALUE;
+------------+
| SIGN_VALUE |
+------------+
|         -1 |
+------------+
1 row in set (0.00 sec)

mysql> SELECT SIGN(100) AS SIGN_VALUE;
+------------+
| SIGN_VALUE |
+------------+
|          1 |
+------------+
1 row in set (0.00 sec)

mysql> SELECT SIGN(0) AS SIGN_VALUE;
+------------+
| SIGN_VALUE |
+------------+
|          0 |
+------------+
1 row in set (0.00 sec)

mysql> RAND() GENERATE A RANDOM NUMBER^C
mysql> SELECT RAND() AS RANDOM_NUMBER;
+---------------------+
| RANDOM_NUMBER       |
+---------------------+
| 0.04027216047073916 |
+---------------------+
1 row in set (0.00 sec)

mysql> SELECT RAND() AS RANDOM_NUMBER;
+--------------------+
| RANDOM_NUMBER      |
+--------------------+
| 0.4937951504195064 |
+--------------------+
1 row in set (0.00 sec)

mysql> SELECT RAND(4) AS RANDOM_NUMBER;
+---------------------+
| RANDOM_NUMBER       |
+---------------------+
| 0.15595286540310166 |
+---------------------+
1 row in set (0.00 sec)

mysql> GREATEST() FIND THE MAXIMUN VALUE^C
mysql> SELECT GREATEST(5,10,15,20) AS GREATEST_VALUE;
+----------------+
| GREATEST_VALUE |
+----------------+
|             20 |
+----------------+
1 row in set (0.00 sec)

mysql> SELECT LEAST(-5,-10,15,-20) AS LEAST_VALUE;
+-------------+
| LEAST_VALUE |
+-------------+
|         -20 |
+-------------+
1 row in set (0.01 sec)

mysql> PI() RETURNS A PI VALUE^C
mysql> SELECT PI() AS PI_VALUE;
+----------+
| PI_VALUE |
+----------+
| 3.141593 |
+----------+
1 row in set (0.00 sec)

mysql> TRUNCATE-- REMOVES SPACES FROM FIRST AND LAST
    -> ^C
mysql> SELECT TRUNCATE(12.3356,2) AS TRUNCATED_VALUE;
+-----------------+
| TRUNCATED_VALUE |
+-----------------+
|           12.33 |
+-----------------+
1 row in set (0.00 sec)

mysql> LOG2() CONVERTS NUMBER INTO BASE 2^C
mysql> SELECT LOG2(8) AS LOG2_VALUE;
+------------+
| LOG2_VALUE |
+------------+
|          3 |
+------------+
1 row in set (0.00 sec)

mysql> SELECT LOG10(1000) AS LOG10_VALUE;
+-------------+
| LOG10_VALUE |
+-------------+
|           3 |
+-------------+
1 row in set (0.00 sec)

mysql> BIT_COUNT()^C
mysql>
mysql> SELECT BIT_COUNT(7) AS SET_BITS_VALUE
    -> ;
+----------------+
| SET_BITS_VALUE |
+----------------+
|              3 |
+----------------+
1 row in set (0.00 sec)

mysql> OCT() RETURNS THE REMAINING BIT valuee^C
mysql> SELECT OCT(64) AS OCTAL_VALUE;
+-------------+
| OCTAL_VALUE |
+-------------+
| 100         |
+-------------+
 SELECT BIN(64) AS BIN_VALUE;
+-----------+
| BIN_VALUE |
+-----------+
| 1000000   |
+-----------+
1 row in set (0.00

mysql> select*from employees;
+--------+------------+-----------+-------------------------+--------------+------------+-----------+----------+
| emp_id | first_name | last_name | email                   | phone_number | department | city      | salary   |
+--------+------------+-----------+-------------------------+--------------+------------+-----------+----------+
|    101 | Rahul      | Kumar     | rahul.kumar@gmail.com   | 987-654-3210 | IT         | Hyderabad | 45000.00 |
|    102 | Anita      | Sharma    | anita.sharma@yahoo.com  | 912-345-6789 | HR         | Bangalore | 38000.00 |
|    103 | Suresh     | Verma     | suresh.verma@gmail.com  | 998-123-4567 | Sales      | Chennai   | 52000.00 |
|    104 | Priya      | Singh     | priya.singh@outlook.com | 900-456-7890 | Finance    | Pune      | 47000.00 |
|    105 | Rahul      | Joshi     | rahul.joshi@gmail.com   | 955-888-1111 | Testing    | Delhi     | 41000.00 |
|    106 | Kiran      | Reddy     | kiran.reddy@gmail.com   | 901-222-3333 | IT         | Hyderabad | 56000.00 |
|    107 | Deepika    | Naidu     | deepika.naidu@yahoo.com | 944-111-2222 | HR         | Vizag     | 39000.00 |
|    108 | Mahesh     | Patel     | mahesh.patel@gmail.com  | 933-444-5555 | Sales      | Mumbai    | 62000.00 |
|    109 | Divya      | Gupta     | divya.gupta@gmail.com   | 955-777-8888 | Finance    | Delhi     | 49000.00 |
|    110 | Arjun      | Rao       | arjun.rao@gmail.com     | 988-999-7777 | Developer  | Hyderabad | 68000.00 |
+--------+------------+-----------+-------------------------+--------------+------------+-----------+----------+
--display full name by concatenating first name and last name 
select first_name,last_name,concat(first_name,' ',last_name)as full_name from employeees;
+------------+-----------+---------------+
| first_name | last_name | full_name     |
+------------+-----------+---------------+
| Rahul      | Kumar     | Rahul Kumar   |
| Anita      | Sharma    | Anita Sharma  |
| Suresh     | Verma     | Suresh Verma  |
| Priya      | Singh     | Priya Singh   |
| Rahul      | Joshi     | Rahul Joshi   |
| Kiran      | Reddy     | Kiran Reddy   |
| Deepika    | Naidu     | Deepika Naidu |
| Mahesh     | Patel     | Mahesh Patel  |
| Divya      | Gupta     | Divya Gupta   |
| Arjun      | Rao       | Arjun Rao     |
+------------+-----------+---------------+
10 rows in set (0.00 sec)

mysql> -- CONVERT FIRST_NAME TO UPPER CASE
mysql> SELECT first_name,UPPER(FIRST_NAME)AS UPPER_NAME FROM EMPLOYEESS;
+------------+------------+
| first_name | UPPER_NAME |
+------------+------------+
| Rahul      | RAHUL      |
| Anita      | ANITA      |
| Suresh     | SURESH     |
| Priya      | PRIYA      |
| Rahul      | RAHUL      |
| Kiran      | KIRAN      |
| Deepika    | DEEPIKA    |
| Mahesh     | MAHESH     |
| Divya      | DIVYA      |
| Arjun      | ARJUN      |
+------------+------------+
10 rows in set (0.00 sec)

--covert last name to lower case
mysql> SELECT LAST_NAME,LOWER(LAST_NAME)AS LOWER_NAME FROM EMPLOYEESS;
+-----------+------------+
| LAST_NAME | LOWER_NAME |
+-----------+------------+
| Kumar     | kumar      |
| Sharma    | sharma     |
| Verma     | verma      |
| Singh     | singh      |
| Joshi     | joshi      |
| Reddy     | reddy      |
| Naidu     | naidu      |
| Patel     | patel      |
| Gupta     | gupta      |
| Rao       | rao        |
+-----------+------------+
10 rows in set (0.00 sec)

select email,substring(email,1,10) as email_prefix from employees;
+-------------------------+--------------+
| email                   | email_prefix |
+-------------------------+--------------+
| rahul.kumar@gmail.com   | rahul.kuma   |
| anita.sharma@yahoo.com  | anita.shar   |
| suresh.verma@gmail.com  | suresh.ver   |
| priya.singh@outlook.com | priya.sing   |
| rahul.joshi@gmail.com   | rahul.josh   |
| kiran.reddy@gmail.com   | kiran.redd   |
| deepika.naidu@yahoo.com | deepika.na   |
| mahesh.patel@gmail.com  | mahesh.pat   |
| divya.gupta@gmail.com   | divya.gupt   |
| arjun.rao@gmail.com     | arjun.rao@   |
+-------------------------+--------------+
10 rows in set (0.00 sec)

mysql> --find the length of the first name^C
mysql> select first_name, length(first_name) as name_lemgth from employees;
+------------+-------------+
| first_name | name_lemgth |
+------------+-------------+
| Rahul      |           5 |
| Anita      |           5 |
| Suresh     |           6 |
| Priya      |           5 |
| Rahul      |           5 |
| Kiran      |           5 |
| Deepika    |           7 |
| Mahesh     |           6 |
| Divya      |           5 |
| Arjun      |           5 |
+------------+-------------+
10 rows in set (0.00 sec)

mysql> select*from employees;
+--------+------------+-----------+-------------------------+--------------+------------+-----------+----------+
| emp_id | first_name | last_name | email                   | phone_number | department | city      | salary   |
+--------+------------+-----------+-------------------------+--------------+------------+-----------+----------+
|    101 | Rahul      | Kumar     | rahul.kumar@gmail.com   | 987-654-3210 | IT         | Hyderabad | 45000.00 |
|    102 | Anita      | Sharma    | anita.sharma@yahoo.com  | 912-345-6789 | HR         | Bangalore | 38000.00 |
|    103 | Suresh     | Verma     | suresh.verma@gmail.com  | 998-123-4567 | Sales      | Chennai   | 52000.00 |
|    104 | Priya      | Singh     | priya.singh@outlook.com | 900-456-7890 | Finance    | Pune      | 47000.00 |
|    105 | Rahul      | Joshi     | rahul.joshi@gmail.com   | 955-888-1111 | Testing    | Delhi     | 41000.00 |
|    106 | Kiran      | Reddy     | kiran.reddy@gmail.com   | 901-222-3333 | IT         | Hyderabad | 56000.00 |
|    107 | Deepika    | Naidu     | deepika.naidu@yahoo.com | 944-111-2222 | HR         | Vizag     | 39000.00 |
|    108 | Mahesh     | Patel     | mahesh.patel@gmail.com  | 933-444-5555 | Sales      | Mumbai    | 62000.00 |
|    109 | Divya      | Gupta     | divya.gupta@gmail.com   | 955-777-8888 | Finance    | Delhi     | 49000.00 |
|    110 | Arjun      | Rao       | arjun.rao@gmail.com     | 988-999-7777 | Developer  | Hyderabad | 68000.00 |
+--------+------------+-----------+-------------------------+--------------+------------+-----------+----------+
10 rows in set (0.00 sec)

mysql> --remove dashes from phone number^C
mysql> select pjone_number, replace(phone_munber,'-','') as clean_phone from employees;
ERROR 1054 (42S22): Unknown column 'pjone_number' in 'field list'
mysql> select phone_number, replace(phone_munber,'-','') as clean_phone from employees;
ERROR 1054 (42S22): Unknown column 'phone_munber' in 'field list'
mysql> select phone_number, replace(phone_number,'-','') as clean_phone from employees;
+--------------+-------------+
| phone_number | clean_phone |
+--------------+-------------+
| 987-654-3210 | 9876543210  |
| 912-345-6789 | 9123456789  |
| 998-123-4567 | 9981234567  |
| 900-456-7890 | 9004567890  |
| 955-888-1111 | 9558881111  |
| 901-222-3333 | 9012223333  |
| 944-111-2222 | 9441112222  |
| 933-444-5555 | 9334445555  |
| 955-777-8888 | 9557778888  |
| 988-999-7777 | 9889997777  |
+--------------+-------------+
10 rows in set (0.00 sec)

mysql> --remove leading and trailing spaces from first name^C
mysql> select trim(first_name) as trimmed_name from employees;
+--------------+
| trimmed_name |
+--------------+
| Rahul        |
| Anita        |
| Suresh       |
| Priya        |
| Rahul        |
| Kiran        |
| Deepika      |
| Mahesh       |
| Divya        |
| Arjun        |
+--------------+
10 rows in set (0.00 sec)

mysql> --concatenates first_name,last_name,email seperatedby comma^C
mysql> select concat_ws(',', first_name,last_name,email) as employee_info from employees;
+---------------------------------------+
| employee_info                         |
+---------------------------------------+
| Rahul,Kumar,rahul.kumar@gmail.com     |
| Anita,Sharma,anita.sharma@yahoo.com   |
| Suresh,Verma,suresh.verma@gmail.com   |
| Priya,Singh,priya.singh@outlook.com   |
| Rahul,Joshi,rahul.joshi@gmail.com     |
| Kiran,Reddy,kiran.reddy@gmail.com     |
| Deepika,Naidu,deepika.naidu@yahoo.com |
| Mahesh,Patel,mahesh.patel@gmail.com   |
| Divya,Gupta,divya.gupta@gmail.com     |
| Arjun,Rao,arjun.rao@gmail.com         |
+---------------------------------------+
10 rows in set (0.00 sec)

mysql> --find the position of the letter 'a' in first_name using position()^C
mysql> select first_name,position('a' in first_name) as position_of_a from employees;
+------------+---------------+
| first_name | position_of_a |
+------------+---------------+
| Rahul      |             2 |
| Anita      |             1 |
| Suresh     |             0 |
| Priya      |             5 |
| Rahul      |             2 |
| Kiran      |             4 |
| Deepika    |             7 |
| Mahesh     |             2 |
| Divya      |             5 |
| Arjun      |             1 |
+------------+---------------+
10 rows in set (0.00 sec)

mysql> --display the first three caracters of first name^C
mysql>  select first_name,left(first_name,3) as short_name from employees;
+------------+------------+
| first_name | short_name |
+------------+------------+
| Rahul      | Rah        |
| Anita      | Ani        |
| Suresh     | Sur        |
| Priya      | Pri        |
| Rahul      | Rah        |
| Kiran      | Kir        |
| Deepika    | Dee        |
| Mahesh     | Mah        |
| Divya      | Div        |
| Arjun      | Arj        |
+------------+------------+
10 rows in set (0.00 sec)

mysql> --display last 3 characters of last_name^C
mysql> select last_name,right(last_name,3) as short_last from employees;
+-----------+------------+
| last_name | short_last |
+-----------+------------+
| Kumar     | mar        |
| Sharma    | rma        |
| Verma     | rma        |
| Singh     | ngh        |
| Joshi     | shi        |
| Reddy     | ddy        |
| Naidu     | idu        |
| Patel     | tel        |
| Gupta     | pta        |
| Rao       | Rao        |
+-----------+------------+
10 rows in set (0.00 sec)

mysql> --reverse the first name^C
mysql> select first_name,reverse(first_name) as reverse_name from employees;
+------------+--------------+
| first_name | reverse_name |
+------------+--------------+
| Rahul      | luhaR        |
| Anita      | atinA        |
| Suresh     | hseruS       |
| Priya      | ayirP        |
| Rahul      | luhaR        |
| Kiran      | nariK        |
| Deepika    | akipeeD      |
| Mahesh     | hsehaM       |
| Divya      | ayviD        |
| Arjun      | nujrA        |
+------------+--------------+
10 rows in set (0.00 sec)

mysql> --pad first name of the left with the * to make it with 10 characters^C
mysql> select first_name,lpad(first_name,10,'*') as padded_name from employees;
+------------+-------------+
| first_name | padded_name |
+------------+-------------+
| Rahul      | *****Rahul  |
| Anita      | *****Anita  |
| Suresh     | ****Suresh  |
| Priya      | *****Priya  |
| Rahul      | *****Rahul  |
| Kiran      | *****Kiran  |
| Deepika    | ***Deepika  |
| Mahesh     | ****Mahesh  |
| Divya      | *****Divya  |
| Arjun      | *****Arjun  |
+------------+-------------+
10 rows in set (0.00 sec)

mysql> select first_name,rpad(first_name,10,'*') as padded_name from employees;
+------------+-------------+
| first_name | padded_name |
+------------+-------------+
| Rahul      | Rahul*****  |
| Anita      | Anita*****  |
| Suresh     | Suresh****  |
| Priya      | Priya*****  |
| Rahul      | Rahul*****  |
| Kiran      | Kiran*****  |
| Deepika    | Deepika***  |
| Mahesh     | Mahesh****  |
| Divya      | Divya*****  |
| Arjun      | Arjun*****  |
+------------+-------------+
10 rows in set (0.00 sec)

mysql> --find ascii value of a first character in first name^C
mysql> select first_name,ascii(first_name) as ascii_value from employees;
+------------+-------------+
| first_name | ascii_value |
+------------+-------------+
| Rahul      |          82 |
| Anita      |          65 |
| Suresh     |          83 |
| Priya      |          80 |
| Rahul      |          82 |
| Kiran      |          75 |
| Deepika    |          68 |
| Mahesh     |          77 |
| Divya      |          68 |
| Arjun      |          65 |
+------------+-------------+
10 rows in set (0.00 sec)

mysql> --find the character length of last name ^C
mysql> select last_name,char_length(last_name)as char_length from employees;
+-----------+-------------+
| last_name | char_length |
+-----------+-------------+
| Kumar     |           5 |
| Sharma    |           6 |
| Verma     |           5 |
| Singh     |           5 |
| Joshi     |           5 |
| Reddy     |           5 |
| Naidu     |           5 |
| Patel     |           5 |
| Gupta     |           5 |
| Rao       |           3 |
+-----------+-------------+
======================================================
questions:-
 --find the employees whose first name starts with R^C
mysql> --find employess whoses email contains 'yahoo'_
    -> dispaly full name along with department as a single string
    -> find the length of every email address
    -> find employees whose first_name has more than 5 chracters
    -> replace 'gmail.com' with 'company.name' in email
    -> find the position of the '@' symbol in email
    -> extract the username part of email(before @) using substring_index()
    -> extract the domain partt of email(after @) using substring_index()
    -> find employees whose last_name ends with 'a'
============================================================================
 ->mask email addresses,showing only the first 3 characters before @
mysql> select email,concat(left(email,3),'****@',substring_index(email,'@',-1)) as masked_email from employees;
+-------------------------+---------------------+
| email                   | masked_email        |
+-------------------------+---------------------+
| rahul.kumar@gmail.com   | rah****@gmail.com   |
| anita.sharma@yahoo.com  | ani****@yahoo.com   |
| suresh.verma@gmail.com  | sur****@gmail.com   |
| priya.singh@outlook.com | pri****@outlook.com |
| rahul.joshi@gmail.com   | rah****@gmail.com   |
| kiran.reddy@gmail.com   | kir****@gmail.com   |
| deepika.naidu@yahoo.com | dee****@yahoo.com   |
| mahesh.patel@gmail.com  | mah****@gmail.com   |
| divya.gupta@gmail.com   | div****@gmail.com   |
| arjun.rao@gmail.com     | arj****@gmail.com   |
+-------------------------+---------------------+

 -> check if employees first name is a palindrome
select first_name from employees where lower(first_name)=lower(reverse(first_name));
Empty set (0.00 sec)

->generate a username using the firstletter of the first name plus the full lastname in lowercase

select concat(lower(left(first_name,1)),lower(last_name)) as username from employees;
+----------+
| username |
+----------+
| rkumar   |
| asharma  |
| sverma   |
| psingh   |
| rjoshi   |
| kreddy   |
| dnaidu   |
| mpatel   |
| dgupta   |
| arao     |
+----------+

 ->categorixe the employees as short name and long name based on the length of the first name

select first_name,
    -> case when length(first_name)<=5 then 'short-name'
    -> else 'long-name' end as name_category
    -> from employees;
+------------+---------------+
| first_name | name_category |
+------------+---------------+
| Rahul      | short-name    |
| Anita      | short-name    |
| Suresh     | long-name     |
| Priya      | short-name    |
| Rahul      | short-name    |
| Kiran      | short-name    |
| Deepika    | long-name     |
| Mahesh     | long-name     |
| Divya      | short-name    |
| Arjun      | short-name    |
+------------+---------------+
