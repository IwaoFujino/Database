USE testbase;
SHOW tables;
SELECT * FROM memberlist;
SELECT * FROM memberlist WHERE age>=22 AND age <=30;
SELECT * FROM memberlist WHERE age<22 OR age >30;
SELECT * FROM memberlist WHERE gender='女' AND age>=22;
SELECT * FROM memberlist WHERE NOT (gender='女' AND age>=22);

