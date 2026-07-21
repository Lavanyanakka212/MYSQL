Full Stack developers
=====================

Frontend:-
Frontend is a visual and interactive layer of website or application that users directly see and interact with through a webserver or mobile app.

it is also called the client side because it runs on the users device(browser/mobile)

responsibilities of frontend:-
----------------------------
1. Display Webpages and user interface(UI)
2. accepts user input(forms ,buttons, search boxes)
3. validates user input before sending it to the server.
4. calls backend API to fetch or send data.
5. display the response received from backend.
6. provides animations and interactive effects.
by prepare frontend layer we are using some technologies like HTML, CSS, js, Bootstrap.

Backend:-
=======
Backend is the server side part of an application.
users cannot see it directly, but it performs all the business logic ,security, data processing ,and database operations.

it acts as the brain of the application.

Responsibilities of Backend.
----------------------------
1. process clients requests.
2.implements business logic.
3.connects with database.
4.perform crud Operations.
5.Authenticates and authorize users.
6.Encrypts Passwords and Authorize users.
7. generate reports.
8.returns responses to the frontend.
we have to use some languages to build backend java,.net ,php ,c, c++

API(Application Programming Interface):
======================================
API is a set of rules and protocols that two different applications or systems to communicate and exchange data without exposing their internal implementation.

it acts as a bridge between the frontend and backend between two different software systems.

Advantages of APIs:-
--------------------
1. Enables communication between different systems.
2.Promotes code reusability.
3.Platform independent
4.faster application development.
5.supports integration with third-party-services
6.improves scalability.
7.easy to maintain.

Storage Areas:-
=============
as a part of our application we required to store data like customer info, billing info, calls info, ..etc.. To store these data we require some storage areas.

there are two types of storage areas such as:-
1) Temporary Storage areas
---------------------------
these are the memory areas where the data will be stored temporarily.
example:- all JVM memory areas(like heap, stack, method area, pc registers ,native method stack). once the JVM is shut down all these memory areas will be cleared automatically

2) Permanent Storage areas:-
-----------------------------
it is also known as persistent storages areas. where data will be stored permanently.
example:- Filesystems, Database, Data warehouse... etc

File Management Systems(FMS):-
============================
A FILE MANAGEMENT SYSTEM IS A SYSTEM where is data is stored in files on the operating systems.each application program must handle its storage data. Retrieval and updating File systems can be provided by the local operating systems.

File system are best suitable for storing very less amount of information
example:- A library management system storing book in a separate text file like books.txt , members.txt...etc.

limitations of file management system:-
---------------------------------------
1. Data redundancy :- same data is stored in multiple files
2. Data inconsistency:- updates in one file may not be reflected in another
3. Poor data security:- no proper accessed control.
4.Difficult Data Retrieval:- searching requires customs programs.
5. integrity issues:- n
o constraints(ex : roll number uniqueness)
6.scalability issues:- hard to manage as data grows.
To overcome the above problems in the file systems we should go for databases.

Database Management System(DBMS):-
---------------------------------
A DBMS is a collection of programs that ENABLES users to create ,manage and manipulate databases.

it acts as an interface between user and database.

Advantages 
-----------
1. we can store huge amount of information in databases.
2. Query Language support is available for every database and hence we perform database operations easily.
3. to access data present in the database. compulsory username and password must be required hence data is secured.
4.Inside database data will be stored in the forms of tables. while developing database tables schemes ,database admin fallows various normalization techniques and we can implement various constraints like unique key , primary key , ..etc which prevent data duplication. hence there is no chance off data inconsistency  problems

Limitations:-
-------------
1. Databases cannot store huge amount of the information like (terabytes)
2.Database can provide support for unstructured data or semi-structured data like(images, videos ,xml data).

to overcome these problems we should go for some more advanced databases like data warehouses ,big data...et

Difference between file Management System(FMS) and database management system(DBMS):-
======================================================================================
https://tinyurl.com/MySQLPFSSDA-04
