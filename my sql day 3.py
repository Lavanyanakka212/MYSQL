------SQL Identifier-----

sql identifier are name used to identify database object such as database names,tables names,column names,view names,index names,constraints
triggers,stroed procedures..etc..

while we are declaring ibentifiers we have to follow somen rules and regulation.
1.the only allowed characters to  define identifier a-z,A-Z,or 0-9,_,$
2. must be begin with letter or underscore(_)
3.we can't declare identifier with reserved words.
4.spaces are not considered to declare identifier.
5.identifier are case senstive
6.max length to declare identifier are 15 character.

SQL
-------------
sql(structure query language) is standardized programming language specially designed for managing and manipulating relational database.it provives a
declaration syntax that allows users to define what data they retrieve,insert,update,or delete
without specifing exactly how database should execute these operation,

SQL commands
----------
1.DDL(data definition language): DDl commands are used to define,create,mofify and delete the structure os a database object sucha as database,tables,views
index and constriants.

*create:by using these commads to create a new database,tables,views,indexs,,etc.

alter:by using these commads we can modifies the structure of an existing table.like(add column,drop column,rename column,modufy database,add constarints)

drop:delets an entries database object perminetly like(database,tables,views,index..etc)

truncate: by using truncate command delete all records from a table without deleting the table.

rename:it is used to rename the database object names.

2.DML(data manipulation language):manages data stroed within database object.

insert:- by using insert commands we can insert some records into a table

update:-by using the update commands we can update the records based on some condition.

delete:-by using the delete commands we can delete some records based on some condition

lock:-controls concurrency by locking a tables restrict accesses from other transaction while it is being modified.

3.DCL(data control language):manage permission and access control on database object.

grant:-gives specific privilages or permission(such select,update,insert,delete,all privilagoues)to a database user or role.

revoke:removes previously granted permission from database user or role.restricting their accesses to database object.

4.TCL:manage to maintain data intergrity.

commit:-permanently saves all changes made during the current transaction  to the database.making them visible to other users.

rollback:-undoes/reverts changes made during the current transaction back to the last commited stsate or a savepoint in case of an error.

savepoint:-set a temporary market within a transaction to you which you can later rollback,without undoing
the entire transaction.

5.DQL:-used to fetch

create
--------
how to create database?
-------------------
syntax:create database database_name;
ex:create database pfs4;

 how to drop the database
 ---------------------
 syntax:drop database database-name;

 create tables
 ----------------
 CREATE TABLE TABLE-NAME(
column-name data-type(size)








































