USE testbase;
#����P
SELECT gender, COUNT(name) FROM memberlist GROUP BY gender;
#����Q
SELECT gender, COUNT(name) FROM memberlist WHERE age>=20 and age<30 GROUP BY gender;
#����R
SELECT gender, COUNT(name) FROM memberlist WHERE age>=20 and age<30 GROUP BY gender HAVING count(name)=1;
