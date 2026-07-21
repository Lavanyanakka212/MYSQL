DAY-2:
------------
what are the diff btw fms and databasse management system(dbms)
http://tinyurl.com/MYSQLLPFSDA-04
1. high data redundancy (duplicate data)
reduce data redundancy.
2.diffcult to main tain and update.
easy to maintain and uodate
3. security is limited.
provides strong security mechansim
4. data sharing is diffcult
multiple users can access data simultaneously.
5. no relationship between tables.
support relationship between tables.
6.backup and recovery is diffcult
provides backup and recovery features.
7.suitable for small application
suitable for small,medium and large application.

q:what is the difference between a file system and a dbms?(iq)
----------------------------------------------------------------
a file system store data in seprate  files may leas to data redundancy,and security issues.A dbms stroes data in a structured manner using tables,reduces
redundancy,providess security,support multiple users,and ensure data consistency and integrity,

what is data,field,record,database
-------------------------------------------
what os data?
raw facts or figures without context
ex:101,lavanya,300000,viz

what is feild
--------------------------
smallest unit of data in database(column/attribute)
ex:empid,empname,empsalary

what is record
-------------------------------
collection of related feild(rows/tuple)
ex:(1o1,lavanya,3000000)
 what is databse
 -------------------------------------
 organied collection of related records stroed together
 ex:in employee database contain all employee details

 what is dbms
 -----------------------------
 a dbms is a software used to create,store,retrive,update and manage database.

 client-server architecture
 --------------------------
 in client-server arch they have 3 components such as
 client
 server
 protocol

 client:the role of the client in client -server arch is send request to yhe server and to get response from the server.

 server:server is a software the role of the server in client-server-arch is to take request from clientsif the request is valid request then it will
 generates some response  we can handover that response to client.if the client request is not a valid request then it will raise the error.

 protocol
 =================
 it has a set of rules and regulation the role of the protocol in cluent-server arch is to send request from client to server.

 datamodels in dbms
 ---------------------------
 def:a data model defines how data is stored,organized and manipulated in a database.
 
 1.physical data model--->describes how data is physically stroed in stroage devices.
 audience:database adminstrators

 2.logical data model------>defines the structure of data(entities,attributes,relationship)independent of physical stroage areas
audiences:developers and data base architects.

3.hierarchical data model---->data is represented as a tree structure.(parents child relationship)
ex:company-->departments---->employee

4.network data model--->data is represented as graph with records(nodes)and relationship(edges)
ex:student enrolled in multiple courses,course teach by multiple professor.

5.relation data model(rdbms)------>data is stroed in tables(relations)with rows(tuple)and columns(attributes)
ex:student(id,mame,marks,dept_id)
departments(dept_id,dept_name)
    























