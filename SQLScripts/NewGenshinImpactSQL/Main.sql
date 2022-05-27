CREATE DATABASE genshin_impact;
\c genshin_impact
\set ON_ERROR_STOP 1
begin;
    \i C:/Users/user/Documents/MiniProjects/SQLScripts/NewGenshinImpactSQL/tables.sql
    \i C:/Users/user/Documents/MiniProjects/SQLScripts/NewGenshinImpactSQL/SideTable.sql
    \i C:/Users/user/Documents/MiniProjects/SQLScripts/NewGenshinImpactSQL/CharactersData.sql
    
    \i C:/Users/user/Documents/MiniProjects/SQLScripts/NewGenshinImpactSQL/createViews.sql
commit;
