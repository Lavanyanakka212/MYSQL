mysql> CREATE TABLES EMPLOYEES(
    -> FNAME VARCHAR(100),
    -> EMID CHAR(5),
    -> LNAME VARCHAR(60),
    -> AGE INT,
    -> DOJ DATE,
    -> ADDRESS TINYTEXT,
    -> DEPT VARCHAR(50)
    -> );
 common uses of alter tables
 --------------------------------
 1.add a column
 2.modify an existing column(type,size,default.etc)
 3.drop a column
 4.rename a column or tables.
 5.add or remove constraints
 6.changes column order (in some database)

 syntax
 --------------------
 alter  table table-name <modification>;
 adding a new column to the existing tables
syntax
 ------------------
 alter table table-name add column-name.
 
ADDING COLUMN:
 add a new column after a particular column
 
syntax:
----------------
ALTER TABLE TABLE-NAME ADD COLUMN-NAME DATATYPE(SIZE) A SPECIFIED COLUMN-NAME

COLUMN MODIFING:
---------------------
    
MODIFY THE NAME COLUMN IN EMPLOYEES TABLES TO VARCHAR(50)

SYNTAX:

ALTER TABLES EMPLOYEES MODITY FNAME VARCHAR(50);

CHANGE COLUMN NAME
---------------------------
ALTER TABLE TABLES-NAME CHANGE EXISTING-COLUMN-NAME NEW COLUMN-NAME DATATYPE(SIZE)

SYNTAX:
    ALTER TABLE EMPLOYEES CHANGE FNAME FIRST VARCHER(30);

TO DROP A COLUMN
----------------
ALTER TABLE TABLE-NAME DROP COLUMN COLUMN-NAME

SYNTAX:
    ALTER TABLE EMPLOYEE DROP COLUMN PFID;

CHANGE THE TABLE-NAME
--------------------

    ALTER TABLE EXISTING-TABLE-NAME RENAME TO NEW-TABLE-NAME
SYNTAX:
    ALTER TABLE EMPLOYEE RENAME TO CODEGNAN_EMP;


    
    

