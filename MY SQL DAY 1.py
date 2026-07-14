frontend
=====
frontend is a visual inter active layer of a website or application that users directly see and interact wiyh through a webserver or mobile app.
 it is also called the client side because it runs on the users.(browser/mobile)

responbilities of frontend
----------------------
1. display web pages and user interface(ui)
2.accept user input(forms,button,search boxes)
3.validates user input before sending it to the server.
4.calls backend api to fetch
or send data.
5.display the respone received from bachend.
6.provide animation and interactive

backend
-------------
backend is the server -side part of an application
user cannot see it directly ,but it perform all the business logic,sercurity,data,procesiing and data operation.

it acts as the brain of the application

responabilities of backend
-----------------
process client request
implements business logic
connects with database
perform crud operation
authentication and authorize users
encrypts password and authorize users
generates reports
returns respone to the fronted
we have to some lan

api(application programming interfaces)------------
______________
api is a set


it acts as bridge between the fronted and backend two different software system.

advantage of api

enables communication beywwen differebt system
promotes code reusability
platform independent
faster application development
supports ingegration with third party service
improves scalability
easy to maintain

stroges areas
--------------------
as part of our application we required to store data like customer info,billing info,calls info ect. to store these data we reqire some storgare areas.

there are two types of stroage areas such as
1.temporary stroage areas
----------------
these are the memory areas where the data will be stroed temporally
ex:all jvm memory areas(like heap,stack,methodarea,pc register, native methodstack).
once jvm is shutdown all these memory areas will be cleared automatically

2. permanent 
-------------
it is also known as persistent stroage areas.where data will be stroed permantly
ex:filesystem,database,dat warehouse..etc
 file management system(fms)

---------------
a file management system is a system where data is stored in files on the operating system.each application program must handle
its own stroage data.retrival and updating filesystem can be provided by the local operating system.

file system are best suitable for to store very least amount infromation
ex:a library management system stroing books in a separates text file likes books,txt,member.txt..etc.
1.data redundancy: same data is stored in multiple files
2:data incosistency:updates in one file may not be reflected in another
3.poor data sercuity: no proper accessed control
4.diffcuilt data retrieval:searching requries custom program.
5.intergrity issues:no constraints(ex:roll numb uniquenessss)
6.scalaability issues:hard to manage as data grows
to overcome the above problem in files system we should go for database

data base management systen(dbms)
a dbms is a collection of program that enables user to creates, manage and manipulate database.
it acts as an interface between user and databasr

advantages
------
1.we can stroe huge amount of infromation in database
2.query language support is avaiable foe every database and hence we peform
data base operation easily
3.to access data present in the database complusory username and passwored must be reqired

4.
limitations of database
--------------------
1.database cannot store huge amount of infromation like(terabytes)
2.database can provides supports for only structured data(tabuar data or relational data)
and cannot provides support for unstricture data or semi structure data(likes videos,audios,xml.etc)

 to overcome these problem we should go for some more advanced database like data
warehouse,big data etc...

what are the diff btw fms and databasse management system(dbms)
http://tinyurl.com/MYSQLLPFSDA-04



































