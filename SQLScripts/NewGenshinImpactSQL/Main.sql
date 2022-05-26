CREATE DATABASE genshin_impact;

\set ON_ERROR_STOP 1
begin;
    \i tables.sql
    \i SideTable.sql
    \i CharactersData.sql
    (Weapons Table Here)
commit;