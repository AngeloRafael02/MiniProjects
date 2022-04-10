 --This is a file used in submitting numerous SQl Commands (scripts may be Removed after succesful execution)

ALTER TABLE weapons ALTER COLUMN weapon TYPE integer USING weapon::integer;

--sword
UPDATE weapons SET weapon = 1 WHERE id IN (1,5,6,29,30,31,32,37,2,3,4,94,95,98,96,97,99,25,26,27,28,33,34,35,36,38);
--claymore
UPDATE weapons SET weapon = 2 WHERE id IN (10,11,43,50,52,104,7,8,9,40,41,42,48,100,101,103,44,45,46,47,49,51,102);
--polearm
UPDATE weapons SET weapon = 3 WHERE id IN (12,13,14,62,63,64,109,110,57,58,60,56,59,61,106,53,54,55,105,107,108);
--catalyst
UPDATE weapons SET weapon = 4 WHERE id IN (18,19,77,78,114,115,15,16,17,65,66,67,68,74,75,76,111,112,72,73,70,71,113);
--bow
UPDATE weapons SET weapon = 5 WHERE id IN (23,24,91,92,93,119,120,20,21,22,79,80,81,82,87,88,89,90,116,117,118,83,84,85,86);