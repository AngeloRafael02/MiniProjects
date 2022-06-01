CREATE DATABASE test4_db;
\set ON_ERROR_STOP 1
begin;
    \c test4_db
    \i C:/Users/user/Documents/MiniProjects/SQLScripts/NewGenshinImpactSQL/CreateAllTables.sql
    \i C:/Users/user/Documents/MiniProjects/SQLScripts/NewGenshinImpactSQL/InsertSideTableData.sql
    \i C:/Users/user/Documents/MiniProjects/SQLScripts/NewGenshinImpactSQL/CreateCharactersData.sql
    \i C:/Users/user/Documents/MiniProjects/SQLScripts/NewGenshinImpactSQL/CreateWeaponsData.sql
    \i C:/Users/user/Documents/MiniProjects/SQLScripts/NewGenshinImpactSQL/CreateViews.sql
commit;\least
