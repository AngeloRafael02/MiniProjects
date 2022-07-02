--NOTE This is the main exe file to make all the SQL tables and views
--Absolute path of files only works on my local system. May changes it in the future 
CREATE DATABASE typeormdb;
\set ON_ERROR_STOP 1
    \c typeormdb
    \i C:/Users/user/Documents/GenshinToDo/Misc/SQL_Scripts/CreateAllTables.sql
    \i C:/Users/user/Documents/GenshinToDo/Misc/SQL_Scripts/InsertSideTableData.sql
    \i C:/Users/user/Documents/GenshinToDo/Misc/SQL_Scripts/CreateCharactersData.sql
    \i C:/Users/user/Documents/GenshinToDo/Misc/SQL_Scripts/CreateWeaponsData.sql
    \i C:/Users/user/Documents/GenshinToDo/Misc/SQL_Scripts/CreateViews.sql
